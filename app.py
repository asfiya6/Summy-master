from __future__ import unicode_literals
from implib import get_text
from implib import readingTime
from flask import Flask, render_template, request
from sp_sum import summarize_sentiment

import time
import spacy

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    start = time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        final_reading_time = readingTime(rawtext)
        final_summary = summarize_sentiment(rawtext)
        summary_reading_time = readingTime(final_summary)
        end = time.time()
        final_time = end-start
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, final_time=final_time, final_reading_time=final_reading_time, summary_reading_time=summary_reading_time)


@app.route('/analyze_url', methods=['GET', 'POST'])
def analyze_url():
    start = time.time()
    if request.method == 'POST':
        raw_url = request.form['raw_url']
        rawtext = get_text(raw_url)
        final_reading_time = readingTime(rawtext)
        final_summary = summarize_sentiment(rawtext)
        summary_reading_time = readingTime(final_summary)
        end = time.time()
        final_time = end-start
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, final_time=final_time, final_reading_time=final_reading_time, summary_reading_time=summary_reading_time)


@app.route('/about')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
