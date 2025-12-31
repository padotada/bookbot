def get_num_words(text: str)->int:
    return len(text.split())

def characters_dict(text: str)->dict:
    char_dict = {}
    for ch in text:
        ch = ch.lower()
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_list_of_char_dicts(char_dict: dict):
    res = []
    for key, value in char_dict.items():
        res.append({"char": key, "num": value})
    res.sort(reverse=True, key=sort_on)
    return res

    