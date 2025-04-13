from stats import word_count, get_character_number, sort_character_dict
import sys

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_content = f.read()
    return  file_content
    
    
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    file_path = sys.argv[1]
    book_content = get_book_text(file_path)
    num_words = word_count(book_content)
    char_count_sorted_list = sort_character_dict(get_character_number(book_content))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_count_sorted_list:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}:{item["count"]}")
    print("============= END ===============")



main()


