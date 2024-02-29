from flask import Flask, render_template, jsonify

app = Flask(__name__)

excs = [
    {
        "title": "moutain climbers",
        "targets": ["core"],
        "description":
        "get down in a push up position and bring feet next to your hands, one at a time",
        "image_src": "TODO-add excercise image url"
    },
    {
        "title": "deadlift",
        "targets": ["core", "glutes", "hamstrings"],
        "description":
        "get down in a push up position and bring feet next to your hands, one at a time",
        "image_src": "TODO-add excercise image url"
    },
    {
        "title": "bench press",
        "targets": ["chest", "triceps"],
        "description":
        "get down in a push up position and bring feet next to your hands, one at a time",
        "image_src": "TODO-add excercise image url"
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', exc=excs, client="Anirudh")

@app.route('/excercises')
def list_exc():
  return jsonify(excs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
