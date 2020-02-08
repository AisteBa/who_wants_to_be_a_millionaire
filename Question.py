import Constant


class Question:

    @staticmethod
    def validate_guess(question_no, guess):
        if Constant.CORRECT_ANSWERS[question_no] == guess.upper():
            print("Congrats! Your answer is correct.")
            return True
        else:
            print("Sorry, your answer is wrong.. :(")
            return False

    @staticmethod
    def ask_question(question_no):
        print("Press H if you want to use Help\n")
        print("%s." % str(int(question_no) + 1))
        if question_no == 0:
            return raw_input("In the \"Road Runner and Coyote\" cartoons, what famous sound does the Road Runner make?\n\
                              A: Ping! Ping!\n\
                              B: Beep! Beep!\n\
                              C: Aooga! Aooga!\n\
                              D: Vroom! Vroom!\n")
        elif question_no == 1:
            return raw_input("Where should choking victims place their hands to indicate to others that they need help?\n\
                              A: Over the eyes\n\
                              B: On the knees\n\
                              C: Around the throat\n\
                              D: On the hips\n")
        elif question_no == 2:
            return raw_input("Which of these dance names is used to describe a fashionable dot?\n\
                              A: Hora\n\
                              B: Swing\n\
                              C: Lambada\n\
                              D: Polka\n")
        elif question_no == 3:
            return raw_input("In what \"language\" would you say \"ello-hay\" to greet your friends?\n\
                              A: Bull Latin\n\
                              B: Dog Latin\n\
                              C: Duck Latin\n\
                              D: Pig Latin\n")
        elif question_no == 4:
            return raw_input("What part of a chicken is commonly called the \"drumstick\"?\n\
                              A: Breast\n\
                              B: Wing\n\
                              C: Leg\n\
                              D: Gizzard\n")
        elif question_no == 5:
            return raw_input("What is the only position on a football team that can be \"sacked\"?\n\
                              A: Center\n\
                              B:  Wide receiver\n\
                              C: Tight end\n\
                              D: Quarterback\n")
        elif question_no == 6:
            return raw_input("What god of love is often depicted as a chubby winged infant with a bow and arrow?\n\
                              A: Zeus\n\
                              B: Mercury\n\
                              C: Cupid\n\
                              D: Poseidon\n")
        elif question_no == 7:
            return raw_input("What Steven Spielberg film climaxes at a place called Devil's Tower?\n\
                              A:  E.T: The Extra-Terrestrial\n\
                              B: Jurassic Park\n\
                              C: Raiders of the Lost Ark\n\
                              D: Close Encounters of the Third Kind\n")
        elif question_no == 8:
            return raw_input("In what U.S. town did the famous 1881 shoot-out at the O.K. Corral take place?\n\
                              A: Laramie\n\
                              B: Tombstone\n\
                              C: El Paso\n\
                              D: Dodge City\n")
        elif question_no == 9:
            return raw_input("Which of the following months has no U.S. federal holiday?\n\
                              A: August\n\
                              B: February\n\
                              C: September\n\
                              D: November\n")
        elif question_no == 10:
            return raw_input("What mythological beast is reborn from its own ashes?\n\
                              A: Phoenix\n\
                              B: Minotaur\n\
                              C: Dragon\n\
                              D: Golem\n")
        elif question_no == 11:
            return raw_input("Who developed the first effective vaccine against polio?\n\
                              A: Albert Sabin\n\
                              B: Niels Bohr\n\
                              C: Louis Pasteur\n\
                              D: Jonas Salk\n")
        elif question_no == 12:
            return raw_input("Which of the following is not a monotheistic religion?\n\
                              A: Islam\n\
                              B: Judaism\n\
                              C: Hinduism\n\
                              D: Christianity\n")
        elif question_no == 13:
            return raw_input("What architect designed the glass pyramid in the courtyard of the Louvre?\n\
                              A: Philip Johnson\n\
                              B: Le Corbusier\n\
                              C: Frank Gehry\n\
                              D:  I.M. Pei\n")
        elif question_no == 14:
            return raw_input("Which of these US presidents appeared on the television series \"Laugh-In?\"? \n\
                              A: Lyndon Johnson\n\
                              B: Richard Nixon\n\
                              C: Jimmy Carter\n\
                              D: Gerald Ford\n")
