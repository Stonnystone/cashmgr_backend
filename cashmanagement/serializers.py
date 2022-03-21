from rest_framework import serializers
from .models import Account, Inflow, Category, Balance, Outflow, Split, Transaction, RecurringTransaction


    # - Create model Account
    # - Create model Balance
    # - Create model Category
    # - Create model Inflow
    # - Create model Outflow
    # - Create model RecurringTransaction
    # - Create model Transaction
    # - Create model Split

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # fields = ('name', 'account_type', 'active', 'iban')
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = ('amount', 'date', 'type')
        
class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = '__all__'

class RecurringTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringTransaction
        fields = '__all__'
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = '__all__'


