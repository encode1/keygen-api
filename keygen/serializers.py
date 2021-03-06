from rest_framework import serializers
from .models import Key, Account
from .generator import KeyGenerator


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email',)


class KeySerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False, required=True)

    class Meta:
        model = Key
        fields = ('id', 'account', 'hash_key', 'created')
        read_only_fields = ['id', 'hash_key']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        key_gen = KeyGenerator(account_data.get('email'))
        if key_gen:
            generated_key = key_gen.generate()
            account = Account.objects.get_or_create(email=account_data.get('email'))
            if account[1]:
                key = Key.objects.create(account=account[0], hash_key=generated_key, **validated_data)
            else:
                key = Key.objects.get(account=account[0])
            return key
        return False