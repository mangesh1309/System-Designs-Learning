from abc import ABC, abstractmethod

# 1. Define the component interface
# This interface will be used by both the base component and all decorators. 
class TextView(ABC):
    @abstractmethod
    def render(self):
        pass

# 2. Implement the concrete component
# This is the base class that renders plain text
class PlainTextView(TextView):
    def __init__(self, text):
        self.text = text

    def render(self):
        print(self.text, end = "")

# 3. Create the abstract decorator
# This class also implements TextView and holds a reference to another TextView component.
class TextDecorator(TextView):
    def __init__(self, inner):
        self.inner = inner

# 4. Implement conrete decorators
# Each decorator adds a specific formatting layer before or after calling the wrapped component's render() method.
class BoldDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)
    
    def render(self):
        print("<b>", end="")
        self.inner.render()
        print("</b>", end="")

class ItalicDecorator(TextDecorator):
   def __init__(self, inner):
       super().__init__(inner)

   def render(self):
       print("<i>", end="")
       self.inner.render()
       print("</i>", end="")

class UnderlineDecorator(TextDecorator):
   def __init__(self, inner):
       super().__init__(inner)

   def render(self):
       print("<u>", end="")
       self.inner.render()
       print("</u>", end="")


# 5. client code
class TextRendererApp:
   @staticmethod
   def main():
       text = PlainTextView("Hello, World!")

       print("Plain: ", end="")
       text.render()
       print()

       print("Bold: ", end="")
       bold_text = BoldDecorator(text)
       bold_text.render()
       print()

       print("Italic + Underline: ", end="")
       italic_underline = UnderlineDecorator(ItalicDecorator(text))
       italic_underline.render()
       print()

       print("Bold + Italic + Underline: ", end="")
       all_styles = UnderlineDecorator(ItalicDecorator(BoldDecorator(text)))
       all_styles.render()
       print()

if __name__ == "__main__":
   TextRendererApp.main()