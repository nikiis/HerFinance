from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
import json


class Spotify:
    def __init__(self, id, secret):
        self.id = id
        self.secret = secret

    def get_playlists(self):
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.id,
                                                                   client_secret=self.secret))

        results = sp.search(q='investment female', type='show', limit=50, market='GB')

        playlists = []
        for show in results['shows']['items']:
            if 'invest' not in show['name'].lower() and 'investment' not in show['description'].lower():
                continue
            playlists.append({'name': show['name'],
                              'url': show['external_urls']['spotify'],
                              'image': show['images'][0],
                              'description': self.shorten(show['description'], 200),
                              'publisher': show['publisher']})

        return playlists

    @staticmethod
    def shorten(text, amount):
        txt = text[:amount]
        return txt[:txt.rfind(' ')] + '...'


if __name__ == '__main__':
    if not os.environ.get('SPOTIFY_ID') or not os.environ.get('SPOTIFY_SECRET'):
        exit('Need to set spotify id and secret as:\nexport SPOTIFY_ID=xxx\nexport SPOTIFY_SECRET=yyy')

    spot = Spotify(id=os.environ.get('SPOTIFY_ID'), secret=os.environ.get('SPOTIFY_SECRET'))
    playlists = spot.get_playlists()

    if os.environ.get('SPOTIFY_DEBUG'):
        print('\n'.join([p['name'] for p in playlists]))

    with open('playlist.json', 'w') as f:
        json.dump(playlists, f)
