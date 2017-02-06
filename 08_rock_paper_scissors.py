'''
----------------------------------------
TASK 8 from http://www.practicepython.org/
----------------------------------------
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors # V
Scissors beats paper
Paper beats rock # V

'''

#
# SOLUTION
# created by Kostya
# on 4 Jan 2017
# Time spent: 18 min
#


if __name__ == '__main__':

    def process_answers():

        answers = []

        i = 1
        while i < 3:
            answer_str = input( "Player {} turn: ".format( i ) )
            i += 1
            answers.append( answer_str.lower() )

        if ( answers[0] == "rock" and answers[1] == "scissors" ) or ( answers[0] == "scissors" and answers[1] == "paper" ) or ( answers[0] == "paper" and answers[1] == "rock" ):
            print( "Player 1 win!\n" )
        elif answers[0] == answers[1]:
            print( "It's a tie!" )
        else:
            print( "Player 2 win!\n" )


    process_answers()

    while True:
        again = input( "Want to play again? ( y/n )" )

        if again == "y":
            False
            process_answers()
        elif again == "n":
            import sys
            sys.exit()

