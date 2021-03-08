from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/loginform',methods=['GET','POST'])
def login():
	return render_template("login.html")
	
@app.route('/newacc',methods=['GET','POST'])
def fillform():
	log1=request.form.get('name')
	log2=request.form.get('pass')
	return render_template("form.html")
	
@app.route('/newacc1',methods=['GET','POST'])
def fillform2():
	log1=request.form.get('name')
	log2=request.form.get('pass')
	return render_template("form.html")
	
app.run(debug=True)