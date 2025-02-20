def count_characters_in_file(filename):
    char_count = {}
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count

filename = input("Enter the filename: ")
char_count = count_characters_in_file(filename)

for char, count in char_count.items():
    print(f"'{char}': {count}")
