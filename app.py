import streamlit as st
import google.generativeai as genai

# =========================
# PASTE YOUR API KEY HERE
# =========================
GEMINI_API_KEY = "AQ.Ab8RN6LlddCpgs9dokhaTFOA8HkSGZdDYZdowZZX0g8BJqjP6A"

genai.configure(api_key=GEMINI_API_KEY)

# Use a currently supported model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page Configuration
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# Header
st.title("🌍 AI Travel Planner")
st.markdown("Plan your perfect trip using AI")

# User Inputs
destination = st.text_input("📍 Destination")

days = st.slider(
    "🗓 Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

budget = st.selectbox(
    "💰 Budget",
    ["Low", "Medium", "High"]
)

travel_type = st.selectbox(
    "✈ Travel Type",
    ["Solo", "Family", "Adventure", "Romantic", "Business"]
)

interests = st.multiselect(
    "🎯 Interests",
    [
        "Beaches",
        "Mountains",
        "Food",
        "Shopping",
        "Historical Places",
        "Nature",
        "Nightlife",
        "Photography"
    ]
)

if st.button("🚀 Generate Travel Plan"):

    if not destination:
        st.warning("Please enter a destination.")
        st.stop()

    prompt = f"""
    Create a detailed travel itinerary.

    Destination: {destination}
    Duration: {days} days
    Budget: {budget}
    Travel Type: {travel_type}
    Interests: {', '.join(interests)}

    Include:
    1. Day-wise itinerary
    2. Top tourist attractions
    3. Recommended food
    4. Estimated budget
    5. Travel tips

    Format the answer neatly using markdown.
    """

    try:
        with st.spinner("Generating travel plan..."):
            response = model.generate_content(prompt)

        st.success("Travel Plan Generated Successfully!")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built with Streamlit + Gemini AI")
