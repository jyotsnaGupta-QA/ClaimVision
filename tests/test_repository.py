from database.models import Customer
from database.repository import ClaimRepository

repo = ClaimRepository()

customer = Customer(
    FullName="Jyotsna Gupta",
    Email="jyotsna@test.com",
    PhoneNumber="9999999999"
)

saved_customer = repo.create_customer(customer)

print(saved_customer.CustomerId)

repo.close()