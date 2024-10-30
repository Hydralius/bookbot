def count_words(string):
        words = string.split()
        print(f"Number of words: {len(words)}")
# Splits the given string into a list of words and prints the total number of words.        

def count_characters(counting):
        new_dict = {}
        lowered_string = counting.lower()

        for char in lowered_string:
            if char.isalpha():
                if char in new_dict:
                    new_dict[char] += 1
                else:
                    new_dict[char] = 1
        
        return new_dict
# Converts the string to lowercase and counts each alphabetic character.
# Returns a dictionary with characters as keys and their counts as values.    
        
def main():
    with open("books/frankenstein.txt")as f:
       file_contents = f.read()

       result = count_characters(file_contents)
       sorted_characters = sorted(result.items(), key=lambda item: item[1], reverse=True)

       print("\n--- Begin report ---")
       count_words(file_contents)

       for char, count in sorted_characters:
            print(f"The '{char}' character was found {count} times")

       print("--- End report ---")
       print(file_contents)
       # Comment out the line below if you do not wish to print the entire book content.
       
# Opens and reads the text file.       
# Uses count_characters to generate a dictionary of character counts.
# Sorts the characters based on frequency in descending order.
# Prints the report on word and character counts.
main()

