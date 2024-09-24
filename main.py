def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        w_count = word_count(file_contents)
        c_count = character_count(file_contents)
        sorted_c_count = sort_character_count(c_count)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{w_count} words found in the document\n")

        for char_dict in sorted_c_count:
            char = char_dict["Character"]
            count = char_dict["Count"]
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")


def word_count(file):
    words = file.split()
    return len(words)

def character_count(file):
    character_count_dict = {}
    lowercase_file = file.lower()
    for char in lowercase_file:
        if not char.isalpha():
            continue
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    return character_count_dict

def sort_character_count(character_count_dict):
    character_list = []
    for char, count in character_count_dict.items():
        char_dict = {"Character" : char, "Count" : count}
        character_list.append(char_dict)
    character_list.sort(key=lambda x: x["Count"], reverse=True)
    return character_list

main()