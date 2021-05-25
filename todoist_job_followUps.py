#! python3

# todoist scheduling application :: https://todoist-python.readthedocs.io/en/latest/modules.html
import pprint
import requests
import todoist

# imports to handle grabbing api key from .gitignore file
import os
from dotenv import load_dotenv

load_dotenv()

import datetime


def update():
    api.sync()


if __name__ == '__main__':

    # grab api_key from environment variable
    get_api = os.getenv('api_key')
    # transform api with todoist library
    api = todoist.TodoistAPI(get_api)
    # get current todoist data

    # to test functionality - will grab all projects and print to console
    ##########################################################################################################
    # # console log raw current projects
    # pprint.pprint(api.state['projects'])
    #
    # # for project in api.state['projects']:
    # #     update()
    # #     print(project['name'])





