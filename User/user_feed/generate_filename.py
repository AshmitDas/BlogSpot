import string
import random
from User.user_feed.check_filename import check_filename

def generate_filename():

    while True:
        
        # generates a filename containing Uppercase, lowercase and digits of length 11
        name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 11))

        if not check_filename(name):
            return name 

        else:
            continue