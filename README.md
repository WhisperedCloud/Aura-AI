Aura AI ✨
A Streamlit-based web application designed to provide a safe and reflective space for users to check in with their emotions.
Aura AI analyzes the sentiment and subjectivity of user input to generate a personalized "Aura" and provide helpful recommendations to support mental well-being.

Features
Sentiment Analysis: Uses the TextBlob library to analyze the sentiment (positivity/negativity) and subjectivity (opinion vs. fact) of user input.
Personalized Aura: Translates sentiment scores into an emotional "Aura" with an emoji and a descriptive label.
Helpful Recommendations: Provides actionable suggestions based on the user's current emotional state.
Interactive Interface: Built with Streamlit for an intuitive and user-friendly experience.
AI Insights: Displays the raw sentiment and subjectivity scores for transparency.
How It Works
User Input: The user writes their thoughts and feelings into a text box.
Analysis: The app analyzes the input using TextBlob to calculate:
Sentiment Score: Indicates how positive or negative the text is.
Subjectivity Score: Indicates how much of the text is opinion-based versus fact-based.
Aura Generation: Based on these scores, the app generates:
An emotional "Aura" (e.g., 🌟 Radiant and Joyful, 😔 Subdued and Reflective).
A recommendation tailored to the user's emotional state.
Results Display: The app clearly displays the generated Aura, the personalized recommendation, and the underlying AI scores.
Installation
To run this project locally, please follow these steps.
Clone the repository:
code
Bash
git clone https://github.com/your-username/aura-ai.git
cd aura-ai
Install dependencies:
Make sure you have Python 3.7+ installed. Then, install the required libraries.
code
Bash
pip install -r requirements.txt
(Note: If you don't have a requirements.txt file, you can install them manually: pip install streamlit textblob)
Download TextBlob Corpora:
The first time you run the app, you'll need to download the necessary NLTK corpora for TextBlob.
code
Bash
python -m textblob.download_corpora
Run the app:
code
Bash
streamlit run app.py
Open the app in your browser at http://localhost:8501.
Usage
Launch the application and read the introduction to understand its purpose.
Write your current thoughts and feelings in the "What's on your mind today?" text box.
Click the "Analyze My Aura" button.
View your personalized Aura, the tailored recommendation, and the AI scores in the expandable section.
Example
Input:
code
Code
"I'm feeling a bit stressed about my project, but I'm also excited for the weekend."
Output:
Aura: 😊 Calm and Positive
Recommendation: "You're in a great, steady headspace. Let's maintain this positive momentum. A quick 5-minute focus game could be both enjoyable and beneficial."
AI Scores:
Sentiment Score: 0.25
Subjectivity Score: 0.60
