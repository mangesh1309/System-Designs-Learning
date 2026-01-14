# Bad design:
# 1. too make constructor parameters (required and optional)
# 2. to many constructors

class User:
    def __init__(self, name, age, city, phone, email, is_active, is_admin):
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone
        self.email = email
        self.is_active = is_active
        self.is_admin = is_admin


user = User("Mangesh", 22, "Pune", None, None, True, False)

# In java, we dont have direct optional paramters allowance like in Python.
# For that we need to code constructor for each combination of parameters.