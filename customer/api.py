from ninja import NinjaAPI
from crm.security import GlobalAuth
from .schemas import CustomerSchema
from .models import Customer
api = NinjaAPI(urls_namespace="customer",auth=GlobalAuth())


@api.post('/create')
def create_customer(request,payload:CustomerSchema):
    print(payload)
    # ** Oque precisa **
    #  validar erro
    #  retorna o comum  de dados igual auth
    customer = Customer.objects.create(
        company=payload.company,
        cpf=payload.vatNumber,
        tel=payload.companyPhone,
        website=payload.website,
        city=payload.address.city,
        state=payload.address.state,
        country=payload.address.street,
    )
    return {"success": True, "customer_id": customer.id}    