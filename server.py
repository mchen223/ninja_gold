from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

#def reward(low,high,location):
#    if form.name=adventure:
#        session['reward'] = random.randint(low,high)
#        session['bank']+=session['reward']
#        activity.append('Earned ',session['reward'],' golds from the ,location,'!')
#    else
#        session['reward'] = random.randint(low,high)
#        session['bank']+=session['reward']
#        activity.append('Earned ',session['reward'],' golds from the ',location,'!')

def rewardtest():
    session['reward'] = random.randint(low,high)
    session['bank']+=session['reward']
    activity.append('Earned ',session['reward'],' golds from the ',location,'!')

@app.route('/')
def index():
    session['bank']=0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    rewardtest(5,10,farm)
    return render_template('index.html')
    return redirect('/')

app.run(debug=True)
