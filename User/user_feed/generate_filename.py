import string
import random
from check_filename import check_filename

def filename():

    while True:

        name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 11))

        if not check_filename(name):
            return name 

        else:
            continue