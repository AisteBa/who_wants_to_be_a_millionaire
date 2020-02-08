import random
import Constant


class Help:

    ask_audience = 1
    remove_two_answers = 1
    jump_the_question = 1

    def __init__(self, ask_audience, remove_two_answers, jump_the_question):
        self.ask_audience = ask_audience
        self.remove_two_answers = remove_two_answers
        self.jump_the_question = jump_the_question

    def show_lifelines_left(self):
        print("You have the fallowing helps left:")
        if self.ask_audience != 0:
            print("ask audience")
        if self.remove_two_answers != 0:
            print("remove two answers")
        if self.jump_the_question != 0:
            print("jump the question")
        if self.ask_audience == 0 and self.remove_two_answers == 0 and self.jump_the_question == 0:
            print("You have no helps left, please press Q")
        print("--------------------------------------------")

    def choose_lifelines(self):
        return raw_input("Please choose which help you want to use: \n"
                         "ask audience - press A \n"
                         "remove two answer - press R \n"
                         "jump the question - press J \n"
                         "return to the game - press Q \n")

    def is_help_valid(self, help):
        if help in ("A", "R", "J", "Q"):
            return True
        else:
            return False

    def remove_help(self, help):
        if help == "A":
            self.ask_audience = self.ask_audience - 1
        elif help == "R":
            self.remove_two_answers = self.remove_two_answers - 1
        elif help == "J":
            self.jump_the_question = self.jump_the_question - 1

    def apply_help(self, help, question_no):
        all_answers = ["A", "B", "C", "D"]
        correct_answer = Constant.CORRECT_ANSWERS[question_no]
        all_answers.remove(correct_answer)
        if help == "A":
            percent = str(random.randint(51, 99))
            print("%s percents of audience thinks that the correct answer is %s" % (percent, correct_answer))
        elif help == "R":
            print("Correct answer is %s or %s" % (correct_answer, random.choice(all_answers)))

    def choose_help(self):
        need_help = True
        while need_help:
            self.show_lifelines_left()
            help = (self.choose_lifelines()).upper()
            if self.is_help_valid(help):
                self.remove_help(help)
                return help
                need_help = False
            else:
                print("Please select valid help!")

