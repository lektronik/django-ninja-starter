from ninja import Schema, ModelSchema
from decimal import Decimal
from typing import List, Optional
from features.models import Product

class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image']

class CartItemSchema(Schema):
    product_id: int
    quantity: int

class CartOutSchema(Schema):
    items: List[dict]
    total: Decimal
