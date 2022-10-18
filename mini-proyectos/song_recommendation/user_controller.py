


from typing import List

from song_recommendation.constants import WELCOME_MESSAGE


def get_song_name(list_of_songs: List[str]) -> int:
    

    user_input = input('Enter the name of a song: ')
    if user_input not in list_of_songs:
        raise ValueError('The song name, was not a valid one!')
    
    return list_of_songs.index(user_input)
        

def show_user_welcome_message() -> None:
    print(WELCOME_MESSAGE)
    

def show_recomendations(recomendations: List[str]) -> None:
    print('the recomended songs for you are...')
    for song in recomendations:
        print(song)

    


