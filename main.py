def main():
    print(report())

def text():
     with open("books/frankenstein.txt") as f:
        file_content = f.read()
        return file_content

def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_characters(file_content):
    characters = [*file_content]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    dictionnary = {}

    for letter in alphabet:
        dictionnary[letter] = 0

    for character in characters:
        if character.lower() not in alphabet:
            pass
        else:
            dictionnary[character.lower()] += 1
    
    return dictionnary


def sorted_characters_count(dictionnary):
    sorted_pairs = sorted(dictionnary.items(), key=lambda x:x[1], reverse=True)

    return dict(sorted_pairs)

def report():
    letter_count = count_characters(text())
    sorted_count = sorted_characters_count(letter_count)
    header = "--- Begin report of books/frankenstein.txt ---\n"
    words_count = f"{count_words(text())} words found in the document\n"
    content = ""
    footer = "--- End report ---\n"

    keys = sorted_count.keys()
    for key in keys:
        content += f"The '{key}' character was found {sorted_count[key]} times\n"

    return header + words_count + content + footer

main()