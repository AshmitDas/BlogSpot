from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from database.db import User, Media, Blog, engine
from User.user_feed.generate_blog_id import generate_blogID



def save_to_media_db(sessionID, filename = "", filetype = ""):

    username = fetch_userID(sessionID)

    query_stmt = insert(Media).values(filename = filename, user_id = username, filetype = filetype)
    with engine.connect() as conn:
        conn.execute(query_stmt)
        conn.commit()



def save_to_blog_db(title, description, sessionID, filename = "", filetype = ""):

    username = fetch_userID(sessionID)

    blog_id = generate_blogID()

    query_stmt = insert(Blog).values(blog_id = blog_id, user_id = username, title = title, description = description, filename = filename, filetype = filetype)
    with engine.connect() as conn:
        conn.execute(query_stmt)
        conn.commit()



def fetch_userID(sessionID):

    query_stmt = select(User.user_id).where(User.session_id == sessionID)

    with Session(engine) as session:
        return session.execute(query_stmt).fetchone()[0]