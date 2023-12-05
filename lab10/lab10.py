from flask import Flask, render_template, request
import random
app = Flask(__name__) #creat flask

# 後端隨機選擇出拳function
def get_computer_choice():
    choices = ['r', 's', 'p']
    return random.choice(choices)

# 定義首頁路由
@app.route('/',methods=['GET'])
def home():
    return render_template('lab10.html')

# 定義互動表單路由
@app.route('/student_data',methods=['POST'])
def form_():
    string1 = request.form['string1']
    string2 = request.form['string2']
    print('\nname : '+string1+'\nstudent_id : '+string2+'\n')
    return 'ok'

# 定義猜拳路由
@app.route('/rsp',methods=['GET'])
def rsp():
    # 前端出拳
    user_choice = request.args.get('choice', '')
    # 後端出拳
    computer_choice = get_computer_choice()
    # 比賽
    if user_choice in ['r', 's', 'p']:
        print('\ncomputer : '+computer_choice+'  user : '+user_choice+'\n')
        if(user_choice == computer_choice):
            return 'It\'s Tie!'
        elif((user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r')):
            return 'You win!'
        else:
            return 'You lose!'
    else:
        return 'Wrong input! try again'
    
app.run(host="0.0.0.0", port=3000, debug=True)
