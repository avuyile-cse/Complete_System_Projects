
import  csv
import  os
import  hashlib
from datetime import datetime 
from flask import Flask, render_template, request, redirect, url_for


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

app =   Flask(__name__)

csv_file    = "users.csv"

def save_user(username, password, status):
    file_exist  = os.path.isfile(csv_file)

    current_datetime = datetime.now()

    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")

    with open(csv_file, mode="a", newline="") as dbfile:
        writer  = csv.DictWriter(dbfile,fieldnames=["username","password","date","time","status"])

        if not file_exist:
            writer.writeheader()
        writer.writerow(
                        {"username" : username, 
                        "password" :password, 
                        "date" : date,
                        "time" : time,
                        "status": status}
                        )

@app.route("/",methods=["GET"])
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def user_login():
    username	= request.form.get("username", "").strip()
    password	= request.form.get("password", "").strip()
    hashed_pw   = hash_password(password)

    if not username or not password:
        save_user(username,password, "loginFailed")
        return render_template("login.html", error= "Both fields are required.")

    save_user(username,hashed_pw, "LoginSuccess")
    return render_template ("login.html", success= f"User '{username}' logged in!")



if __name__ == "__main__":
    app.run(debug=True)
