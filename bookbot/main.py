def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    characters = {}

    for char in file_contents:
        char_to_lower = char.lower()

        if (char_to_lower not in characters):
            characters[char_to_lower] = 1
        else:
            characters[char_to_lower] += 1

    return characters

with open("./books/frankenstein.txt", "r") as file:
    file_contents = file.read()
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print(word_count)
    print(char_count)
