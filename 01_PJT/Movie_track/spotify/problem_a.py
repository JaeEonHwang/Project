import json
from pprint import pprint


def artist_info(artist):
    # 여기에 코드를 작성합니다.
    new_dict ={}
    new_dict['genres_ids'] = artist['genres_ids']
    new_dict['id'] = artist['id']
    new_dict['images'] = artist['images']
    new_dict['name'] = artist['name']
    new_dict['type'] = artist['type']
    return new_dict
    pass


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)
    
    pprint(artist_info(artist_dict))
