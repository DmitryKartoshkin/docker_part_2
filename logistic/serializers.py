from rest_framework import serializers
from logistic.models import Product, Stock,  StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['quantity', 'price', 'product']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        list_ = []
        for position in positions:
            stocks_product = StockProduct(stock=stock, **position)
            list_.append(stocks_product)
        StockProduct.objects.bulk_create(list_)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for el in positions:
            product = el.pop('product')
            StockProduct.objects.update_or_create(stock=stock,
                                                  product=product,
                                                  defaults=
                                                  {'quantity': el['quantity'],
                                                   'price': el['price']
                                                   }
                                                  )
        return stock



