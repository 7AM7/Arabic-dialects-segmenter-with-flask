# Farasa Flask APP

# Installation
## Using pip
```
git clone https://github.com/ahmed451/SummerInternship2020-PyPIFarasa
cd SummerInternship2020-PyPIFarasa/7AM7/API
pip install -r requirements.txt
```
# Flask Steps
1- Create new Folder with any name:
```
$ mkdir app
```
2- Create new Virtual Environment
  ```
  $ virtualenv -p python3.6 venv
  $ source venv/bin/activate
  ```
For Deactivate use:
  ```
  $ deactivate venv
  ```
3- Install Flask Package
  ```
  $ pip install flask gunicorn
  ```
4- Create new python file with any name:
EX :
  ```
  $ touch app.py 
  ```

5-  Add simple flask code
EX :   
```
from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
    return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    app.run()
```
6-  Create `Requirements` file
```
$ pip freeze > requirements.txt
```
7- Create `Procfile` file
```
$ touch Procfile
```
and add this line
```
web: gunicorn app:app
```
8- Create `runtime.txt` file
```
$ touch runtime.txt
```
and add your python version 
EX:
```
python-3.6.6
```
9- Initialize an empty repo, add the files in the repo and commit all the changes using terminal.
```
$ git init 
$ git add .
$ git commit -m "Initial Commit"
```

# Heroku Steps
1-  Create new [Heroku](https://signup.heroku.com/) account.

2-  Install Heroku CLI [Heroku Download](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
  - Linux Ubuntu
  ```
  $ sudo snap install --classic heroku
  ```
  - Mac OSx
  ```
  $ brew tap heroku/brew && brew install heroku
  ```
  - Windows [Heroku Windows](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
  
3- Login to Heroku
```
$ heroku Login
```

4- Now, Create a unique name for your Web app.
```
$ heroku create FarasaAPI
```
5- Push your code from local to the heroku remote.
```
$ git push heroku master
```

Finally, web app will be deployed on http://FarasaAPI.herokuapp.com.

## NOTE: IF you want using `NLTK`Package with [Heroku](https://signup.heroku.com/) Please follow with following steps.
1- Create `nltk.txt` file
```
$ touch nltk.txt
```
2- Add Your Corpus name 
```
punkt
```
# Refeneces
- https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
- https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app
- https://www.tutorialspoint.com/flask/index.htm 
