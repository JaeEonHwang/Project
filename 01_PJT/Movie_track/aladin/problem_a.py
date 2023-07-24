import json
from pprint import pprint



def book_info(book):
    new_dict = {}
    new_dict['author'] = book['author']
    new_dict['categoryId'] = book['categoryId']
    new_dict['cover'] = book['cover']
    new_dict['description'] = book['description']
    new_dict['id'] = book['id']
    new_dict['priceSales'] = book['priceSales']
    new_dict['title'] = book['title']
    return new_dict
    # 여기에 코드를 작성합니다.  




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    pprint(book_info(book))
