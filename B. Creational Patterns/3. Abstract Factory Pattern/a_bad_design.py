# Imagine you're building a cross-platform desktop application that must support both Windows and macOS.

# To provide a good user experience, your application should render native-looking UI components for each operating system like:

# Buttons
# Checkboxes

# Windows UI Elements
class WindowsButton:
    def paint(self):
        print("painting with Windows Button")
    
    def on_click(self):
        print("on click with Windows Button")

class WindowsCheckbox:
    def paint(self):
        print("painting with Windows Checkbox")
    
    def on_click(self):
        print("on click with Windows Checkbox")

# MacOS UI Elements
class MacOSButton:
    def paint(self):
        print("painting with MacOS Button")
    
    def on_click(self):
        print("on click with MacOS Button")

class MacOSCheckbox:
    def paint(self):
        print("painting with MacOS Checkbox")
    
    def on_click(self):
        print("on click with MacOS Checkbox")

# Application Logic
import platform

class Application:
    @staticmethod
    def main():
        os = platform.system()

        if "windows" in os.lower():
            button = WindowsButton()
            checkbox = WindowsCheckbox()
            button.paint()
            checkbox.paint()
        elif "darwin" in os.lower(): # macOS
            button = MacOSButton()
            checkbox = MacOSCheckbox()
            button.paint()
            checkbox.paint()
        else:
            raise Exception("Unsupported operating system")

try:
    Application.main()
except Exception as e:
    print(e)

# Why a bad design?
# 1. It violates the Open/Closed Principle.
# 2. There is tight coupling between the application logic and the operating system.
# 3. No abstraction and polymorphism.
# 4. Scalability is poor (to add components and os).