from flask import Flask, render_template, redirect, url_for
from datetime import date

app = Flask(__name__)

# execute this command in the shell to clear the port: !kill -9 $(lsof -t -i:5000)
    
@app.route("/")
def home():
# you can acually use html tags in the return here
    current_date = date.today().strftime('%m/%d/%Y')
    return render_template("index.html", time = current_date)
     
        

if __name__ == "__main__":
    app.run(debug=True)