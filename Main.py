import Constant
from Help import Help
from Money import Money
from Question import Question


class Main:

    @staticmethod
    def run():
        print("Hello, please welcome to the game \"Who Wants To Be A Millionaire\"")
        i = 0
        question = Question()
        my_money = Money()
        my_helps = Help(1, 1, 1)

        while i <= Constant.TOTAL_QUESTIONS:
            if i == Constant.TOTAL_QUESTIONS:
                print("Congratulations you just have won a million!!!!")
                break

            print("You have: %s EUR" % my_money.get_curr_amount(i))
            answer = raw_input("Press any key if you want to play\nPress Q if you want to take the money and quit\n")
            if str(answer).upper() == "Q":
                print("Thank you for playing! See you next time..")
                break
            guess = question.ask_question(i)
            if str(guess).upper() == "H":
                help = my_helps.choose_help()
                if help == "J":
                    print("You skipped the question, the right answer was %s" % Constant.CORRECT_ANSWERS[i])
                    i = i + 1
                    continue
                elif help in ("A", "R"):
                    my_helps.apply_help(help, i)
                guess = raw_input("Please choose your answer:\n")
            if not question.validate_guess(i, guess):
                print("You have: %s EUR" % my_money.get_current_amount(i, False))
                print("Thank you for playing! See you next time..")
                break
            else:
                i = i + 1


if __name__ == "__main__":
    Main.run()
