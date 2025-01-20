def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = word_count(file_contents)
    count = character_count(file_contents)

    print_report(words, count)


def word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def character_count(file_contents):
    lower_conversion = file_contents.lower()
    count_result = {}
    for character in lower_conversion:
        if character in count_result:
            count_result[character] += 1
        else:
            count_result[character] = 1
    return count_result

# functions for printing a report

# this one might be unnessary
def report_data(file_contents):
    words = word_count(file_contents)
    chars = character_count(file_contents)
    return words, chars

# converts dictionary to a list of dictionaries
def dict_to_list_conv(chars):
    return [{"char": char, "num": num} for char, num in chars.items()]

# filters non-alphabetic characters out
def filter_alpha(characters_list):
    # each item in characters_list is a dictionary with 'char' and 'num' keys
    filtered_characters = [char_dict for char_dict in characters_list if char_dict['char'].isalpha()]
    return filtered_characters

# sorts based on frequency
def frequency_sort(filtered_characters):
    return sorted(filtered_characters, key=lambda x: x["num"], reverse=True)

# prints formatted report
def print_report(words, count):
    # Convert dictionary to list of dictionaries
    char_list = dict_to_list_conv(count)
    # Filter for alphabetic characters
    filtered_chars = filter_alpha(char_list)
    # Sort by frequency
    sorted_chars = frequency_sort(filtered_chars)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print() # for spacing
    
    # Now loop through the sorted characters
    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
        
    print("--- End report ---")


if __name__ == "__main__":
    main()

