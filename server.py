"""
Flask web application for detecting emotions in text.

This app renders an index page where the user can enter text,
and then it calls the emotion detection function to analyze the emotions
expressed in that text.

"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create a Flask app instance
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Route to render the homepage.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Route to analyze the emotions in the user's input text.

    Returns:
        str: A message containing emotion scores or an error message.
    """
    # Retrieve the text from the URL parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function to analyze the text
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dominant = response["dominant_emotion"]

    # If the dominant emotion is None, it means the input was invalid
    if dominant is None:
        return "Invalid text! Please try again!"

    # Return the formatted result
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    # Run the Flask application in debug mode on port 5005
    app.run(port=5005, debug=True)
