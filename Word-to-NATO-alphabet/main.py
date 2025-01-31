import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code  for index, row in df.iterrows()}

word = input("Enter a word: ").upper()
transformed_word = [alphabet[let] for let in word]

print(transformed_word)