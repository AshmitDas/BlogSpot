from sqlalchemy import select
from sqlalchemy.orm import Session
from User.user_feed.user_db import Media, engine


def check_filename(self):
    query_stmt = select(Media.filename).where(Media.filename == self.filename)

    with Session(engine) as session:
        try:
            session.execute(query_stmt).fetchone()[0]
            return True

        # if the filename does not exist in the databse
        except TypeError:
            return False