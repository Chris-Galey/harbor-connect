from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    SupplierSerializer,
    SalesOrderSerializer,
    SalesOrderItemSerializer,
    PurchaseOrderSerializer,
    PurchaseOrderItemSerializer,
)
from .models import (
    Category,
    Product,
    Supplier,
    SalesOrder,
    SalesOrderItem,
    PurchaseOrder,
    PurchaseOrderItem,
)
