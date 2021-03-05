from flask import Flask, render_template, url_for, request, redirect

from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        f = open('words.txt', 'r')
        words = []
        for i in f.read().split():
            if len(i) == len(task_content):
                words.append(i)
                if len(words) > 2:
                    length = str(len(i))
                    return render_template("index.html", tasks=words, length=length)

        try:
            return redirect('/')

        except:
            return redirect('/')

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
