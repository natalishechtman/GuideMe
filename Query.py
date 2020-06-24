class Query:
    def __init__(self, question, answer=None,id=None):
        self.id = id
        self.question = question
        self.answer = answer


    def setAnswer(self, answer):
        self.answer = answer

    def showQuestion(self):
        print(self.question)

    def showAnswer(self):
        print('\n' +self.answer)