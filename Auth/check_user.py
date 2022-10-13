from sqlalchemy import select
from sqlalchemy.orm import Session
from Auth.auth_db import User, engine


class Check:
    """Matches user provided credintials with the database."""

    @staticmethod
    def userid_exist(username):
        # checks if user provided user_id exists in the database

        query_stmt = select(User.user_id).where(User.user_id == username)

        with Session(engine) as session:
            try:
                session.execute(query_stmt).fetchone()[0]
                return True

            # if the user_id does not exist in the databse
            except TypeError:
                return False
    
    @staticmethod
    def password_matches(username, password):
        # checks if the password matches with the password in the database associated with the user_id

        query_stmt = select(User.password).where(User.user_id == username)

        with Session(engine) as session:
            user_password = session.execute(query_stmt).fetchone()[0]

            if user_password != password:
                return False
            
            else:
                return True
