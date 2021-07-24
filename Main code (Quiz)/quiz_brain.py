class QuizBrain :
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer.lower() :
            print("you got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct Answer was = {current_answer}")
        print(f"Your Score is :{self.score}/{self.question_number}")
        print("\n")

    def next_question(self):

        current_question = self.question_list[self.question_number]
        current_answer = current_question.answer

        self.question_number += 1

        user_answer = input(f"Q.{self.question_number} {current_question.text}. (True/False) : \n").lower()
        self.check_answer(user_answer , current_answer)
