from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup.html')


@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    
    #error1 - The user leaves any of the following fields empty: username, password, verify password.
    if username == '':
        username_error = "That's not a valid username"

    if password == '':
        password_error = "That's not a valid password"

    if verify == '':
        verify_password_error = "Passwords do not match"

    #error2 - The user's username or password is not valid -- for example, it contains a space character
    if ' ' in username:
        username_error = "That's not a valid username"

    if ' ' in password:
        password_error = "That's not a valid password"

    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"

    if len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"

    #error3 - The user's password and password-confirmation do not match.
    if password != verify:
        verify_password_error = "Passwords do not match"

    #error4 - The user provides an email, but it's not a valid email. 
    # Note: the email field may be left empty, but if there is content in it, then it must be validated. 
    # The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    if email:
        if len(email) < 3 or len(email) > 20:
            email_error = "That's not a valid email"

        if ' ' in email or '@' not in email or '.' not in email:
            email_error = "That's not a valid email"

    #no errors
    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('signup.html',
        username=username,
        username_error=username_error,
        password=password,
        password_error=password_error,
        verify=verify,
        verify_password_error=verify_password_error,
        email=email,
        email_error=email_error)


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()