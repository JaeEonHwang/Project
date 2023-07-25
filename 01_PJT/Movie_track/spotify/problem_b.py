import json
from pprint import pprint


def artist_info(artist, genres):
    # 여기에 코드를 작성합니다.   
    new_dict ={}
    genres_list = []
    for id in artist['genres_ids']:
        for genre in genres:
            if id == genre['id']:
                genres_list.append(genre['name'])
    new_dict['genre_names'] =genres_list
    new_dict['id'] = artist['id']
    new_dict['images'] = artist['images']
    new_dict['name'] = artist['name']
    new_dict['type'] = artist['type']
    return new_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
