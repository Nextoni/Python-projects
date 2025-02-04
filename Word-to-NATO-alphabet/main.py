import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code  for index, row in df.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        transformed_word = [alphabet[let] for let in word]

    except KeyError:
        print("Sorry! Only letters are allowed!")
        generate_phonetic()

    else:
        print(transformed_word)

generate_phonetic()