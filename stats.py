def get_number_words(path):
    return len(path.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def __sort_values(items):
    return items["num"]

def get_sorted_dict(dict):
    new_list = []
    for char, count in dict.items():
        new_dict = {}
        if char.isalpha():
            new_dict["char"] = char
            new_dict["num"] = count
            new_list.append(new_dict)
    new_list.sort(reverse=True , key= __sort_values)
    return new_list
