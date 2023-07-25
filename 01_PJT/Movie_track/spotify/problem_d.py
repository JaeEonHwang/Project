import json
import os

def max_revenue(artists):
    # 여기에 코드를 작성합니다.
    filenames = os.listdir('data/artists')
    new_list = [0,'artist']
    for filename in filenames:
        file = open(f'data/artists/{filename}', encoding='utf-8')
        file_list = json.load(file)
        if file_list['popularity'] > new_list[0]:
            new_list[0] = file_list['popularity']
            new_list[1] = file_list['name']
    return new_list[1]



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(max_revenue(artists_list))
