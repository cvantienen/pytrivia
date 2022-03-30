print('Welcome to my Trivia game!!')

ans = input('Ready to Play? (Yes/No): ')
score = 0 
total_q = 10

print()
print()
if ans.lower() == 'yes':
    ans = input('1. True or false, California and Texas were once part of Mexico?:  ')
    if ans.lower() == 'true':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT')

    print()
    print()

    ans = input('2. True or false, lemons contain more sugar than strawberrys?:  ')
    if ans.lower() == 'true':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT')


    print()
    print()
    ans = input('3. What Nut Is Used To Make Marzipan?:  ')
    if ans.lower() == 'almonds':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, the correct answer was almonds.')


    print()
    print()
    ans = input('4. A group of goats is called a?:  ')
    if ans.lower() == 'trip':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, a group of goats is called a trip.')


    print()
    print() 
    ans = input('5. What Is The Most Frequently Sold Item At Walmart?:  ')
    if ans.lower() == 'bananas':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, bananas should have been your choice.')



    print()
    print()
    ans = input('6. Ph.D. Stands For What?:  ')
    if ans.lower() == 'doctor of philosophy':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, Doctor of Philosophy should have been your answer.')


    print()
    print()
    ans = input('7. Which Country Has Not Fought A War Since 1814?:  ')
    if ans.lower() == 'sweden':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, Sweden has not been involved in a war for hundereds of years')


    print()
    print()
    ans = input('8. What’s The Total Number Of Dots On A Pair Of Dice?:  ')
    if ans.lower() == '42':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, there are 42 dots on a pair of dice.')



    print()
    print()
    ans = input('9. Which Chess Piece Can Only Move Diagonally?:  ')
    if ans.lower() == 'bishop':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT, the bishop can only move diagonally')


    print()
    print()
    ans = input('10. In What Year The Titanic Sink?:  ')
    if ans.lower() == '1912':
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT')


    print()
    print()
    print('Thanks for playing! You answered', score, 'questions correct.')



