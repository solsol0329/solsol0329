from rest_framework import serializers
from .models import DepositProduct, DepositOptions


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = "__all__"

# 멤버 오버라이딩할 때는 인자로 read_only=True
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = "__all__"
        read_only_fields = ("product", )

