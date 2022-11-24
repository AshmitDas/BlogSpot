from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from database.db import User, Blog, engine


def save_to_blog_db(title, description, sessionID, filename = "", filetype = ""):

    username = fetch_userID(sessionID)

    query_stmt = insert(Blog).values(user_id = username, title = title, description = description, filename = filename, filetype = filetype)
    with engine.connect() as conn:
        conn.execute(query_stmt)
        conn.commit()



def fetch_userID(sessionID):

    query_stmt = select(User.user_id).where(User.session_id == sessionID)

    with Session(engine) as session:
        return session.execute(query_stmt).fetchone()[0]