from src.payloads.schemas.master import CustomerSchema
from src.entities.master import CustomerEntity 

from src.configs.database import get_db
from src.utils import AddPagination
from sqlalchemy import select

def post_simple_customer(req:CustomerSchema.MtrCustomerSimpleSchema):
    db = get_db()
    try:
        _new_data = CustomerEntity.MtrCustomer()
    except Exception as err:
        return None, err
