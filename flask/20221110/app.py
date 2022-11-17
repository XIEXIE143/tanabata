from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/touroku')
def touroku():
      return render_template('touroku.html')

@app.route('/touroku_app', methods=['POST'])
def touroku_app():

      id = request.form['id']
      pwd = request.form['pwd']
      
      return id+':'+pwd

@app.route('/radio')
def radio():
      return render_template('radio.html')

@app.route('/radio_app', methods=['POST'])
def radio_app():
      address = request.form['address']
      return address

  
@app.route('/select')
def select():
  	return render_template('select.html')
  
  
@app.route('/select_app', methods=['POST'])
def select_app():
  	favorite = request.form['favorite']
  	return favorite

@app.route('/textarea')
def textarea():
  	return render_template('textarea.html')
  
  
@app.route('/textarea_app', methods=['POST'])
def textarea_app():
  	date = request.form['data']
  	return date

@app.route('/input')
def inputa():
  	return render_template('input.html')
  
  
@app.route('/input_app', methods=['POST'])
def input_app():
  id= request.form('id')
  pwd = request.form('pwd')
  ad = request.form('ad')
  fvt = request.form('fvt')

  file=open('date.txt','a') 

  file.write(id + '\n')
  file.write(pwd + '\n')
  file.write(ad + '\n')
  file.write(fvt + '\n')
  
  return 'ALOHA!'
  
  file.close()

if __name__=='__main__':
      app.run(debug=True)
