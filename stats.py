def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    num_chars = {}
    
    for l in text:
        c = l.lower()
        if (c not in num_chars):
            num_chars[c] = 0
        num_chars[c] += 1
    return num_chars

def sort_count(num_chars):
    sorted_list = []
    
    for k in num_chars:
        sorted_list.append({ "name": k, "count": num_chars[k]})
    sorted_list.sort(reverse=True, key=sort_on_count)
    return sorted_list

def sort_on_count(dict):
    return dict["count"]
