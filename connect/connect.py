import psycopg2


class Connect:

    def __init__(self):
        try:
            self.conn = psycopg2.connect("\
                    dbname='Task2'\
                    user='postgres'\
                    host='localhost'\
                    password='172331'\
            ")

            self.cur = self.conn.cursor()

        except:
            print("Erro ao conectar na base da dados")

    def __del__(self):
        print("Conexão finalizada com sucesso")
        del self
