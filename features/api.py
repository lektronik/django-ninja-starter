from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from features import models, schemas
from app.auth import NinjaJWTAuth

# ── Product Router ──
products_router = Router(tags=["Products"])

@products_router.get("/", response=List[schemas.ProductSchema])
def list_products(request):
    return models.Product.objects.all()

@products_router.get("/{id}", response=schemas.ProductSchema)
def get_product(request, id: int):
    return get_object_or_404(models.Product, id=id)

# ── Cart Router ──
cart_router = Router(tags=["Cart"], auth=NinjaJWTAuth())

@cart_router.get("/", response=schemas.CartOutSchema)
def get_cart(request):
    cart, _ = models.Cart.objects.get_or_create(user=request.user)
    items = []
    total = 0
    for item in cart.items.select_related('product').all():
        line_total = item.product.price * item.quantity
        total += line_total
        items.append({
            "product": item.product.name,
            "quantity": item.quantity,
            "price": item.product.price,
            "line_total": line_total
        })
    return {"items": items, "total": total}

@cart_router.post("/add")
def add_to_cart(request, payload: schemas.CartItemSchema):
    cart, _ = models.Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(models.Product, id=payload.product_id)
    
    item, created = models.CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += payload.quantity
    else:
        item.quantity = payload.quantity
    item.save()
    
    return {"success": True, "message": f"Added {product.name} to cart"}
