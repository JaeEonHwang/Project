import json
import os

def dec_artists(artists):
    # 여기에 코드를 작성합니다.
    filenames = os.listdir('data/artists')
    new_list = []
    for filename in filenames:
        file = open(f'data/artists/{filename}', encoding='utf-8')
        file_list = json.load(file)
        if file_list['followers']['total'] > 10000000:
            empty_dict = {}
            empty_dict['name'] = file_list['name']
            empty_dict['uri-id'] = file_list['uri'].split(':')[2]
            new_list.append(empty_dict)
    return new_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
