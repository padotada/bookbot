from stats import get_num_words, characters_dict, sorted_list_of_char_dicts
import sys

def get_book_text(file_path: str)->str:
    with open(file_path, encoding="utf8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = characters_dict(book_text)
    sorted_char_dicts = sorted_list_of_char_dicts(char_dict)
    for i in sorted_char_dicts:
        if not i["char"].isalpha():
            continue
        else:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
main()