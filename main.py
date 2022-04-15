import pandas
from logo import logo

print(logo)

morse_data = pandas.read_csv("alphabet_to_morse.csv")
morse_data_dict = {row.letter: row.code for (index, row) in morse_data.iterrows()}

word = input("Enter the message: ").upper()

try:
    output = [morse_data_dict[letter] for letter in word]
except KeyError:
    print("Please only enter letters or numbers.")
else:
    output_formatted = ('  '.join(output))
    print(output_formatted)
