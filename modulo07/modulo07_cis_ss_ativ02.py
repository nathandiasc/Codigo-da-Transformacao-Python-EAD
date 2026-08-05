from faker import Faker

fake = Faker('pt_BR')

print("--- Perfis Fictícios Gerados ---")
for _ in range(3):
    print(f"Nome: {fake.name()}")
    print(f"E-mail: {fake.email()}")
    print(f"Cidade: {fake.city()}\n")