from faker import Faker
fake = Faker()
# pip install Faker
def user_details():
    return {'name': fake.name(),'address': fake.address()}

if __name__ == "__main__":
    print(user_details())
