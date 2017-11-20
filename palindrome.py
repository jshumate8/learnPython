#This code teaches how to manipulate a word as an array of characters, and how to reverse an array in python.
#Python automatically turns strings into an array of characters. The keyword "list" allows you to interact with the string's characters as an array.
#The if function utilizes the reverse of an array. To reverse an array, use [::-1].
user_word = input("Please give me a word: ")
print("You input " + user_word)
print(user_word.title() + " backwards is " + user_word[::-1])
if (user_word[::1]) == (user_word[::-1]):
    print("Palindrome!")
else:
    print("Sorry, " + user_word + " is not a palindrome.")