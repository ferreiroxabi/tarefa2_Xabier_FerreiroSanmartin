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

# Bucle para imprimir por pantalla os datos dos alumnos formateados para maior lexibilidade 
for codigo, datos in usuarios.items():
    print(f"Usuario {codigo}")
    print(f"Nome: {datos['nome']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Correo: {datos['correo']}")
    print(f"Teléfono: {datos['telefono']}\n")

usuarioRandom = random.choice(list(usuarios.values()))
print("O usuario chamado", usuarioRandom['nome'], "foi o afortunado")