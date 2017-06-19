from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

def reward():
    time = datetime.now().strftime('%m-%d-%Y %H:%M')
    name = request.form['action']
    if name == 'farm':
        reward = random.randint(10,20)
    elif name == 'cave':
        reward = random.randint(5,10)
    elif name == 'house':
        reward = random.randint(2,5)
    elif name == 'casino':
        reward = random.randint(-50,50)
    session['bank'] += reward
    session['activity'] += 'Earned '+ str(reward) + ' golds from the ' + str(name) + '! ' + '(' + time + ')' + '.\n'

@app.route('/')
def index():
    if not session.get('bank'):
        session['bank']=0
    if session['bank'] < 0:
        reset()
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process():
    reward()
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
