def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = map_book(text)
    chars_sorted_list = get_chars_dict(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    # print("--- Begin report of books/frankenstein.txt ---")
    # print(f"{num_words} words found in the document")
    # print("")
    # print("")
    
    # print(chars_dict)  rf
    # print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)
 #get some

def map_book(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):    
    with open(path) as f:
        return f.read()
 
def sort_on(dic):
    return dic["num"]

def get_chars_dict(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
