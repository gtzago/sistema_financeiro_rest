from rest_framework import serializers

from financial.models import FinancialAccount, Transaction


class FinancialAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinancialAccount
        fields = ('name', 'description', 'acc_type', 'balance')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('date', 'description', 'acc_from', 'acc_to', 'value')
