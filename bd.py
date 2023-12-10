import psycopg2


def conexao():
    try:
        conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
        return conn
    except:
        print("Erro ao se conectar com o banco de dados")
        return None

DB_NAME = ""
DB_USER = ""
DB_PASS = ""
DB_HOST = "isabelle.db.elephantsql.com"
DB_PORT = "5432"