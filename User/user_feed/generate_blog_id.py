# from sqlalchemy import select
# from sqlalchemy.orm import Session
# from database.db import Blog, engine
# from secrets import token_hex

# def generate_blogID():
#     while True:

#         blog_id = token_hex(16)  # generates hexadecimal of 16 characters
#         query_stmt = select(Blog.blog_id).where(Blog.blog_id == blog_id)

#         # checks in the db if the generated hexadecimal character exists in the db or not
#         with Session(engine) as session:
#             try:
#                 session.execute(query_stmt).fetchone()[0]
#             except TypeError:
#                 return blog_id