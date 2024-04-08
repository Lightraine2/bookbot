def main(): 
    book_path = "books/frankenstein.txt"
        
    def get_book_text(path):
        with open(path) as f:
            return f.read()
    
    def word_count(text):
        words = text.split()
        count = len(words)
        return count

    def char_count(text):
        char_count = {}
        words = text.split()

        for word in words:
            word = word.lower()
            for char in word:
                    if char.isalpha():
                         if char in char_count:
                             char_count[char] += 1
                         else:
                            char_count[char] = 1

        return char_count
    
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    char_count_list = [{'character': char, 'count': count} for char, count in num_chars.items()]

    def print_report():
        print(f"--- Begin report of {book_path} ---")
        print(f"There are {num_words} words in the document.")
        for char_dict in char_count_list:
            print(f"Character '{char_dict['character']}' occurs {char_dict['count']} times.")        
        print("--- End report ---")

    print_report()

main()