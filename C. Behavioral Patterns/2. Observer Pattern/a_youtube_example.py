from abc import ABC, abstractmethod


# 1️⃣ Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self):
        pass

# 2️⃣ Concrete Observer (User / Subscriber)
class User(Subscriber):
    def __init__(self, name):
        self.name = name
    
    def update(self, channel_name, video_title):
        print(f"{self.name} 🔔 New video from {channel_name}: {video_title}")

# 3️⃣ Subject Interface (Channel)
class Channel(ABC):
    @abstractmethod
    def subscribe(self):
        pass

    @abstractmethod
    def unsubscribe(self):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass

# 4️⃣ Concrete Subject (YouTube Channel)
class YouTubeChannel(Channel):
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    
    def notify_subscribers(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(self.name, video_title)
    
    def upload_video(self, video_title):
        print(f"\n{self.name} uploaded a new video: {video_title}")
        self.notify_subscribers(video_title)

# 5️⃣ Client Code (Usage)
if __name__ == "__main__":
    channel = YouTubeChannel("TechWithMangesh")

    user1 = User("Amit")
    user2 = User("Sneha")
    user3 = User("Rahul")

    channel.subscribe(user1)
    channel.subscribe(user2)
    channel.subscribe(user3)

    channel.upload_video("Observer Design Pattern in Python")

    channel.unsubscribe(user2)

    channel.upload_video("Advanced Python Design Patterns")