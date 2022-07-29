1. cd into project folder
2. mkdir <file name>
3. pipenv install
4. pipenv install Flask PyMySQL bcrypt
5. pipenv shell
6. create a server.py file
7. copy paste this:

from flask_app import app

if __name__=="__main__":
    app.run(debug=True,port=5000)