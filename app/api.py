from ninja import NinjaAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth

api = NinjaAPI(
    title="NinjaStart Boilerplate",
    version="1.0.0",
    description="Production-ready Django Ninja Boilerplate",
)

# Auth Controller (Login, Refresh)
api.register_controllers(NinjaJWTDefaultController)

# Registers routers from feature modules
api.add_router("/auth", "features.auth.api.router")
api.add_router("/products", "features.api.products_router")

api.add_router("/cart", "features.api.cart_router")


@api.get("/health")
def health(request):
    return {"status": "ok"}
