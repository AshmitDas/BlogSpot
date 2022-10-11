from sqlalchemy import select
from sqlalchemy.orm import Session
from Auth.auth_db import User, engine


def match_session_with_db(username, sessionID):
    
    query_stmt = select(User.session_id).where(User.user_id == username)

    with Session(engine) as session:
        try:
           result = session.execute(query_stmt).fetchone()[0]

           if result == sessionID:
            return True

        except TypeError:
            return False