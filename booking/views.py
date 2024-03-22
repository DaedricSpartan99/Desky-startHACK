from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from .models import Workplace, City, Coworking, Farm
from .serializers import WorkplaceSerializer, FarmSerializer, CitySerializer, CoworkingSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def get_queryset(request):
        
        if request.method == 'GET':

            search = request.GET.get('keyword', None)

            if search is None:
                return JsonResponse({'message' : 'No keyword'}, status=400)

            # Get farm list
            queryset = Farm.objects.filter(
                Q(title__icontains=search) | 
                Q(city__name__icontains=search)
            )

            farms = FarmSerializer(queryset, many=True)

            #if not farms.is_valid():
            #    print(farms.errors)
            #    return JsonResponse({'message' : 'Error serializing farms', 'errors' : str(farms.errors) }, status=400)
            
            # Get coworking list
            queryset = Coworking.objects.filter(
                Q(title__icontains=search) | 
                Q(description__icontains=search)
            )

            coworking = CoworkingSerializer(queryset, many=True)

            #if not coworking.is_valid():
            #    print(farms.errors)
            #    return JsonResponse({'message' : 'Error serializing farms', 'errors' : str(coworking.errors)}, status=400)
            
            # merge results
            return JsonResponse(farms.data + coworking.data, safe=False)

        else:
            if search is None:
                return JsonResponse({'message' : 'Bad request'}, status=400)
        

class WorkplaceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WorkplaceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned workplaces to a given user,
        by filtering against a `search` query parameter in the URL.
        """
        queryset = Workplace.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(description__icontains=search) | 
                Q(address__icontains=search)
            )
        return queryset

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class WorkplaceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


