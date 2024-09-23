from datetime import date
from API.connect import connect
from config import load_config


def doesTodaySessionExists() -> bool:
    """Check if a session is already created for today
    
    Return: One if the session already exists, Zero else
    """
    
    config = load_config(filename="database.ini", section='PostgreSQL')
    with connect(config) as conn:
        with conn.cursor() as cur:
            sqlVerif = f"""select count(1) from session
                            where date = {date.today()}"""
            
            cur.execute(sqlVerif)
            result = cur.fetchone()
            return result[0] == 1
            

        