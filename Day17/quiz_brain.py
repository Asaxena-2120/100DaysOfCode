class QuizBrain:

    def __init__(self,q_list):
        # Attribute to keep track of the question number from the question list
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        # Retrieve current question from question list
        curr_question_no = self.question_number
        curr_question = self.question_list[curr_question_no]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False) ")
        self.check_answer(user_answer,curr_question.answer)

    # Checks if all questions are over
    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    # To check if user answer matches given answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!!")
            self.score +=1

        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your correct score is {self.score}/{self.question_number}")
        print()

