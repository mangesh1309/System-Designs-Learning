# The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.
# In our case, we want to create a family of UI components that look and behave differently based on the operating system but expose the same interface.

# Abstract product interfaces
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


# Concrete product classes
class WindowsButton(Button):
    def paint(self):
        print("painting with Windows Button")

    def on_click(self):
        print("on click with Windows Button")


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("painting with Windows Checkbox")
    
    def on_click(self):
        print("on click with Windows Checkbox")


class MacOSButton(Button):
    def paint(self):
        print("painting with MacOS Button")
    
    def on_click(self):
        print("on click with MacOS Button")

class MacOSCheckbox(Checkbox):
    def paint(self):
        print("painting with MacOS Checkbox")
    
    def on_click(self):
        print("on click with MacOS Checkbox")


# Abstract factory interface
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete factory classes
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Client code: The client code uses the factory to create UI components. It doesn't care which OS it is dealing with.
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        self.button.paint()
        self.checkbox.paint()

# Application entry point
import platform
class ApplicationEntryPoint:
    @staticmethod
    def main():
        os = platform.system()

        factory = None
        if "windows" in os.lower():
            factory = WindowsFactory()
        elif "darwin" in os.lower():
            factory = MacOSFactory()
        else:
            raise Exception("Unsupported operating system")
        
        if factory is not None:
            application = Application(factory)
            application.render_ui()
        else:
            raise Exception("Factory is not initialized")

if __name__ == "__main__":
    ApplicationEntryPoint.main()