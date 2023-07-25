"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists():
    # 여기에 코드를 작성합니다.
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_dict = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)
    
    acoustic = [genre for genre in genres_list if genre['name'] == 'acoustic']
    acoustic_id = acoustic[0]['id']
    acoustic_artist = []
    for artist in artists_dict:
        if acoustic_id in artist['genres_ids']:
            acoustic_artist.append(artist['name'])
    return acoustic_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(acoustic_artists())
