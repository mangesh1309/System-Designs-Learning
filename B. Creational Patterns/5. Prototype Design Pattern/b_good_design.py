from abc import ABC, abstractmethod
import copy

# Prototype interface
class EmailTemplateInterface(ABC):
    @abstractmethod
    def clone(self):
        pass

# Base Email Template
class EmailTemplate(EmailTemplateInterface):
    def __init__(self, subject, content):
        self.subject = subject
        self.content = content

    def clone(self):
        return copy.deepcopy(self)

    def set_content(self, content):
        self.content = content
    
    def send_mail(self, to):
        print(f"Sending mail to {to}\nSubject: {self.subject}\nContent: {self.content}\n\n")

# Concrete Email Templates
class WelcomeEmail(EmailTemplate):
    def __init__(self):
        super().__init__(
            subject="Welcome to XYZ Firm",
            content="Hello there! Thanks for signing up!"
        )


class PasswordResetEmail(EmailTemplate):
    def __init__(self):
        super().__init__(
            subject="Password Reset Request",
            content="Click the link below to reset your password: [reset_link]"
        )


# Prototype Registry
class EmailTemplateRegistry:
    _prototypes = {}

    @classmethod
    def register_prototype(cls, name, prototype):
        cls._prototypes[name] = prototype
    
    @classmethod
    def unregister_prototype(cls, name):
        cls._prototypes.pop(name, None)
    
    @classmethod
    def get_prototype(cls, name):
        if name not in cls._prototypes:
            raise ValueError(f"Prototype with name {name} not registered")

        return cls._prototypes.get(name)

# Client code
# Register prototypes
EmailTemplateRegistry.register_prototype("welcome", WelcomeEmail())
EmailTemplateRegistry.register_prototype("password_reset", PasswordResetEmail())

email1 = EmailTemplateRegistry.get_prototype("welcome")
email1.send_mail("user1@gmail.com")

email2 = EmailTemplateRegistry.get_prototype("welcome")
email2.set_content("Hi John! Welcome to our platform.")
email2.send_mail("user2@gmail.com")

email3 = EmailTemplateRegistry.get_prototype("password_reset")
email3.send_mail("user3@gmail.com")

