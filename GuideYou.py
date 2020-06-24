from Agent import AgentExpert
import csv
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

print('Wellcome to Guide You')
print('Hi dear expert, please enter your name:')

agentName = input('> ')
print('waiting for client to connect....')
agentExpert = AgentExpert(agentName)
agentFile = open("agentFile.csv", "a+", newline='')
csvFile = csv.writer(agentFile, delimiter=',')
csvFile.writerow([agentExpert.id, agentExpert.name])
agentFile.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('client connected:', addr)
        while True:
            print('please wait for question...')
            data = conn.recv(1024)
            print('please answer to the client:')
            print(data.decode())
            ans = input('> ')
            conn.sendall(ans.encode())
            if not data:
                break


"""


questionFile = open("Question.csv", "r")
AnswersFile = open("Answers.csv", "w")

while(0):
    questionFile = open("Question.csv", "r")
    for Q in QuestionFile.readlines():
        print(Q)
        agentAns = input()
"""



