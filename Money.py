import Constant


class Money:

    @staticmethod
    def get_curr_amount(question_no):
        if question_no == 0:
            return 0
        else:
            return Constant.QUESTIONS_VALUES[question_no - 1]

    @staticmethod
    def get_current_amount(question_no, is_answer_correct):
        if is_answer_correct:
            return Constant.QUESTIONS_VALUES[question_no]
        else:
            if question_no < 4:
                return 0
            elif question_no < 9:
                return 1000
            elif question_no < 15:
                return 32000

