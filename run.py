import os

from youtube_client import YouTubeClient
from spotify_client import SpotifyClient

def run():
    # 1. Get a list of the user's playlists from YouTube
    youtube_client = YouTubeClient('./credentials/client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()

    # 2. Ask which playlist the user wants to retrieve music from
    for index, playlist in enumerate(playlists):
        print(str(index)+": "+playlist.title)
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print("You selected: "+chosen_playlist.title)

    # 3. For each video in the chosen playlist, get the song info from YouTube
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print("Attempting to add "+str(len(songs))+" items")

    # 4. Search for the song on Spotify and add to Spotify Liked Songs list
    for song in songs:
        # spotify_song_id = spotify_client.search_song(song.artist, song.track)
        spotify_song_id = spotify_client.search_song("music", song)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                # print("Added "+song.track+" ("+song.artist+")")
                print("Added "+song)


if __name__ == '__main__':
    run()
