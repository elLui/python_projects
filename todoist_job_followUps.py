#! python3

# todoist scheduling application :: https://todoist-python.readthedocs.io/en/latest/modules.html
import todoist



import datetime
import os
from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':


    get_api = os.getenv('api_key')
    api = todoist.TodoistAPI(get_api)
    api.sync()


    print(api.state['projects'])








