import json
import os

def new_books(books):
    # 여기에 코드를 작성합니다.  
    filenames = os.listdir('C:/Users/SSAFY/Desktop/jaeeon/project/01_PJT/Movie_track/ALADIN/data/books')
    new_list = []
    for file in filenames:
        book = open(f'data/books/{file}', encoding='utf-8')
        book_detail = json.load(book)
        if book_detail['pubDate'][:4] == '2023':
            new_list.append(book_detail['title'])
    pass



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    print(new_books(books_list))
