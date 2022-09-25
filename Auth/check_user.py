from sqlalchemy import select
from sqlalchemy.orm import Session
from Auth.auth_db import User, engine


class Check_Credintials:
    """Matches user provided credintials with the database."""

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def check_userid_exist(self):
        # checks if user provided user_id exists in the database

        query_stmt = select(User.user_id).where(User.user_id == self.username)

        with Session(engine) as session:
            try:
                session.execute(query_stmt).fetchone()[0]
                return True

            # if the user_id does not exist in the databse
            except TypeError:
                return False

    def check_password(self):
        # checks if the password matches with the password in the database associated with the user_id

        query_stmt = select(User.password).where(User.user_id == self.username)

        with Session(engine) as session:
            user_password = session.execute(query_stmt).fetchone()[0]

            if user_password != self.password:
                return False
            
            else:
                return True
