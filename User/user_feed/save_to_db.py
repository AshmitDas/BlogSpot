from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from database.db import User, Media, Blog, engine


def save_to_media_db(filename, filetype, session_id):

    username = fetch_userID(session_id)

    query_stmt = insert(Media).values(filename = filename, user_id = username, filetype = filetype)
    with engine.connect() as conn:
        conn.execute(query_stmt)
        conn.commit()

# def save_to_blog_db(title, description, session_id):
#     username = fetch_userID(session_id)


def fetch_userID(sessionID):

    query_stmt = select(User.user_id).where(User.session_id == sessionID)

    with Session(engine) as session:
        return session.execute(query_stmt).fetchone()[0]