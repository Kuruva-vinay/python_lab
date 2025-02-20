# Accept a string and count the number of uppercase letters, lowercase letters, vowels, consonants, and spaces using a class

class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.uppercase_count = 0
        self.lowercase_count = 0
        self.vowel_count = 0
        self.consonant_count = 0
        self.space_count = 0

    def analyze_string(self):
        vowels = "AEIOUaeiou"
        for char in self.input_string:
            if char.isupper():
                self.uppercase_count += 1
            if char.islower():
                self.lowercase_count += 1
            if char in vowels:
                self.vowel_count += 1
            if char.isalpha() and char not in vowels:
                self.consonant_count += 1
            if char.isspace():
                self.space_count += 1

    def display_counts(self):
        print(f"Uppercase letters: {self.uppercase_count}")
        print(f"Lowercase letters: {self.lowercase_count}")
        print(f"Vowels: {self.vowel_count}")
        print(f"Consonants: {self.consonant_count}")
        print(f"Spaces: {self.space_count}")

# Accept a string from the user
input_string = input("Enter a string: ")

# Create an object of the StringAnalyzer class
analyzer = StringAnalyzer(input_string)

# Analyze the string
analyzer.analyze_string()

# Display the counts
analyzer.display_counts()
