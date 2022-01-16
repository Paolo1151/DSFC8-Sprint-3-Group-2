import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import keyring
import time

def recommendation_engine():
    st.title('Recommended Songs for seed track: DEDMA')
    st.write("https://open.spotify.com/playlist/5gbaOZOo7Qq5tmPTAP2nrd")
    
    client_id=keyring.get_password('spotify', 'cid')
    client_secret=keyring.get_password('spotify', 'secret') 
    redirect_uri='https://localhost:8888/callback/'

    username = '31ghcybphvuuh3bzfzr6d35pmwuy'
    scope_playlist = 'playlist-modify-public'
    scope_user = 'user-library-modify'

    #Credentials to access the Spotify Music Data
    manager = SpotifyClientCredentials(client_id,client_secret)
    sp = spotipy.Spotify(client_credentials_manager=manager)

    #Credentials to access the library  
    token_user= spotipy.util.prompt_for_user_token(username,scope_user,client_id,client_secret,redirect_uri) 
    sp_user = spotipy.Spotify(auth=token_user)

    #Credentials to access the playlists
    token_playlist= spotipy.util.prompt_for_user_token(username,scope_playlist,client_id,client_secret,redirect_uri) 
    sp_playlist = spotipy.Spotify(auth=token_playlist)
    
    new_playlist_name = "Eskwelabs: Recommendations for seed track DEDMA"    
    new_playlist = sp_playlist.user_playlist_create(username, name=new_playlist_name)
    new_playlist
    
    new_playlist['id']
    
    playlist_id=new_playlist['id']
    sp_playlist.user_playlist_add_tracks(username, playlist_id, track_id_list)

    pass
