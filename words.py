def find_words(letters, file_name):
    lst = list(letters.strip())
    found_words = []
    with open(file_name, "r") as f:
        for line in f:
            temp_letters = list(letters.strip())
            temp_dict = list(line.strip())
            for char in line.strip():
                if char not in temp_letters:
                    continue
                elif char in temp_letters:
                    temp_dict.remove(char)
                    temp_letters.remove(char)
            if len(temp_dict) == 0:
                found_words.append(line.strip())
    return found_words


def main():
    user = input("Please enter a value between 1 and 7 (inclusive)\n> ")


print(find_words("tdri", "enable1.txt"))