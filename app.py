import streamlit as st
from textblob import TextBlob
import time

# --- The AI Engine (Class Definition) ---
class CognitiveEmpathyEngineLite:
    """
    A simplified version of the AI model that analyzes text sentiment.
    """
    def analyze_check_in(self, text):
        analysis = TextBlob(text)
        sentiment_score = analysis.sentiment.polarity
        subjectivity_score = analysis.sentiment.subjectivity
        return sentiment_score, subjectivity_score

    def generate_aura_and_recommendation(self, sentiment, subjectivity):
        """
        Translates the raw scores into a user-friendly "Aura" and recommendation.
        """
        if sentiment > 0.6 and subjectivity > 0.5:
            aura = "🌟 Radiant and Joyful"
            recommendation = "Your energy is wonderfully high! It's a perfect time to harness this positivity. Consider tackling a creative project or sharing your good vibes with someone."
        elif sentiment < -0.5:
            aura = "☁️ Cloudy and Heavy"
            recommendation = "I sense some significant stress in your words. Please be gentle with yourself. A short, 3-minute guided breathing exercise could help ground you right now."
        elif sentiment < -0.1 and subjectivity > 0.7:
             aura = "🤔 Anxious and Overthinking"
             recommendation = "It seems like a lot is on your mind, and the thoughts might be spinning. A 'brain dump' journaling session could be very effective. Just write everything down without judgment."
        elif sentiment > 0.2:
            aura = "😊 Calm and Positive"
            recommendation = "You're in a great, steady headspace. Let's maintain this positive momentum. A quick 5-minute focus game could be both enjoyable and beneficial."
        elif sentiment < -0.1:
            aura = "😔 Subdued and Reflective"
            recommendation = "It sounds like you're feeling a bit down. That's completely okay. Maybe some gentle activity, like listening to a favorite calm song or a short walk, would feel comforting."
        else:
            aura = "🧘 Balanced and Centered"
            recommendation = "You seem to be in a state of equilibrium. This is a great foundation. Let's reinforce it with a simple mindfulness exercise to appreciate the present moment."
            
        return aura, recommendation

# --- The Streamlit App Interface ---

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# FIX: This line was missing. It creates the AI engine object.
ai_engine = CognitiveEmpathyEngineLite()
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

st.set_page_config(page_title="Aura AI", page_icon="✨")

# --- App Header ---
st.title("Aura AI ✨")
st.markdown("_A personalized companion for mental well-being._")

# --- App Introduction ---
st.markdown("""
Welcome to Aura. This is a space for quiet self-reflection. 

The idea is simple: provide a safe place for you to express your thoughts and feelings without judgment. 
Our AI will then gently analyze the underlying sentiment of your words to reflect your current emotional 'Aura' back to you, along with a simple, helpful recommendation.

**Whenever you're ready, share your thoughts below.**
""")
st.markdown("---") # Visual separator

# --- User Input Section ---
st.header("Your Daily Check-in")

user_journal = st.text_area(
    "What's on your mind today?", 
    height=150, 
    placeholder="For example: I'm feeling a bit stressed about my project, but I'm also excited for the weekend..."
)

# --- Analysis Trigger ---
if st.button("Analyze My Aura"):
    if user_journal:
        with st.spinner("Analyzing your energy..."):
            time.sleep(1)
            # Now the 'ai_engine' variable exists and this line will work
            sentiment, subjectivity = ai_engine.analyze_check_in(user_journal)
            aura, recommendation = ai_engine.generate_aura_and_recommendation(sentiment, subjectivity)

        # --- Display the Results ---
        st.header("Here is your Aura for the moment:")
        col1, col2 = st.columns([1, 4])
        
        with col1:
            aura_emoji = aura.split(' ')[0]
            st.write(f"<p style='font-size: 80px; text-align: center;'>{aura_emoji}</p>", unsafe_allow_html=True)
        
        with col2:
            st.subheader(aura)
            st.info(f"**Recommendation:** {recommendation}")

        with st.expander("See the AI scores"):
            st.write(f"**Sentiment Score:** {sentiment:.2f} (How positive/negative the text is)")
            st.write(f"**Subjectivity Score:** {subjectivity:.2f} (How much of an opinion vs. a fact it is)")
    else:
        st.warning("Please write something in the check-in box before analyzing.")

# --- Footer ---
st.markdown("---")
st.markdown("_Disclaimer: This is a prototype for demonstration purposes and not a medical tool._")