

from django.contrib.auth.models import User
from rest_framework import serializers

from financial.models import FinancialAccount, Transaction


class FinancialAccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FinancialAccount
        fields = ('name', 'description', 'acc_type', 'balance', 'owner')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('date', 'description', 'acc_from', 'acc_to', 'value')


class UserSerializer(serializers.ModelSerializer):
    financial_accounts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=FinancialAccount.objects.all())
    transactions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=FinancialAccount.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'transactions', 'financial_accounts')
