import streamlit as st
import google.generativeai as genai

# Read API key from Streamlit Secrets
api_key = "AQ.Ab8RN6JPbuIGmk6Xs9Dr0qUeJAfQq9QIvO12x2G9R3Jv7Bafpg"

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# Page Configuration
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# Header
st.title("🌍 AI Travel Planner")
st.markdown("### Plan your dream trip with AI")

# User Inputs
destination = st.text_input("📍 Enter Destination")

days = st.slider(
    "🗓 Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

budget = st.selectbox(
    "💰 Select Budget",
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
        "Nature",
        "Food",
        "Shopping",
        "Historical Places",
        "Nightlife",
        "Photography"
    ]
)

# Generate Plan
if st.button("🚀 Generate Travel Plan"):

    if not destination:
        st.warning("Please enter a destination.")
    else:

        prompt = f"""
        Create a professional travel itinerary.

        Destination: {destination}
        Duration: {days} days
        Budget: {budget}
        Travel Type: {travel_type}
        Interests: {', '.join(interests)}

        Include:
        1. Day-wise itinerary
        2. Recommended attractions
        3. Food recommendations
        4. Estimated budget
        5. Travel tips

        Format with headings and bullet points.
        """

        with st.spinner("Generating AI Travel Plan..."):

            response = model.generate_content(prompt)

            st.success("Travel Plan Generated Successfully!")

            st.markdown(response.text)

# Footer
st.markdown("---")
st.caption("AI Travel Planner | Streamlit + Gemini AI")
