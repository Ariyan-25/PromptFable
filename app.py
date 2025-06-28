from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from utils.storygen import generate_story

app = Flask(__name__)
app.config['DATABASE'] = os.path.join('instance', 'storyteller.db')

# Ensure the instance folder exists
os.makedirs(os.path.dirname(app.config['DATABASE']), exist_ok=True)

def init_db():
    with sqlite3.connect(app.config['DATABASE']) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS stories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        prompt TEXT NOT NULL,
                        story TEXT NOT NULL
                    )''')
        conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    if not prompt:
        return redirect(url_for('index'))

    story = generate_story(prompt)

    with sqlite3.connect(app.config['DATABASE']) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO stories (prompt, story) VALUES (?, ?)", (prompt, story))
        conn.commit()

    return render_template('index.html', prompt=prompt, story=story)

@app.route('/history')
def history():
    with sqlite3.connect(app.config['DATABASE']) as conn:
        c = conn.cursor()
        c.execute("SELECT id, prompt, story FROM stories ORDER BY id DESC")
        rows = c.fetchall()
    return render_template('history.html', stories=rows)

@app.route('/clear_history', methods=['POST'])
def clear_history():
    with sqlite3.connect(app.config['DATABASE']) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM stories")
        conn.commit()
    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)
