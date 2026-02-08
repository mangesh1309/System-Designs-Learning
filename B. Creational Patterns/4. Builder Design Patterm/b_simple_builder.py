class User:
    def __init__(self):
        # required params
        self.name = None
        self.age = None
        self.city = None

class UserBuilder:
    def __init__(self):
        self.user = User()
    
    def set_name(self, name):
        self.user.name = name
        return self

    def set_age(self, age):
        self.user.age = age
        return self

    def set_city(self, city):
        self.user.city = city
        return self


    def set_profession(self, profession):
        self.user.profession = profession
        return self # Allows method chaining

    def set_income(self, income):
        self.user.income = income
        return self
    
    def build(self):
        return self.user

user = (
    UserBuilder()
    .set_name("Mangesh")
    .set_age(34)
    .set_city("Noida")
    .set_profession("Teacher")
    .set_income(15000)
    .build()
)

print(user.name, user.age, user.city, user.profession, user.income)