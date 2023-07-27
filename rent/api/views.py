from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from ..models import UAV, RentalRecord
from . serializers import UAVSerializer, RentalRecordSerializer
class UAVListView(generics.ListCreateAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class UAVDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RentalRecordListView(generics.ListCreateAPIView):
    queryset = RentalRecord.objects.all()
    serializer_class = RentalRecordSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RentalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentalRecord.objects.all()
    serializer_class = RentalRecordSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
