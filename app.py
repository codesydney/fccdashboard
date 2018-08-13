from flask import Flask, render_template, g, request, redirect, url_for, flash
import os, re, sqlite3
from flask_wtf import Form
from forms import InputForm, LoginForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

DATABASE = 'fccdashboard.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    fccamperslist = []

    try: 
        cur = db.execute('SELECT Name, Email, Password, A1, A2 from fccdashboardtable')
    except Exception as e:
        print('Exception: ',e)    
    res = cur.fetchall()

    for row in res:
        print(row)
        fccamperslist.append(row)

    return render_template('home.html',
                           fccamperslist=fccamperslist)

@app.route('/register', methods=['GET', 'POST'])
def register():
    registerform = RegisterForm() 
    error = None
    if request.method == 'POST':
        db = get_db()
        Email = registerform.RegisterEmail.data   
        NameList = re.findall('[^@]+', Email)
        Name = ''.join(NameList)
        Password = registerform.RegisterPassword.data
        try: 
            user_cur = db.execute('SELECT Name, Email, Password from fccdashboardtable where Email = ?', [Email])
        except Exception as e:
            print('Exception: ',e)    
        numRows = (len(user_cur.fetchall()))
        try: 
            user_cur = db.execute('SELECT Name, Email, Password from fccdashboardtable where Email = ?', [Email])
        except Exception as e:
            print('Exception: ',e)

        if numRows == 1:
            return render_template('register.html', error='Email already exists!')
        else:
            if Name != ' ':
                db.execute('INSERT into fccdashboardtable (Name, Email, Password, A1) values (?, ?, ?, ?)', [Name, Email, Password, 'Not yet started'])
                db.commit()                
        return redirect(url_for('index'))
    else:
        return render_template('register.html',
                                registerform=registerform)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm() 
    error = None
    if request.method == 'POST':
        db = get_db()
        Email = loginform.LoginEmail.data       
        #Name = re.findall('[^@]+', Email)
        #Password = loginform.LoginPassword.data
        try: 
            user_cur = db.execute('SELECT Name, Email, Password from fccdashboardtable where Email = ?', [Email])
        except Exception as e:
            print('Exception: ',e)    
        numRows = (len(user_cur.fetchall()))

        try: 
            user_cur = db.execute('SELECT Name, Email, Password from fccdashboardtable where Email = ?', [Email])
        except Exception as e:
            print('Exception: ',e)    

        if numRows == 1:
            res = user_cur.fetchall()
            for row in res:
                print(row[1])
                Name  = row[0]
                Email = row[1]
                Password = row[2]
                if Password == loginform.LoginPassword.data:
                    return redirect(url_for('index'))
                else:
                    error = 'The password is incorrect.'
        else:
            error = 'The username is incorrect'

        return render_template('login.html',
                                loginform=loginform,
                                error=error)
    else:
        return render_template('login.html',
                                loginform=loginform)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)