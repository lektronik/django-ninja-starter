from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth

api = NinjaExtraAPI(
    title="NinjaStart Boilerplate",
    version="1.0.0",
    description="Production-ready Django Ninja Boilerplate",
)

# Auth Controller (Login, Refresh)
api.register_controllers(NinjaJWTDefaultController)

from features.auth.api import router as auth_router
from features.api import products_router, cart_router

# Registers routers from feature modules
api.add_router("/auth", auth_router)
api.add_router("/products", products_router)
api.add_router("/cart", cart_router)


@api.get("/health")
def health(request):
    return {"status": "ok"}
