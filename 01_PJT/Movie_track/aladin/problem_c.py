import json
from pprint import pprint


def books_info(books, categories):
    # 여기에 코드를 작성합니다.  
    new_list = []   
    for book in books:
        new_dict = {}
        new_dict['author'] = book['author']
        category_list = []
        for ID in book['categoryId']:
            for id in categories_list:
                if ID == id['id']:
                    category_list.append(id['name'])
        new_dict['categoryName'] = category_list
        new_dict['cover'] = book['cover']
        new_dict['description'] = book['description']
        new_dict['id'] = book['id']
        new_dict['priceSales'] = book['priceSales']
        new_dict['title'] = book['title']
        new_list.append(new_dict)
    return new_list
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)
    pprint(books_info(books, categories_list))