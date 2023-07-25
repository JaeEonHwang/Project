import json


def sorted_cs_books_by_price(books, categories):
    # 여기에 코드를 작성합니다. 
    new_dict = {}
    for book in books:
        if 2721 in book['categoryId']:
            new_dict[book['priceSales']] = book['title']
    new_list = list(new_dict.keys())
    new_list.sort(reverse=True)
    final_list = []
    for price in new_list:
        final_list.append(new_dict[price])
    return final_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
