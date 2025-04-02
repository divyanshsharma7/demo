from collections import Counter

def find_duplicate_chars(s):
    char_count = Counter(s)  
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    return duplicates

string = "divyanshsharma"
print(find_duplicate_chars(string))
