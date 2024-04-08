def main(): 
    book_path = "books/frankenstein.txt"
        
    def get_book_text(path):
        with open(path) as f:
            return f.read()
    
    def wordCount(text):
        words = text.split()
        count = len(words)
        return count

    def charCount(text):
        char_count = {}
        words = text.split()

        for word in words:
            word = word.lower()
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        return char_count
    
    text = get_book_text(book_path)
    num_words = wordCount(text)
    num_chars = charCount(text)

    print(num_words)    
    print(num_chars)

main()