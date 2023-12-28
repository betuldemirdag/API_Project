import pandas as pd

def get_data(limit, sp):
    """
    getting data for spesific user: artist_name, popularity, genre, followers

    Params:

    limit: maximum number of artists to show

    Returns:

    Dataframe of the artist list of following of the selected user
    """
    

    all_data = []

    results = sp.current_user_followed_artists(limit = limit)
    artists = results['artists']['items']


    for artist in artists:
        data = {
            "artist_name": artist['name'],
            "popularity": artist['popularity'],
            "genre": artist['genres'],
            "followers": artist["followers"]["total"]
            }
        all_data.append(data)
        
    return pd.DataFrame(all_data)