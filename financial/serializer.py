from rest_framework import serializers

from financial.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('name', 'description', 'acc_type', 'balance')
