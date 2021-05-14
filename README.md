# zerodha-bhavcopy

access webapp from -> http://yashp-zerodha-bhavcopy.centralindia.cloudapp.azure.com/

## features

- Downloads the equity bhavcopy zip from BSE India every day at 18:00 IST for the current date
- Extracts and parses the CSV file in it.
- Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
- Renders a simple V̶̶̶u̶̶̶e̶̶̶J̶̶̶S̶̶̶ ̶f̶r̶o̶n̶t̶e̶n̶d̶ HTML/CSS/Bootstrap frontend with a search box that allows the stored entries to be searched by name and renders a table of results and optionally downloads the results as CSV
- The search performed on the backend using Redis

## FYI

- used HTML/CSS/Bootstrap for frontend instead of VueJS
- celery framework is used for background task to download bhavcopy everyday at 6pm
- webapp is deployed on *Microsoft Azure Cloud*

## Setup


- clone this repository by 
- ```bash
  git clone <repo link>
  ```
- Go to the project root directory
  ```bash
  cd zerodha-bhavcopy
  ```
- Create Virtualenv and activate it
  ```bash
  virtualenv ve 
  source ve/bin/activate
  ```
- Install dependency packages
  ```bash
  pip3 install -r requirements.txt
  ```
- Install redis-server
  ```bash
  sudo apt install redis-server
  ```
- run django makemigrations command
  ```bash
  python3 manage.py makemigrations
  ```
- run django migrate command
  ```bash
  python3 manage.py migrate
  ```
#### To run the server
-   ```bash
    python manage.py runserver
    ```
- configure celery beat and worker by refering this 
  https://medium.com/swlh/asynchronous-task-with-django-celery-redis-and-production-using-supervisor-ef920725da03
  
- access the webapp from http://127.0.0.1:8000/


### Contact for any difficulties accessing the webapp or related to setup

- email:- yashpatel7025@gmail.com
