from database.models import Customer, Vehicle, Claim

customer = Customer(
    FullName="Jyotsna Gupta",
    Email="jyotsna@test.com",
    PhoneNumber="9999999999"
)

print(customer.FullName)

vehicle = Vehicle(
    VehicleBrand="Hyundai",
    VehicleModel="i20"
)

print(vehicle.VehicleBrand)

claim = Claim(
    Status="Pending"
)

print(claim.Status)