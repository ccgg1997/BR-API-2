from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .repository.customer_repository import CustomerRepository
from .serializer import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        return [IsAuthenticated()]

    @extend_schema(
        summary="Create new customer",
        responses={
            200: CustomerSerializer(many=True),
        },
    )
    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            CustomerRepository.create_customer(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
