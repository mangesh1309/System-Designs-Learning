from abc import ABC, abstractmethod

# FileSystemItem: interface
# File: implements FileSystemItem
# Folder: implements FileSystemItem
# FileSystem: Composite pattern
# Client Code

class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def display(self):
        pass

class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display(self):
        print(f"File: {self.name} - {self.size} bytes")

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item: FileSystemItem):
        self.items.append(item)
    
    def remove_item(self, item: FileSystemItem):
        self.items.remove(item)
    
    def get_size(self):
        total = 0 # Composite pattern
        for item in self.items:
            total += item.get_size()
        return total
    
    def display(self):
        print(f"Folder: {self.name}")
        for item in self.items:
            item.display()

class FileSystem:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: FileSystemItem):
        self.items.append(item)
    
    def remove_item(self, item: FileSystemItem):
        self.items.remove(item)
    
    def get_total_size(self):
        total = 0 # Composite pattern
        for item in self.items:
            total += item.get_size()
        return total
    
    def display(self):
        for item in self.items:
            item.display()

# CLIENT CODE

file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)
folder1 = Folder("folder1")
folder1.add_item(file1)
folder1.add_item(file2)
folder2 = Folder("folder2")
folder2.add_item(folder1)

print(folder2.get_size())
folder2.display()