from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

def createPlot():
   t = np.linspace(0,2*np.pi,1000)
   y = np.sin(t)
   figfile = StringIO()
   plt.figure(figsize=(6*(1+np.sqrt(5))/2,6))
   plt.xlabel("t")
   plt.ylabel(r"$\sin(t)$")
   plt.plot(t, y, "r-")
   plt.savefig(figfile, format="svg")
   figfile.seek(0)
   return figfile.getvalue()


app = Flask(__name__)

@app.route("/")
def hello():
   return render_template("view.html", result = createPlot())

if __name__ == "__main__":
   app.run(debug=True)
