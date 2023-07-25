import json
import os

def best_book(books):
    # 여기에 코드를 작성합니다.
    filenames = os.listdir('C:/Users/SSAFY/Desktop/jaeeon/project/01_PJT/Movie_track/ALADIN/data/books')
    new_list = [0,'book']
    for file in filenames:
        book = open(f'data/books/{file}', encoding='utf-8')
        book_detail = json.load(book)
        if book_detail['customerReviewRank'] > new_list[0]:
            new_list[1] = book_detail['title']
            new_list[0] = book_detail['customerReviewRank']
    return new_list[1]
    pass


        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    print(best_book(books_list))
