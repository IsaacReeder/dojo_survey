from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])
def create_user():
    print(request.form)
   
    print('name', request.form['name'])
    name=request.form['name']
    print('email', request.form['email'])
    email=request.form['email']
    return render_template('dojo_survey_result.html', name2=name, email=email)


if __name__=="__main__":
    app.run(debug=True) 
