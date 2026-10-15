"""Deploy the Watson emotion-detector application with Flask."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emotion_analyzer():
    """Analyze interface text and return scores or the required input error."""
    result = emotion_detector(request.args.get('textToAnalyze', ''))
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route('/')
def render_index_page():
    """Render the course-provided emotion-analysis interface."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
