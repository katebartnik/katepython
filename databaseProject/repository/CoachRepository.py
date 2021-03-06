import sys
sys.path.insert(1, '../tools')

import DatabaseConnector

class CoachRepository:
    def __init__(self):
        self.__connection = DatabaseConnector.DatabaseConnection()

    def findAll(self):
        query = self.__connection.query("SELECT * FROM coach", '')
        return query.fetchall()

    def findOneById(self, id):
        query = self.__connection.query("SELECT * FROM coach WHERE id = %s", [id])
        return query.fetchall()

    def findOneByLanguage(self, language):
        query = self.__connection.query("SELECT * FROM coach LEFT JOIN coach_rank ON coach.coach_rank_"
                                        "id = coach_rank.id WHERE coach_rank.name = 'VIP'", [language])
        return query.fetchall()

    def insertCoach(self, name, surname):
        query = self.__connection.query("INSERT INTO coach (name, surname) VALUES (%s, %s)", [name, surname])
        return query.fetchall()

    def findOnebyPrice(self, price):
        query = self.__connection.query("SELECT * FROM coach WHERE price = ") [price]
        return query.fetchall()



