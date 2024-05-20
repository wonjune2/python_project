#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

# for (index, row) in df.iterrows():
#     print(row.letter)



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on = True
while is_on:
    try:
        name = input("Enter a word: ").upper()
        letters = [nato_dict[letter] for letter in name]
        print(letters)
        is_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")


