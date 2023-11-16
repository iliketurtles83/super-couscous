import pandas as pd
import pickle
from os import path

SITE_ROOT = path.realpath(path.dirname(__file__))

# get titles.pkl
titles = pickle.load(open(path.join(SITE_ROOT, 'titles.pkl'), 'rb'))

weighted_sim = pickle.load(open(path.join(SITE_ROOT, 'weighted_sim.pkl'), 'rb'))

def get_track_id(artist, song):
    '''Get index from titles where artist and song match'''
    
    try:
        track_id = titles[(titles['artist'] == artist) & (titles['name'] == song)].index[0]
        return track_id
    except IndexError:
        print('Song not found in database')
        return None

def get_song(index):
    '''Get song artist and name at index'''
    try:
        row = titles.iloc[index]
        artist_song = row['artist'] + ' - ' + row['name']
        return artist_song
    except IndexError:
        print('Index not found in database')
        return None

def recommend_content(artist, title, sim_matrix = weighted_sim):
    '''Get similar songs using the similarity matrix'''
    # get index for our song
    idx = get_track_id(artist, title)
    
    # get similarity scores of all songs w.r.t to our song
    sim_scores = list(enumerate(sim_matrix[idx]))
    
    # sort scores based on similarity
    sorted_sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # limit to 20 songs
    sorted_sim_scores = sorted_sim_scores[1:20]

    # get song artist and names
    content_similar_scores = []
    for i in sorted_sim_scores:
        content_similar_scores.append(get_song(i[0]))
    
    return content_similar_scores