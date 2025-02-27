from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("/square/", "square.api.router")
api.add_router("/shopify/", "shopify.api.router")