from random import random
from faker import Faker
from requests import request
import requests
fake = Faker()

my_real_phone = fake.phone_number()
print(my_real_phone)
my_real_address = fake.building_number() + ' ' + fake.street_name() + ' ' + fake.street_suffix()
print(my_real_address)
if(random() > 0.7):
    my_real_2nd_address = fake.secondary_address()
else:
    my_real_2nd_address = ""
print(my_real_2nd_address)
my_real_city = fake.city()
print(my_real_city)
my_real_state = fake.state_abbr()
print(my_real_state)
my_real_zip = fake.postalcode_in_state(my_real_state)
print(my_real_zip)

my_real_name = fake.name()
print(my_real_name)

my_real_creditcard = fake.credit_card_number()
print(my_real_creditcard)
my_real_expiration = fake.credit_card_expire()
print(my_real_expiration)
my_real_cv2 = fake.credit_card_security_code()
print(my_real_cv2)
req = requests.request()