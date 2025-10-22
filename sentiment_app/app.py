from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for the web page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables
    text = ""
    sentiment = "Neutral"
    polarity = 0
    subjectivity = 0

    # This block executes when the user submits the form
    if request.method == 'POST':
        text = request.form.get('text_input')
        
        if text:
            # Create a TextBlob object
            blob = TextBlob(text)
            
            # Get the polarity and subjectivity scores
            polarity = round(blob.sentiment.polarity, 4)
            subjectivity = round(blob.sentiment.subjectivity, 4)
            
            # Classify the sentiment
            if polarity > 0.1:  # Using 0.1 as a threshold for positive
                sentiment = "Positive"
            elif polarity < -0.1: # Using -0.1 as a threshold for negative
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

    # Render the HTML template, passing in the variables
    return render_template('index.html', 
                           text=text, 
                           sentiment=sentiment, 
                           polarity=polarity, 
                           subjectivity=subjectivity)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)