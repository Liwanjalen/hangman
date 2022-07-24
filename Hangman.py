def hangman():
    word = "motivated"
    wrong_guesses = 0
    phases = ["",
             "_________",
             "|    |   ",
             "|    0   ",
             "|   /|\  ",
             "|   / \  ",
             "|        "]
    win = False
    letters_left = list(word)
    print("Welcome to Hangman!")
    score_board = ["_"]*len(word)
    while wrong_guesses < len(phases)-1:
        print('\n')
        guess = input("Guess a Letter:\n")
        if guess in letters_left:
            character_index = letters_left.index(guess)
            score_board[character_index] = guess
            letters_left[character_index] = '$'
        else:
            wrong_guesses += 1
        print(''.join(score_board))
        print('\n'.join(phases[0:wrong_guesses+1]))
        if '_' not in score_board:
            print('You win! The word was:')
            print(''.join(score_board))
            win = True
            break
    if not win:
        print('You lose! The word was:')
        print(''.join(score_board))
        print('\n'.join(phases[0:wrong_guesses]))
        print('You lose!')

hangman()
