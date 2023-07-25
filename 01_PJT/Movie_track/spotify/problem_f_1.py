"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
import os


def get_popular():
    # 여기에 코드를 작성합니다.
    artist_list = []
    filenames = os.listdir('data/artists')
    for filename in filenames:
        file = open(f'data/artists/{filename}', encoding='utf-8')
        file_list = json.load(file)
        if 5000000 < file_list['followers']['total'] < 10000000:
            empty_dict = {}
            empty_dict['follwers'] = file_list['followers']['total']
            empty_dict['name'] = file_list['name']
            artist_list.append(empty_dict)
    return artist_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_popular())
