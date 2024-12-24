import question_model
import data
import quiz_brain

question_bank = []

for data in data.question_data:
    question = question_model.Question(data.get("text"), data.get("answer"))
    question_bank.append(question)

quiz_brain = quiz_brain.QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

