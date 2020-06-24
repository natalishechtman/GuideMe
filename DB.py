import csv
from Query import Query


class DB:
    def __init__(self, queries_DB_file):
        self.info = {}
        self.size = 0
        self.queries = []

        with open(queries_DB_file) as DB_file:
            csv_reader = csv.reader(DB_file, delimiter=',')
            for row in csv_reader:
                new_query = Query(id=row[0], question=row[1], answer=row[2])
                self.queries.append(new_query)

    def addQuery(self, question, answer):
        new_query = Query(question=question, answer=answer, id=(len(self.queries)))
        self.queries.append(new_query)

    def updateQuery(self, query, answer):
        self.queries[int(query.id)].answer = answer


"""
    def removeQuery(self, question):
        # add Question to DB
    def getQuery(self, id):
        # add Question to DB
"""
DB("query_list.csv")
