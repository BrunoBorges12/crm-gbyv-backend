from ninja import NinjaAPI
from crm.security import GlobalAuth


api = NinjaAPI(auth=GlobalAuth())


@api.post('/create')
def create_customer(request):
    return {"success": "Customer created"}