1. Install Dependencies
Install the required Python packages:
already provided in requirements.txt

2. Run the Application
Start the local Flask development server:

The application will be running at http://127.0.0.1:5000.

3. How to Use
Open your web browser and navigate to http://127.0.0.1:5000.

Type or paste the text you want to analyze into the text area.

Click the "Analyze Text" button.

The results will appear below, showing the overall Sentiment, Polarity score, and Subjectivity score.

4. How It Works
This application uses the TextBlob library to perform sentiment analysis.

Polarity: This is a floating-point number between [-1.0, 1.0].

> 0.1 is classified as Positive.

< -0.1 is classified as Negative.

Between -0.1 and 0.1 is classified as Neutral.

Subjectivity: This is a floating-point number between [0.0, 1.0].

0.0 is very objective (factual).

1.0 is very subjective (an opinion).
