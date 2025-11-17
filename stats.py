def get_num_words(book_string):
    return len(book_string.split())

def get_num_char(book_string):
    book_string_lower = book_string.lower()
    res = {}
    for c in book_string_lower:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res

def sort_char(dict_char):
    list_char = []
    for c in dict_char:
        list_char.append({"char" : c, "num" : dict_char[c]})
    list_char.sort(reverse=True, key=sort_on)
    return list_char

def sort_on(items):
    return items["num"]