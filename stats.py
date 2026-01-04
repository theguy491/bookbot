def get_num_words(text):
    words = text.split()
    return len(words)
        


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items["num"]

def dict_to_list(chars_dict):
    sorted_dict = []
    for char in chars_dict:
        num = chars_dict[char]
        temp_dict = {"char":char, "num":num}
        sorted_dict.append(temp_dict)
    sorted_dict.sort(reverse=True, key=sort_on)

    return sorted_dict


