from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Major and minor keys
MAJORS = [
    "C","G","D","A","E","B",
    "F#/Gb","C#/Db","Ab","Eb","Bb","F"
]

MINORS = [
    "Am","Em","Bm","F#m/Gbm","C#m/Dbm","G#m",
    "D#m/Ebm","A#m/Bbm","Fm","Cm","Gm","Dm"
]

SCALES = {
    # Major scales
    "C": ["C","D","E","F","G","A","B"],
    "G": ["G","A","B","C","D","E","F#"],
    "D": ["D","E","F#","G","A","B","C#"],
    "A": ["A","B","C#","D","E","F#","G#"],
    "E": ["E","F#","G#","A","B","C#","D#"],
    "B": ["B","C#","D#","E","F#","G#","A#"],
    "F#/Gb": ["F#","G#","A#","B","C#","D#","F"], 
    "C#/Db": ["Db","Eb","F","Gb","Ab","Bb","C"],
    "Ab": ["Ab","Bb","C","Db","Eb","F","G"],
    "Eb": ["Eb","F","G","Ab","Bb","C","D"],
    "Bb": ["Bb","C","D","Eb","F","G","A"],
    "F": ["F","G","A","Bb","C","D","E"],

    # Minor scales
    "Am": ["A","B","C","D","E","F","G"],
    "Em": ["E","F#","G","A","B","C","D"],
    "Bm": ["B","C#","D","E","F#","G","A"],
    "F#m/Gbm": ["F#","G#","A","B","C#","D","E"],
    "C#m/Dbm": ["Db","Eb","F","Gb","Ab","Bb","C"],
    "G#m": ["G#","A#","B","C#","D#","E","F#"],
    "D#m/Ebm": ["D#","F","F#","G#","A#","B","C#"], 
    "A#m/Bbm": ["A#","C","C#","D#","F","F#","G#"], 
    "Fm": ["F","G","Ab","Bb","C","Db","Eb"],
    "Cm": ["C","D","Eb","F","G","Ab","Bb"],
    "Gm": ["G","A","Bb","C","D","Eb","F"],
    "Dm": ["D","E","F","G","A","Bb","C"]
}

@app.route("/")
def index():
    return render_template("index.html", majors=MAJORS, minors=MINORS)

@app.route("/get_scale", methods=["POST"])
def get_scale():
    key = request.json.get("key")
    scale = SCALES.get(key)
    return jsonify(scale=scale)

if __name__ == "__main__":
    app.run(debug=True)
