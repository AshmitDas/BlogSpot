from sqlalchemy import select, update
from sqlalchemy.orm import Session
from database.db import User, Media, engine
from secrets import token_urlsafe


class SessionID:

    @staticmethod
    def match_with_db(username, sessionID):
        
        query_stmt = select(User.session_id).where(User.user_id == username)

        with Session(engine) as session:
            try:
                result = session.execute(query_stmt).fetchone()[0]

                if result == sessionID:
                    return True

            except TypeError:
                return False

    @staticmethod
    def generate():

        while True:

            token = token_urlsafe(32)

            query_stmt = select(User.session_id).where(User.session_id == token)

            with Session(engine) as session:
                try:
                    session.execute(query_stmt).fetchone()[0]
                    continue

                except TypeError:
                    return token




    @staticmethod
    def save(username, sessionID):

        query_stmt = update(User).where(User.user_id == username).values(session_id = sessionID)

        with Session(engine) as session:
            session.execute(query_stmt)
            print("hello")
            session.commit()

