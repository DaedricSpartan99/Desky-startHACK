#from django.shortcuts import render
from rest_framework import views, parsers
from rest_framework.response import Response
from django.db.models import Count
from django_eventstream import send_event

# Create your views here.

#from django.http import HttpResponse
from transactions.serializers import BondSerializer, BrokerSerializer, TransactionSerializer, PositioningSerializer
from transactions.models import Bond, Broker, Transaction, TradeStatus, Currency

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


# act on all transactions
@csrf_exempt
def transactions_list(request):
    #List all, or create a new.
    if request.method == 'GET':
        trades = Transaction.objects.all()
        serializer = TransactionSerializer(trades, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():

            # save serialized data
            serializer.save()

            # notify clients of new row
            send_event('transactions', 'message', {'request' : 'POST', 'source' : request.META['HTTP_USER_AGENT'], 'data' : serializer.data})

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


# act on single transaction
@csrf_exempt
def transaction_detail(request, pk):
    #Retrieve, update or delete.
    try:
        trade = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TransactionSerializer(trade)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TransactionSerializer(trade, data=data, partial=True)
        if serializer.is_valid():

            # save serialized data
            serializer.save()

            # notify users of refresh
            send_event('transactions', 'message', {'request' : 'PUT', 'source' : request.META['HTTP_USER_AGENT'], 'data' : serializer.data})

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        trade.delete()

        # notify users of refresh
        send_event('transactions', 'message', {'request' : 'DELETE', 'source' : request.META['HTTP_USER_AGENT'], 'id' : pk})

        return HttpResponse(status=204)


# specific behaviour
@csrf_exempt
def local_transaction_after(request, after):
    
    # parse date
    # TODO change format
    date = datetime.strptime(after, "%Y-%d-%m").date()

    if request.method == 'GET':
        # get dates greater or equal than requested
        trades = Transaction.objects.exclude(trade_status="CONF").filter(trade_date__gte=date)
        serializer = TransactionSerializer(trades, many=True)
        return JsonResponse(serializer.data, safe=False)

# return all transactions between date range
@csrf_exempt
def local_transaction_range(request, start, end):
    
    # parse date
    # TODO change format
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date() + timedelta(days=1)

    print("Start date: ", start_date)
    print("End date: ", end_date)

    if request.method == 'GET':
        # get dates greater or equal than requested
        trades = Transaction.objects.filter(trade_datetime__range=[start_date, end_date])
        serializer = TransactionSerializer(trades, many=True)
        return JsonResponse(serializer.data, safe=False)


# get data needed for the positioning
@csrf_exempt
def get_positioning(request):

    start_date = request.GET.get("startDate", None)
    end_date = request.GET.get("endDate", None)

    # parse trade date range
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date() + timedelta(days=1)

    # get actors
    bond = request.GET.get("bond", None)
    broker = request.GET.get("broker", None)

    # get status
    status = request.GET.get("status", "active,pending,confirmed,cancelled")
    # get market BID, TODO custom parameters
    market_bid = request.GET.get("marketBid", 0.) 

    if request.method == 'GET':
        # get dates greater or equal than requested
        trades = Transaction.objects.filter(trade_datetime__range=[start_date, end_date])
            
        # filter by bond
        if bond is not None:
            trades = trades.filter(bond__name__exact=bond)

        # filter by broker
        if broker is not None:
            trades = trades.filter(broker__name__exact=broker)

        # filter by status array
        status = [TradeStatus.from_label(s.strip()) for s in status.split(',')]
        trades = trades.filter(trade_status__in=status)

        # pass market BID as context
        try:
            market_bid = float(market_bid)
        except:
            pass

        context = {'market_bid' : market_bid}

        #serializer = TransactionSerializer(trades, many=True)
        serializer = PositioningSerializer(trades, context=context)
        
        return JsonResponse(serializer.data, safe=False)



"""
    Bond operations
"""

# act on all transactions
@csrf_exempt
def bond_list(request, number):

    # List 5 most frequent bonds
    if request.method == 'GET':
        bonds = Transaction.objects.                   \
                    values('bond').                     \
                    annotate(dcount=Count('bond')).     \
                    order_by('-dcount')[:number].       \
                    values_list('bond__name', flat=True)

        return JsonResponse(list(bonds), safe=False)

# list all bonds
def bond_list_all(request):

    # List 5 most frequent bonds
    if request.method == 'GET':
        bonds = Bond.objects.values_list('name', flat=True)

        return JsonResponse(list(bonds), safe=False)

# list all brokers
def broker_list_all(request):

    # List 5 most frequent bonds
    if request.method == 'GET':
        brokers = Broker.objects.values_list('name', flat=True)

        return JsonResponse(list(brokers), safe=False)

# list all currencies
def currency_list_all(request):
    if request.method == 'GET':
        curr = Currency.objects.values_list('name', flat=True)
        return JsonResponse(list(curr), safe=False)

"""
   Blot upload and add transactions
"""

import pandas
from datetime import datetime
from datetime import timedelta


class BlotUploadView(views.APIView):
    #parser_classes = [parsers.FileUploadParser]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        #file_obj = request.data['file']

        #serializer = self.serializer_class(data=request.data)
        #if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
        #    serializer.save()

        file_data = request.data['file']
        file_name = file_data.name
        print("BLOT name: ", file_name)

        # open blot in pandas dataframe
        df = None

        if file_name.endswith('.xlsx'):
            df = pandas.read_excel(file_data, skiprows=2, engine='openpyxl')
        elif file_name.endswith('.xls'):
            df = pandas.read_excel(file_data, skiprows=2, engine='xlrd')
        elif file_name.endswith('.csv'):
            df = pandas.read_csv(file_data, skiprows=2)

        if df is None:
            return JsonResponse({'message' : "File extension is not '.xlsx', or '.xls' or '.csv'"}, status=400, safe=False)


        # remap column names to match Transaction model
        remap = {
                'Status' : 'trade_status',
                'Side' : 'trade_side',
                'Price' : 'market_price',
                'UserName' : 'user',
                'Trade Dt' : 'trade_date',
                'Qty (M)' : 'quantity',
                'Dlr Alias' : 'broker',
                'Curncy' : 'currency',
                'ISIN' : 'bond'
            }

        # column check: if missing raise error
        if not set(remap.keys()).issubset(set(df.columns)):
            diff = list(set(remap.keys()).difference(set(df.columns)))
            return JsonResponse({'message' : "BLOT miss same required columns: " + str(diff)}, status=400, safe=False)

        # update remap with non-mandatory fields
        remap['DNotes'] = 'comments'
        remap['Exec Time'] = 'trade_time'
        remap['SetDt'] = 'settlement_date'
        remap['Security'] = 'security'
            
        # rename columns
        df.rename(columns=remap, inplace=True)

        # change Status format
        df.trade_status.loc[df.trade_status == 'Accepted'] = 'confirmed'
        df.trade_status.loc[df.trade_status == 'Cancelled'] = 'cancelled'

        # change Side format
        df.trade_side.loc[df.trade_side == 'S'] = 'sell'
        df.trade_side.loc[df.trade_side == 'B'] = 'buy'
        df.trade_side.loc[df.trade_side == '[S]'] = 'sell'
        df.trade_side.loc[df.trade_side == '[B]'] = 'buy'
        
        # keep only useful columns
        cols = list(set(remap.values()).intersection(set(df.columns)))
        df = df[cols]

        # convert trade and settlement date
        df.trade_date = df.trade_date.dt.date
        df.trade_time = df.trade_time
        df.settlement_date = df.settlement_date.dt.date
        df['settlement_time'] = df.trade_time.copy()

        # Nan comments to ""
        df.comments.fillna('', inplace=True)

        print("Dataframe before loading:")
        print(df)

        # TODO: manage yield, principal, ISIN, Security, Currency, Dlr Alias

        serializer = TransactionSerializer(data=df.to_dict('records'), many=True)
        if serializer.is_valid():

            # save serialized data
            serializer.save()

            # notify users of refresh
            send_event('transactions', 'message', {'request' : 'POST', 'source' : request.META['HTTP_USER_AGENT'], 'data' : df.to_dict('records')})

            return JsonResponse(data=df.to_dict('records'), status=201, safe=False)
        
        # Error in serialization
        return JsonResponse({'message' : 'Invalid serialization' + str(serializer.errors)}, status=400)

