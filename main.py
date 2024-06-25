
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    count_words(file_contents)

def count_words(text):
    string_list = text.split()

    print(len(string_list))








if __name__ == "__main__":
    main()