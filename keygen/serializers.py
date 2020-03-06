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
        fields = ('account', 'hash_key', 'created')
        read_only_fields = ['hash_key']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        key_gen = KeyGenerator(account_data.get('email'))
        if key_gen:
            generated_key = key_gen.generate()
            account = Account.objects.get(email=account_data.get('email'))
            if not account:
                account = Account.objects.create(**account_data)
            key = Key.objects.create(account=account, hash_key=generated_key, **validated_data)
            return key
        return False