# JiX
[![Build Status](https://travis-ci.com/jix-666/jix.svg?branch=master)](https://travis-ci.com/jix-666/jix)
[![codecov](https://codecov.io/gh/jix-666/jix/branch/master/graph/badge.svg)](https://codecov.io/gh/jix-666/jix)

JiX web application is a web forum for finding friends and people who have mutually-interested events. The activities are categorized into categories including Hangout, Meeting, Study, Entertainment, Travel, etc. Users can select the interesting category of activity on the Explore page. Moreover, they can find or post about any activity or event on the Feed page. The feed and explore page is visible to everyone on the internet (doesn’t have to log in), but web visitors have to login before post and participate in any event. The intended users are various from teenagers to working adults.

## Getting Started

|    Name    | Required version(s) |
| :--------: | :-----------------: |
|   Python   |   3.7 or higher     |
|   Django   |   3.1 or higher     |

1. Clone this repo to your computer.
    ```
    git clone https://github.com/jix-666/jix.git
    ```
2. Change directory to the repo.
    ```
    cd jix
    ```
3. Install virtualenv to your computer.
    ```
    pip install virtualenv
    ```
4. Create virtual environment.
    ```
    virtualenv jix_env
    ```
5. Activate virtualenv by using this command.
    ```
    source jix_env/bin/activate
    ```
6. To make sure the pip is up-to-date, install the lastest version of pip.
    ```
    jix_env/bin/python -m pip install --upgrade pip
    ```
7. Run this command to install all require packages.
    ``` 
    pip install -r requirements.txt
    ```
8. Create .env file inside jix (same level as settings.py) and added:
    ```
    DEBUG=True
    ```
9. Run this command to migrate the database.
    ```
    python manage.py migrate
    ```
10. Start running the server by this command.
    ```
    python manage.py runserver
    ```

## Project Documents

- [Project proposal](https://docs.google.com/document/d/1xFfaPgIMUXFGIeDvwk4D-pv7skU7g_7FcfdE7mvHmDA/edit)
- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Code Review Procedure](../../wiki/Code%20Procedure)
- [Code Checklist](../../wiki/Code%20Checklist)
### Iteration Plan
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)
- [Iteration 4 Plan](../../wiki/Iteration%204%20Plan)
- [Iteration 5 Plan](../../wiki/Iteration%205%20Plan)
- [Iteration 6 Plan](../../wiki/Iteration%206%20Plan)
