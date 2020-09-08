import requests
import urllib.parse


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self, artist, track):
        # query = urllib.parse.quote(artist + " " + track)
        query = urllib.parse.quote(track)
        url = "https://api.spotify.com/v1/search?q="+query+"&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+self.api_token
            }

        )
        response_json = response.json()

        results = response_json['tracks']['items']
        if results:
            # assuming first track is the most relevant
            return results[0]['id']
        else:
            # raise Exception("No matches for "+artist+" - "+track)
            print("No matches for "+track)
            return

    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer "+self.api_token
            }
        )

        return response.ok