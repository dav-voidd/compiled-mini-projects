#The Music Playlist Shuffler (Linked List)



class SongNode:
    def __init__(self, song_title, artist):
        self.song_title = song_title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, song, artist):
        new_song = SongNode(song, artist)
        if self.head is None:
            self.head = new_song
            self.current = new_song
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_song

    def skip_song(self):
        if self.head is None:
            print("The playlist is empty add more songs!")
            return

        print(f"Skipping: {self.current.song_title}")
        self.current = self.current.next
        print(f"Now playing: {self.current.song_title}")


    def play_all(self):
        current_song = self.current
        while current_song is not None:
            print(f"Now playing: [{current_song.song_title}] by {current_song.artist}")
            current_song = current_song.next
        print("No more songs")

playlist = Playlist()
while True:
    user_input = input("Type (p) to play all, (s) to skip song, (a) to add song: ")
    if user_input == 'p':
        playlist.play_all()
    elif user_input == 's':
        playlist.skip_song()
    elif user_input == 'a':
        user_song = input("Whats the name of the song: ")
        user_artist = input("Whats the name of the artist?: ")
        playlist.add_song(user_song, user_artist)
    else:
        print("Invalid")
