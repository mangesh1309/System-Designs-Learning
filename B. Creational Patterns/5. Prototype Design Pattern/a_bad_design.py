# Consider an email notification system where each email instance requires extensive setup—loading templates, configurations, user settings, and formatting. Creating every email from scratch introduces redundancy and inefficiency.

# Now imagine having a pre-configured prototype email, and simply cloning it for each user while modifying a few fields (like the name or content). That would save time, reduce errors, and simplify the logic.

from abc import ABC, abstractmethod

class EmailTemplate(ABC):
    @abstractmethod
    def set_content(self, content):
        pass

    @abstractmethod
    def send_mail(self, to):
        pass


class WelcomeEmail(EmailTemplate):
    def __init__(self):
        self.subject = "Welcome to XYZ Firm"
        self.content = "Hello there! Thanks for signing up!" # default content

    def set_content(self, content):
        self.content = content

    def send_mail(self, to):
        print(f"Sending mail to {to}\nContent: {self.content}\n\n")


email1 = WelcomeEmail()
email1.send_mail("user1@gmail.com")

# similar mail with different content
email2 = WelcomeEmail()
email2.set_content("This is slightly a different content")
email2.send_mail("user2@gmail.com")

# yet another variation
email3 = WelcomeEmail()
email3.set_content("This is a very different variation in content")
email3.send_mail("user3@gmail.com")