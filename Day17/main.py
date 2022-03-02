from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# A list of question objects
question_bank = []

# pulling data from question_data to make Question objects
for dictionary in question_data:
    new_question = Question(dictionary['text'],dictionary['answer'])
    question_bank.append(new_question)

# Create QuizBrain object
quiz = QuizBrain(question_bank)

# Continues to list next question from question_list until all the questions are over
while quiz.still_has_question():
    quiz.next_question()
