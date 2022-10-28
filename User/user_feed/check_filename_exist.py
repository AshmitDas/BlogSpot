from sqlalchemy import select
from sqlalchemy.orm import Session
from database.db import Media, engine


def check_filename(filename):
    query_stmt = select(Media.filename).where(Media.filename == filename)

    with Session(engine) as session:
        try:
            session.execute(query_stmt).fetchone()[0]
            return True

        # if the filename does not exist in the databse
        except TypeError:
            return False