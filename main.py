
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def get_num_words(text):
    string_list = text.split()
    print(len(string_list))

def sort_on(d):
    return d["num"]

def get_chars_dict(text):
    characters_dict = {}

    for i in text:
        if i.lower() in characters_dict:
            characters_dict[i.lower()] += 1
        else:
            characters_dict[i.lower()] = 1

    return characters_dict

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num" : num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
            
def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()