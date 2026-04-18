from flask import Flask, render_template,request, redirect
import csv
import os

app         = Flask (__name__)
csv_file    = "users.csv" 

# check and create if file does not exist
if not os.path.exists(csv_file):
    with open(csv_file, "w",newline="") as file:
        writer  = csv.writer(file,quoting = csv.QUOTE_ALL)
        writer.writerow(["username","password"])

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login",methods=["POST"])
def login():
    username    = request.form.get("username")
    password    = request.form.get("password")

    with open(csv_file,"a", newline ="") as file:
        writer  = csv.writer(file)
        writer.writerow([username,password])

    return redirect("/users")

@app.route("/users")

def users():
    print("Users method/n")
    user_list   = []

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader) 

        for row in reader:
            user_list.append(row)
    return render_template("success.html", users = user_list)



if __name__ == "__main__":
    app.run(debug=True)
