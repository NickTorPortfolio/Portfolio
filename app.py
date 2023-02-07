from flask import Flask, render_template, request, url_for, redirect
#from markupsafe import escape
import mathfuncs


app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home():
    '''This route handles the main page of the app.'''
    docsurl = url_for("docs")
    if request.method == "POST":
        num=request.form.get("name")
        return redirect(num)
    return render_template("home.html", docsurl=docsurl)
    
    


@app.route("/docs")
def docs():
    '''This route handles the documentation of the app.'''
    homeurl = url_for("home")
    return render_template("documentation.html", homeurl=homeurl)


@app.route("/<int:N>")
def num(N):
    '''This route handles the numerical analysis reports.'''
    homeurl = url_for("home")
    docsurl = url_for("docs")
    result = mathfuncs.numerical_analysis(N)
    return render_template("analysis.html",
                           number=N,
                           homeurl=homeurl,
                           docsurl=docsurl,
                           **result)




if __name__ == '__main__':
    app.run()
