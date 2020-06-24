import csv
from os import path
class Agent:
    def __init__(self, name):
        if path.isfile('agentFile.csv'):
            self.id = len(open("agentFile.csv").readlines())
        else:
            self.id = 0
        self.name = name

    #def sendText(self, text):
        #sent text to client


class AgentCilent(Agent):
        i = 0


class AgentExpert(Agent):
        i = 0
"""
    def answerQuestion(self,question):


    def sendText(self, text):
        ans = input()
"""