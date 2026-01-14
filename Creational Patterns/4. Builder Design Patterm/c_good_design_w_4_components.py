# Four Components:
# 1. Product - the class to be built
# 2. Abstract Builder - What steps are required to build the product
# 3. Concrete Builder - Implements how the object is built
# 4. Director - Controls the order and combination of building steps



# 1. Product - the class to be built
class User:
    def __init__(self):
        self.name = None
        self.age = None
        self.city = None

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, city={self.city})"


# 2. Abstract Builder - What steps are required to build the product
from abc import ABC, abstractmethod

class UserBuilder(ABC):

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def set_city(self, city):
        pass

    @abstractmethod
    def build(self):
        pass

# 3. Concrete Builder - Implements how the object is built
class ConcreteUserBuilder(UserBuilder):
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

    def build(self):
        return self.user

# 4. Director - Controls the order and combination of building steps
class UserDirector:
    def __init__(self, builder: UserBuilder):
        self.builder = builder

    def build_basic_user(self):
        return (
            self.builder
            .set_name("Mangesh")
            .set_age(22)
            .build()
        )

    def build_full_user(self):
        return (
            self.builder
            .set_name("Mangesh")
            .set_age(22)
            .set_city("Pune")
            .build()
        )


# Client code
builder = ConcreteUserBuilder()
director = UserDirector(builder)

basic_user = director.build_basic_user()
print(basic_user)

full_user = director.build_full_user()
print(f"Full User: {full_user}")
