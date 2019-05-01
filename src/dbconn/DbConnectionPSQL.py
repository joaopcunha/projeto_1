import psycopg2
import psycopg2.extras
import logging

class DbConnectionPSQL:

    def __init__(self, host, user, password, database):
        try:
            self.__conn = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=database
            )

        except Exception as e:
            raise ValueError(
                "Unable to connect to the database \n Error: {}".format(e)
                )

    def select(self, sql:str):
        try:
            conn = self.__conn
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cur.execute(sql)
            rows = cur.fetchall()
            conn.commit()

            return rows

        except Exception as e:
            conn.commit()
            raise ValueError(
                "Unable to run select query {} \n Error: {}".format(sql, e)
            )

    def insert(self, sql:str, values=None):
        try:
            conn = self.__conn
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            return True

        except Exception as e:
            conn.commit()
            raise ValueError(
                "Unable to run insert query {} \n Error: {}".format(sql, e)
            )

    def run_query(self, sql:str):
        try:
            conn = self.__conn
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            return True

        except Exception as e:
            conn.commit()
            raise ValueError(
                "Unable to run query {} \n Error: {}".format(sql, e)
            )

    def create_indexes(self, indexes, table_name):
        try:
            conn = self.__conn
            for index in indexes:
                cur = conn.cursor()
                cur.execute("CREATE INDEX {} ON {} ({})".format(
                    index, table_name, index
                ))
                conn.commit()
            return True

        except Exception as e:
            conn.commit()
            raise ValueError(
                "Unable to create index for table {} \n Error: {}".format(table_name, e)
            )

    def close_connection(self):
        if self.__conn:
            self.__conn.close()