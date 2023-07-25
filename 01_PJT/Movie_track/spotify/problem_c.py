import json
from pprint import pprint


def artist_info(artists, genres):
    # 여기에 코드를 작성합니다.
    new_list = []
    for artist in artists:
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
        new_list.append(new_dict)
    return new_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)
    
    pprint(artist_info(artists_list, genres_list))
