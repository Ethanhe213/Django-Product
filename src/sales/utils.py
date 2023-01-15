import uuid
from customers.models import Customer
from profiles.models import Profile
def generate_code():
    return str(uuid.uuid4()).replace('-','')[:12]

def get_customer_from_id(val):
    return Customer.objects.get(id=val)

def get_salesman_from_id(val):
    return Profile.objects.get(id=val)