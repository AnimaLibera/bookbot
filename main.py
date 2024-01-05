def main():

    path_to_file = "./books/frankenstein.txt"
    #text = load_text(path_to_file)
    #number_words = count_words(text)
    #print(count_letters(text))
    print_report(path_to_file)

def load_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    number_words = len(words)
    return number_words

def count_letters(text):
    letter_dicitionary = {}
    lowercase_text = text.lower()
    
    for character in lowercase_text:
        if character in letter_dicitionary:
            letter_dicitionary[character] += 1
        else:
            letter_dicitionary[character] = 1
   
    return letter_dicitionary

def print_report(path_to_file):
    text = load_text(path_to_file)
    number_words = count_words(text)
    letter_dicitionary = count_letters(text)
    letter_list = list(letter_dicitionary)
    letter_list.sort()

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{number_words} words found in the document")
    print()
    
    for letter in letter_list:
        if letter.isalpha():
            print(f"The \'{letter}\' character was found {letter_dicitionary[letter]} times")

    print()
    print("--- End report ---")

main()