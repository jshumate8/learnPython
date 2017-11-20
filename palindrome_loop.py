again_prompt = True
while again_prompt:
    user_word = raw_input("Please give me a word: ")

    for i in range(0, len(user_word)):
        norm_word = user_word[i]

    for i in range(len(user_word)-1, -1, -1):
        rev_word = user_word[i]

    if norm_word == rev_word:
        print("Palindrome!")

    else:
        print("Not a palindrome.")

    play_again = raw_input("Hit any key to play again, or press 'q' to Quit.")
    
    if play_again == "q" or play_again == "Q":
        break
        


    