from database.models import Customer

customer = Customer(
    FullName="Jyotsna Gupta",
    Email="jyotsna.gupta@xebia.com",
    PhoneNumber="9619361287"
)

print(customer.FullName)
print(customer.Email)