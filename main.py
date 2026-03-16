from faker import Faker
import random

fake = Faker('es_ES')

usuarios = {
    i: {
        "nome": fake.name(),
        "direccion": fake.address(),
        "correo": fake.email(),
        "telefono": fake.phone_number()
    }
    for i in range(1,16)
}

for i in usuarios:
    print(usuarios(i))

