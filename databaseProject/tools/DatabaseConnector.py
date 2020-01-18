import psycopg2

class DatabaseConnection(object):

    def __init__(self):
        self._db_connection = psycopg2.connect("dbname='symfony' user='symfony' host='beta.videotrener.co' password='symfony'")
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_cur

    def __del__(self):
        self._db_connection.close()
