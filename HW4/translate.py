#translate.py

#Kyle Nabors

#Translates whatever the user inputs into pig latin

#Global Variables

word = input("Enter a word to translate:")#ask user for word 

word = word.lower()#puts the word in all lowercase

first_letter = word[0]#gets the first letter of word

if first_letter in "aeiou":#checks if the first letter is a vowel
    #prints the word in piglatten
    print("Pig latin:",word+"way")
else:
    print("Pig latin:",word[1:]+first_letter+"ay")
