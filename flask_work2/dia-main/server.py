from flask import Flask,render_template,request
import dia

app = Flask(__name__)

@app.route("/",methods=['Get','POST'])
def index():
    당뇨여부 = '데이터를 넣으세요.'
    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""
    h = ""
    age = ""
    if request.method=='POST':
        esti = dia.getModel()
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        e = request.form['e']
        f = request.form['f']
        h = request.form['h']
        age = request.form['age']

        당뇨여부 = esti.predict([[a, b, c, d, e, f, h, age]])
        if 당뇨여부[0] == 1:
            당뇨여부 = '죄송합니다. 당뇨병에 걸리셨습니다.'
        else:
            당뇨여부 = '축하합니다. 당뇨병이 아닙니다.'
        # 당뇨여부 = esti.predict([[1.0,89,66,23,94,28.1,0.2,21]])
    return render_template("index.html",당뇨여부=당뇨여부,a=a,b=b,c=c,d=d,e=e,f=f,h=h,age=age)

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/pregnancy")
def graph():
    return render_template("pregnancy.html")


app.run(debug=True,host="0.0.0.0",port=5000)