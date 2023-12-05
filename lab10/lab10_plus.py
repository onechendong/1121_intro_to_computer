from flask import Flask, render_template, request
import json
app = Flask(__name__) #creat flask
data_on_server = {}

# 定義首頁路由
@app.route('/',methods=['GET'])
def home():
    return render_template('lab10_plus.html')

# 定義互動表單路由
@app.route('/set',methods=['POST'])
def form_():
    input1 = request.form ['store_name']
    input2 = request.form ['score']
    data_on_server [input1]= input2 
    current_data = data_on_server
    input_data = request.form.to_dict()
    print(f'\nuser input data : {input_data}\n')
    print(f'Data on server : {data_on_server}\n')
    return render_template('lab10_plus.html', **locals())
    

# 定義重置路由
@app.route('/reset/<yes_or_no>',methods=['GET'])
def reset(yes_or_no):
    if(yes_or_no == 'y'):
        data_on_server.clear()
        print(f'\nData on server : {data_on_server}\n')
        return render_template('reset.html')
    else:
        current_data = data_on_server
        return render_template('lab10_plus.html', **locals())
    
    
app.run(host="0.0.0.0", port=3000, debug=True)
