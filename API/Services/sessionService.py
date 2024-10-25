from datetime import date
from Class.session import Session
from connect import connect
from config import load_config


def doesTodaySessionExists() -> bool:
    """Check if a session is already created for today
    
    Return: One if the session already exists, Zero else
    """
    
    config = load_config(filename="database.ini", section='PostgreSQL')
    with connect(config) as conn:
        with conn.cursor() as cur:
            sqlVerif = f"""select count(1) from session
                            where date = '{date.today()}'"""
            
            cur.execute(sqlVerif)
            result = cur.fetchone()
            return result[0] == 0

def GetTodaySession(themeBlindTest:str = None) -> str:
    global idSession
    config = load_config(filename="database.ini", section='PostgreSQL')
    with connect(config) as conn:
        with conn.cursor() as cur:
            if doesTodaySessionExists():
                session=Session(themeBlindTest)

                sqlInsert = f"""
                                insert into session (id, date, nbshooters, themeblindtest, nbdropcoupe)
                                values ('{session.id}', '{session.date}', {session.nbShooters}, '{session.themeBlindTest}', {session.nbDropCoupe})
                            """
                
                cur.execute(sqlInsert)
                idSession = session.id
            else:
                sqlSelect = f"""
                                select id from session where date = '{date.today()}'
                            """
                
                cur.execute(sqlSelect)
                result = cur.fetchone()
                idSession = result[0]
    return idSession