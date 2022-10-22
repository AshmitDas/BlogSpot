from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from database.db import User, Media, Blog, engine

class Save:

    @staticmethod
    def to_media_db(filename, filetype, session_id):

        query_stmt = select(User.user_id).where(User.session_id == session_id)

        with Session(engine) as session:
            username = session.execute(query_stmt).fetchone()[0]


        query_stmt = insert(Media).values(filename = filename, user_id = username, filetype = filetype)
        with engine.connect() as conn:
            conn.execute(query_stmt)
            conn.commit()

    @staticmethod
    def to_blog_db(title, description, session_id):
        query_stmt = select(User.user_id).where(User.session_id == session_id)

        with Session(engine) as session:
            username = session.execute(query_stmt).fetchone()[0]


