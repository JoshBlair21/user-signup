from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome", methods=['GET'])
def welcome():
    return render_template("welcome.html")


@app.route("/", methods=['POST'])
def error():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    verify_error = ''
    pass_error = ''
    email_error = ''
    
    if ' ' in username or len(username) < 3 or len(username) > 20:
        user_error = "Enter a valid username"
        username = ''
        
    if ' ' in password or len(password) < 3 or len(password) > 20:
        pass_error = "Enter a valid password"
    
    if password != verify:
        verify_error = "Your passwords do not match"

    if '@' not in email or '.' not in email or len(email) < 3 or len(email) > 20:
        email_error = "Enter a valid email"
        email_error= ''

    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html')

    else:
        return render_template('index.html', email_error=email_error, verify_error=verify_error, pass_error=pass_error, user_error=user_error, username=username, password=password, verify=verify, email=email)

    
    

app.run()

