from rest_framework import serializers
from transactions.models import Bond, Broker, Transaction, TradeStatus, TradeSide, Currency
from django.core.exceptions import ValidationError
from datetime import datetime
import codes
import re

class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = [
            'name',
            'market_bid'
            ]

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = [
            'name',
            ]

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'name',
            ]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'trade_status', 
            'trade_side', 
            'bond',
            'broker',
            'user',
            'currency',
            'market_price',
            'quantity',
            'security',
            'comments',
            'trade_datetime',
            'settlement_datetime',
            'modif_datetime'
        ]

    # from inside database to outside
    def to_representation(self, instance):
        repres = super().to_representation(instance)
        
        # convert Id for AG-Grid sake (goddamn)
        #repres["trade_id"] = instance.id

        # Interface object labels instead of values (lowercase)
        repres["trade_status"] = TradeStatus._value2member_map_[instance.trade_status].label
        repres["trade_side"] = TradeSide._value2member_map_[instance.trade_side].label

        # Interface names instead of ids
        repres["bond"] = "null" if instance.bond is None else instance.bond.name
        repres["broker"] = "null" if instance.broker is None else instance.broker.name
        #repres["user"] = instance.user.username
        repres["currency"] = "null" if instance.currency is None else instance.currency.name

        if instance.trade_datetime is not None:
            repres["trade_date"] = instance.trade_datetime.date()
            repres["trade_time"] = instance.trade_datetime.time()
        else:
            repres["trade_date"] = None
            repres["trade_time"] = None


        repres["modif_date"] = instance.modif_datetime.date()
        repres["modif_time"] = instance.modif_datetime.time()
        
        if instance.settlement_datetime is not None:
            repres["settlement_date"] = instance.settlement_datetime.date()
            repres["settlement_time"] = instance.settlement_datetime.time()
        else:
            repres["settlement_date"] = None
            repres["settlement_time"] = None
        
        # delete useless fields
        #del repres["id"]
        del repres["trade_datetime"]
        del repres["modif_datetime"]
        del repres["settlement_datetime"]

        return repres

    # from outside post or put to inside data
    def to_internal_value(self, data):

        # transform id
        #if "trade_id" in data:
        #    data['id'] = data['trade_id']
        #    del data['trade_id']

        # transform labels into fields
        if "trade_status" in data:
            data['trade_status'] = TradeStatus.from_label(data['trade_status'])
        if "trade_side" in data:
            data['trade_side'] = TradeSide.from_label(data['trade_side'])

        # look for bond by name, otherwise create it
        if "bond" in data:
            try:
                bond = Bond.objects.get(name=data['bond'])
                data['bond'] = bond.id
            except Bond.DoesNotExist:
                data['bond'] = Bond.objects.create(name=data['bond']).id

        # look for broker, otherwise create it
        if "broker" in data:
            try:
                broker = Broker.objects.get(name=data['broker'])
                data['broker'] = broker.id
            except Broker.DoesNotExist:
                data['broker'] = Broker.objects.create(name=data['broker']).id

        if "currency" in data:
            try:
                currency = Currency.objects.get(name=data['currency'])
                data['currency'] = currency.id
            except Currency.DoesNotExist:
                data['currency'] = Currency.objects.create(name=data['currency']).id

        # look for user, otherwise raise validation error
        #try:
        #    user = User.objects.get(username=data['user'])
        #    data['user'] = user.id
        #except User.DoesNotExist:
        #    raise ValidationError("Could not create Transaction: User name %s doesn't exist." % data['user'])
      
        # set trade_date
        if "trade_date" in data and "trade_time" in data:

            # convert date from string
            if isinstance(data["trade_date"], str):
                data["trade_date"] = datetime.strptime(data["trade_date"], '%Y-%m-%d').date()

            # convert time from string
            if isinstance(data["trade_time"], str):
                data["trade_time"] = datetime.strptime(data["trade_time"], '%H:%M:%S').time()


            data["trade_datetime"] = datetime.combine(data["trade_date"], data["trade_time"])
            del data["trade_date"]
            del data["trade_time"]

        # set settlement_date
        if "settlement_date" in data and "settlement_time" in data:

            # convert date from string
            if isinstance(data["settlement_date"], str):
                data["settlement_date"] = datetime.strptime(data["settlement_date"], '%Y-%m-%d').date()

            # convert time from string
            if isinstance(data["settlement_time"], str):
                data["settlement_time"] = datetime.strptime(data["settlement_time"], '%H:%M:%S').time()


            data["settlement_datetime"] = datetime.combine(data["settlement_date"], data["settlement_time"])
            del data["settlement_date"]
            del data["settlement_time"]
       

        # convert market price's format

        # format example "100-09"
        pattern_0 = re.compile(r"(?P<a>\d+)-(?P<d>\d+)")
        price_0 = lambda a, d: a + d / 32.0

        # format example "100-09 5/8"
        pattern_1 = re.compile(r"(?P<a>\d+)-(?P<d>\d+)\W(?P<f1>\d+)/(?P<f2>\d+)")
        price_1 = lambda a, d, f1, f2: a + (d + float(f1)/f2) / 32.0

        # format example "100-09+"
        pattern_2 = re.compile(r"(?P<a>\d+)-(?P<d>\d+)\+")
        price_2 = lambda a, d: a + (d + 0.5) / 32.0

        if "market_price" in data and isinstance(data["market_price"], str):
            # check pattern 0
            if pattern_0.match(data["market_price"]) is not None:
                args = pattern_0.findall(data["market_price"])[0]
                args = [int(arg) for arg in args]
                data["market_price"] = price_0(*args)

            # check pattern 1
            elif pattern_1.match(data["market_price"]) is not None:
                args = pattern_1.findall(data["market_price"])[0]
                args = [int(arg) for arg in args]
                data["market_price"] = price_1(*args)

            # check pattern 2
            elif pattern_2.match(data["market_price"]) is not None:
                args = pattern_2.findall(data["market_price"])[0]
                args = [int(arg) for arg in args]
                data["market_price"] = price_2(*args)

            # else it's a number
                
        
        return super().to_internal_value(data)


"""
    Positioning specific serializers
"""

import pandas as pd


# Put results of scripts into a structured form
# rows: <list of rows>
# agg: {'buy' : <dict of agg buy>, 'sell' : <dict of agg sell>}
class PositioningSerializer(serializers.Serializer):
    
    # manually serialize, too complex
    def to_representation(self, instance):
        repres = super().to_representation(instance)
        
        # pre-apply the serializer
        table = TransactionSerializer(instance, many=True)

        # init environment, initialize aggregates as the context
        df = pd.DataFrame(table.data)
        agg = dict(self.context)

        print("Initialization: ", agg)

        # collect scripts
        query = codes.models.Script.objects.order_by('exec_priority')

        # execute all codes and collect results SEQUENTIALLY
        # pass the already computed values to the dict
        for script in query:
            result = None

            # manage empty case
            if len(df) > 0:
                try:
                    result = script.execute({'df' : df, **agg})
                except Exception as e:
                    print("An error occured while computing script: ", script.name)
                    result = str(e)

            if script.script_type == codes.models.ScriptType.COL:
                # add to columns of df
                df[script.name] = result

            elif script.script_type == codes.models.ScriptType.AGG:
                # add to aggregates
                agg[script.name] = result


        # set environment as outputs
        repres['rows'] = df.to_dict('records')
        repres['agg'] = agg

        return repres

