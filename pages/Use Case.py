import streamlit as st
import matplotlib.image as mpimg

st.header("Actor Star Power Impact & Optimal Release Timing in Film and Television")

st.subheader("Business Objectives:")

st.caption("From a Production House/Producer Perspective:")

st.markdown(""" - Identifying the most suitable actors for specific content based on attributes like star power, genre compatibility, and market influence.  

- Evaluating actors' historical success percentages by genre to make informed casting decisions. \

- Determining the optimal timing for content release, such as on an actor's birthday or during holiday seasons, to maximize audience engagement.
""")

st.caption("From an OTT Management Perspective:")

st.markdown(""" - Optimizing content selection to satisfy existing subscribers and attract new ones by comparing different actors' appeal and performance.

- Enhancing content strategy by launching shows that align with subscriber preferences and market trends.

- Increasing subscriber retention and acquisition through well-informed content decisions.

""")


st.subheader("Dimensions :")


st.markdown(""" • No. of Awards won

• Media and Magazines review

• Audience Popularity & Rating Summary

• Media polls and opinions

• Twitter audience review

• Weighted average

• Movie Success

• Box Office Success

• Same character portrayal

• Box office success

• Social media presence and followers

• Success factors

• Actors performance analysis

• Good acting vs bad acting

• Actors performance accuracy

• Magnitude of actors Star Power to influence success of a movie
""")



st.subheader("Find out:")

st.markdown("""
- Success factors of the actors on multiple criterion based on historical data

- Calculate Star Power of the actors (-/100) to influence success of a show

- Find success percentage of those actors w.r.t different genres

         ROI: 

          -- Best time to launch the shows of two different lead actors


      Future Prospect:  

          -- Which OTT platform to launch the shows (where the actors have been more successful)

          -- Predict viewership of those shows using ML predictive analytics and metadata present
""")


st.subheader("Architecture:")

arch = mpimg.imread('images/GenAI-architecture.png')
st.image(arch, width=900)


