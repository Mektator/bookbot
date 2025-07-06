def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_char(text):
    num_char = {}
    for char in text.lower():
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    num_char = [{"char": char, "num": count} for char, count in num_char.items()]
    return num_char

def sort_on(items):
    return items["num"]