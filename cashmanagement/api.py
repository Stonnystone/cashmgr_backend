from cashmanagement.models import Account, Balance, Category, Outflow
from cashmanagement.models import Inflow, Split, Transaction, RecurringTransaction
# from cashmanagement.models import SplitQuerySet, AccountQuerySet, TransactionQuerySet, RecurringTransactionManager

from rest_framework import viewsets, permissions

from .serializers import AccountSerializer, InflowSerializer, CategorySerializer, BalanceSerializer
from .serializers import  OutflowSerializer, SplitSerializer, TransactionSerializer, RecurringTransactionSerializer

# Account Viewset
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AccountSerializer
    
class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BalanceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer
    
class InflowViewSet(viewsets.ModelViewSet):
    queryset = Inflow.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InflowSerializer
    
class OutflowViewSet(viewsets.ModelViewSet):
    queryset = Outflow.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OutflowSerializer
    
class SplitViewSet(viewsets.ModelViewSet):
    queryset = Split.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SplitSerializer
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TransactionSerializer
    
class RecurringTransactionViewSet(viewsets.ModelViewSet):
    queryset = RecurringTransaction.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecurringTransactionSerializer