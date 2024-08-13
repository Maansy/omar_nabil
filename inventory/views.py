from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, MechanicalPartSerializer, RawMaterialSerializer, ElectricalPartSerializer
from .models import MechanicalPart, RawMaterial, ElectricalPart
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        if user and user.check_password(request.data['password']):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=400)

class MechanicalPartListCreateView(generics.ListCreateAPIView):
    queryset = MechanicalPart.objects.all()
    serializer_class = MechanicalPartSerializer
    permission_classes = [permissions.IsAuthenticated]

class MechanicalPartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MechanicalPart.objects.all()
    serializer_class = MechanicalPartSerializer
    permission_classes = [permissions.IsAuthenticated]

class RawMaterialListCreateView(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class RawMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class ElectricalPartListCreateView(generics.ListCreateAPIView):
    queryset = ElectricalPart.objects.all()
    serializer_class = ElectricalPartSerializer
    permission_classes = [permissions.IsAuthenticated]

class ElectricalPartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricalPart.objects.all()
    serializer_class = ElectricalPartSerializer
    permission_classes = [permissions.IsAuthenticated]

class AllInventoryItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        mechanical_parts = MechanicalPartSerializer(MechanicalPart.objects.all(), many=True).data
        raw_materials = RawMaterialSerializer(RawMaterial.objects.all(), many=True).data
        electrical_parts = ElectricalPartSerializer(ElectricalPart.objects.all(), many=True).data

        all_items = {
            'mechanical_parts': mechanical_parts,
            'raw_materials': raw_materials,
            'electrical_parts': electrical_parts
        }

        return Response(all_items)