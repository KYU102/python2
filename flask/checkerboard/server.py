from flask import Flask, render_template

app = Flask(__name__)



@app.route('/play')
def lvl1(row=8, col=8, color1='red', color2='black'):
    return render_template("index.html", row=8, col=8, color1='red', color2='black')

@app.route('/play/<int:col>')
def lvl2(col, row=8):
    return render_template("index.html",row=8, col=col)

@app.route('/play/<int:col>/<int:row>')
def lvl3(col, row):
    return render_template("index.html",row=row, col=col)

@app.route('/play/<int:col>/<int:row>/<string:color1>/<string:color2>')
def lvl4(col, row, color1, color2):
    return render_template("index.html",row=row, col=col, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True,port=5003)
