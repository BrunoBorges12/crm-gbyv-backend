from ninja import Schema
from typing import Optional

class AddressSchema(Schema):
    state: str
    city:str
    street:str
class CustomerSchema(Schema):
    company: str
    vatNumber: str
    companyPhone: str
    website: Optional[str] = None  # Campo opcional
    address:AddressSchema
