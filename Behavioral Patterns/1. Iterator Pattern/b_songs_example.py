from abc import ABC, abstractmethod

# Step 1: Define the Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

# Step 2: Define the IterableCollection Interface
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Step 3: Implement the Concrete Collection
class Playlist(IterableCollection):
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def get_song_at(self, index):
        return self.songs[index]
    
    def get_size(self):
        return len(self.songs)
    
    def create_iterator(self):
        return PlaylistIterator(self)
    
# Step 4: Implement the Concrete Iterator
class PlaylistIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0
    
    def has_next(self):
        return self.index < self.playlist.get_size()
    
    def next(self):
        song = self.playlist.get_song_at(self.index)
        self.index += 1
        return song

# Step 5: Using the Iterator (Client Code)
def music_player_demo():
    playlist = Playlist()
    playlist.add_song("Shape of You")
    playlist.add_song("Bohemian Rhapsody")
    playlist.add_song("Blinding Lights")
    
    iterator = playlist.create_iterator()
    
    print("Now Playing:")
    while iterator.has_next():
        print(f" 🎵 {iterator.next()}")

music_player_demo()