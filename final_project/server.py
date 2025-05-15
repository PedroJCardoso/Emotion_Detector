"""This module will implement a server for emotion detections"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')


@app.route('/')
def index():
    """Renders the default page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    """Analyses the given text and returns the predominant emotion, alongside other scores"""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return 'Invalid text! Please try again!'
    return f"""For the given statement, the system response is 'anger':{response['anger']},
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},
    and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."""


if __name__ == '__main__':
    app.run(port=7999, host = '0.0.0.0')
