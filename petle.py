# wynik = 0
#
# for i in range(0,4):
#     x = int(input("podaj liczbe: "))
#     wynik += x
#     print(i)
#
# print("wynik dodawania liczb to: ",wynik)


from faker import Faker

fake = Faker(['pl_PL'])
firstname = fake.first_name()
lastname = fake.last_name()
phoneNo = fake.phone_number()
email = fake.email()
street = fake.street_name()
buildingNo = fake.building_number()
postcode = fake.postcode()
cityname = fake.city()
password = fake.password()
password_check = fake.password()

print(password)
print(password_check)