from sqlalchemy import select, update
from sqlalchemy.orm import Session
from Auth.auth_db import User, engine
from secrets import token_urlsafe


class SessionID:

    @staticmethod
    def match_session_with_db(username, sessionID):
        
        query_stmt = select(User.session_id).where(User.user_id == username)

        with Session(engine) as session:
            try:
                result = session.execute(query_stmt).fetchone()[0]

                if result == sessionID:
                    return True

            except TypeError:
                return False

    @staticmethod
    def generate_sessionID():

        return token_urlsafe(32)


    @staticmethod
    def save_sessionID(username, sessionID):

        query_stmt = update(User).where(User.user_id == username).values(session_id = sessionID)

        with Session(engine) as session:
            session.execute(query_stmt)
            session.commit()

