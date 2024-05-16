from dotenv import load_dotenv
import os

load_dotenv()

pwd=os.environ['dylanpereyra12']
user=os.environ['postgres']
host=os.environ['localhost']
database=os.environ['DATABASE']
server=os.environ['SERVER']

DATABASE_CONNECTION=f'{server}://{user}:{pwd}@{host}/{database}'