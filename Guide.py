import socket
from Query import Query
from DB import DB

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

class Guide:
    def __init__(self, stepFile, port, gameDB):
        text_file = open(stepFile, encoding="utf8")
        self.currentStep = 0
        self.steps = text_file.readlines()
        self.stepsLen = len(self.steps)
        self.port = port
        self.DB = gameDB
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, self.port))

    def showNextStep(self):
        if self.currentStep < self.stepsLen:
            print('\n'+self.steps[self.currentStep])
            self.currentStep += 1
            return True
        else:
            return False

    def showDoneOrHelp(self):
        print("please choose:\n1.Done step.\n2.Need help.")
        ans = input('> ')
        if ans == "1":
            return False
        elif ans == "2":
            return True
        else:
            print("invalid input, let try again!!!")
            return self.showDoneOrHelp()

    def showGetHelp(self):
        print("How Can i help you?")
        ans = input('> ')
        return ans

    def isQuestionCorrect(self,query):
        print('\n' + "did you mean: ")
        query.showQuestion()
        print('\n' +"please choose:\n1.yes.\n2.No.")
        ans = input('> ')
        if ans == "1":
            return True
        elif ans == "2":
            return False
        else:
            print("invalid input, let try again!!!")
            return self.isQuestionCorrect()

    def isAnsCorrect(self,query):
        query.showAnswer()
        print('\n'+"did it fix the problem?")
        print('\n' +"please choose:\n1.yes.\n2.No.")
        ans = input('> ')
        if ans == "1":
            return True
        elif ans == "2":
            return False
        else:
            print("invalid input, let try again!!!")
            return self.isAnsCorrect()

    def goToExpert(self, question, query=None):

        question_as_bytes = str.encode(question)
        self.sock.sendall(question_as_bytes)
        answer = self.sock.recv(1024)
        print(answer.decode())
        if query:
            self.DB.updateQuery(query=query, answer=answer)
        else:
            self.DB.addQuery(question=question, answer=answer)
        """
        print('\n'+"did it fix the problem?")
        print('\n' +"please choose:\n1.yes.\n2.No.")
        fixed = input()
        if fixed == "1":
            self.DB.addQuery(question=question, answer=answer)
            return

        elif fixed == "2":
            # TODO: need to create relation to qutions
            return self.goToExpert()
        else:
            print("invalid input, let try again!!!")
            return self.goToExpert()
        """
