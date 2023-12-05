import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

st.set_page_config(page_title='Actor Comparison',  page_icon="🎬", layout="wide")
# Data

# Define icons
icon_award = "🏆"
icon_tweet = "🐦"
icon_review = "📝"
icon_opinion = "💬"
icon_poll = "📊"
icon_good = "👍"
icon_bad = "👎"
icon_accuracy = "📏"
icon_star = "⭐"

## Functions start here

def get_actor_1_poster():
    
    al_pacino_poster = mpimg.imread('Al Pacino.png')
    st.image(al_pacino_poster, width=200)

    
def get_actor_2_poster():
    
    robert_di_niro_poster = mpimg.imread('Robert Di Niro.png')
    st.image(robert_di_niro_poster, width=235)
    
    
def fetch_movie_poster(movie_name):
    movies = pd.read_pickle('models/movies.pkl')
    if (movie_name in movies['title'].unique()):
        movie_id = movies.iloc[movie_index].id
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?" \
          "api_key=433ff6eeee0036e8693c029787f184c5&language=en-US"
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    st.image(full_path, width=235)

def display_icon(factor):
        icons = {
            "Iconic Roles": "🌟",
            "Academy Awards": "🏆",
            "Golden Globe Awards": "🌍",
            "Screen Actors Guild Awards": "🎭",
            "Emmy Awards": "📺",
            "Net Worth": "💰",
        }
        return icons.get(factor, "")


def create_horizontal_bar_chart(data, title, x_label, y_labels, colors):
    fig = go.Figure(data=go.Bar(
        x=data,
        y=y_labels,
        orientation='h',
        marker=dict(color=colors)
    ))

    fig.update_layout(
        title=title,
        xaxis=dict(title=x_label),
        yaxis=dict(autorange="reversed"),
        height=400
    )  

    return fig
   
def display_actor_info(actor_data):
    for opinion in actor_data:
        print("Opinion", opinion['source'])
        if(opinion['source'] == 'IMDb'):
            st.image(mpimg.imread('images/IMDB.png'), width=60)
        elif(opinion['source'] == 'Rotten Tomatoes'):
            st.image(mpimg.imread('images/Rotten Tomatoes.png'), width=100)
        elif(opinion['source'] == 'Variety'):
            st.image(mpimg.imread('images/Variety.png'), width=100)
        elif(opinion['source'] == 'The Guardian'):
            st.image(mpimg.imread('images/The Guardian.png'), width=100) 
        else:
            st.image(mpimg.imread('images/Rolling Stone.png'), width=140)
        #st.subheader(opinion['source'])
        st.write(opinion['text'])
        sentiment = opinion['sentiment']
        if sentiment == 'positive':
            st.markdown('<span style="color:green;font-weight:bold">Positive</span>', unsafe_allow_html=True)
        elif sentiment == 'negative':
            st.markdown('<span style="color:red;font-weight:bold">Negative</span>', unsafe_allow_html=True)
        st.markdown("---")
            
   
    # Function to display icons
# def display_icon(icon_name):
#     st.markdown(f'<i class="icon-{icon_name}"></i>', unsafe_allow_html=True)

# Function to display comparative analysis
def display_tweets(name, tweets):
    #st.write(f"## {name}")
    if(name == 'Al Pacino'):
        get_actor_1_poster()
    else:
        get_actor_2_poster()
    for handle, tweet in tweets.items():
        st.write(f"- 🐤{handle}: {tweet}")

# Function to display overall sentiment
def display_sentiment(name, sentiment):
    st.write(f"Overall Sentiment")
    st.write(sentiment)

# Function to display weighted average
def display_weighted_average(data):
    st.write("## Weighted Average")
    for name, score in data.items():
        st.write(f"- {name}: {score}")
        
def display_movie_reviews(actor_data):
        for movie in actor_data["movies"]:
            st.subheader(movie["name"])
            st.text("Type: " + movie["type"])

            st.subheader("Positive Reviews:")
            for review in movie["reviews"]["positive"]:
                st.success(review)

            st.subheader("Negative Reviews:")
            for review in movie["reviews"]["negative"]:
                st.error(review)

            st.markdown("---")

def display_actor_factors(actor_data):
    factors = actor_data["factors"]
    st.subheader("Factors:")
    for factor, value in factors.items():
        st.text(factor + ": " + str(value))

def display_social_media(actor_data):
    if "social_media_presence_and_followers_list" in actor_data:
        social_media = actor_data["social_media_presence_and_followers_list"]
        st.subheader("Social Media Presence:")
        for platform, followers in social_media.items():
            if platform != "Total Followers":
                st.text(platform + ": " + str(followers))

        st.text("Total Followers: " + str(social_media.get("Total Followers", 0)))
    else:
        st.warning("Social media data not available for this actor.")
        
        
def display_comparison():
    data = {
        "awards_list": {
            "Al Pacino": [
                {"award": "Academy Award for Best Actor", "movie": "Scent of a Woman", "result": "Won"},
                {"award": "Golden Globe Award for Best Actor – Motion Picture Drama", "movie": "Scent of a Woman", "result": "Won"},
                {"award": "Primetime Emmy Award for Outstanding Lead Actor in a Miniseries or a Movie", "movie": "Angels in America", "result": "Won"},
                {"award": "Golden Globe Award for Best Actor – Miniseries or Television Film", "movie": "Angels in America", "result": "Won"},
                {"award": "Screen Actors Guild Award for Outstanding Performance by a Male Actor in a Leading Role", "movie": "The Irishman", "result": "Nominated"}
            ],
            "Robert Di Niro": [
                {"award": "Academy Award for Best Actor", "movie": "Raging Bull", "result": "Won"},
                {"award": "Academy Award for Best Supporting Actor", "movie": "The Godfather Part II", "result": "Won"},
                {"award": "Golden Globe Award for Best Actor – Motion Picture Drama", "movie": "Raging Bull", "result": "Won"},
                {"award": "Golden Globe Award for Best Supporting Actor – Motion Picture", "movie": "The Godfather Part II", "result": "Won"},
                {"award": "Screen Actors Guild Award for Outstanding Performance by a Cast in a Motion Picture", "movie": "American Hustle", "result": "Nominated"}
            ]
        },
         "media_reviews_list": {
            "Al Pacino": {
                "The Godfather": {"review": "The Godfather is a masterpiece of cinema, and Al Pacino's performance as Michael Corleone is one of the greatest in film history.", "media_source": "The New York Times", "sentiment": "Positive"},
                "Scent of a Woman": {"review": "Al Pacino gives a tour-de-force performance as a blind retired Army officer in Scent of a Woman.", "media_source": "Rolling Stone", "sentiment": "Positive"},
                "The Irishman": {"review": "Al Pacino is a standout in The Irishman, bringing his trademark intensity to the role of Jimmy Hoffa.", "media_source": "Variety", "sentiment": "Positive"},
                "Overall Sentiment": "Positive",
                "Audience Rating Summary": {"Positive": "80%", "Neutral": "10%", "Negative": "10%"}
            },
            "Robert Di Niro": {
                "Taxi Driver": {"review": "Robert Di Niro delivers a haunting performance as Travis Bickle in Taxi Driver.", "media_source": "The Guardian", "sentiment": "Positive"},
                "Raging Bull": {"review": "Robert Di Niro's portrayal of boxer Jake LaMotta in Raging Bull is a tour-de-force of acting.", "media_source": "The New Yorker", "sentiment": "Positive"},
                "The Irishman": {"review": "Robert Di Niro reunites with Martin Scorsese for The Irishman, and delivers another great performance.", "media_source": "The Hollywood Reporter", "sentiment": "Positive"},
                "Overall Sentiment": "Positive",
                "Audience Rating Summary": {"Positive": "75%", "Neutral": "15%", "Negative": "10%"}
            },
            "Winner": "Robert Di Niro",
            "Factors where Robert Di Niro surpassed Al Pacino": [
                "More Academy Awards for Best Actor and Best Supporting Actor",
                "More Golden Globe Awards for Best Actor and Best Supporting Actor",
                "More positive reviews for Taxi Driver and Raging Bull"
            ]
        },
         "media_opinions_list": {
            "Al Pacino": [
                {"source": "IMDb", "text": "Al Pacino is one of the greatest actors of all time. His performances in The Godfather, Scarface, and Scent of a Woman are legendary.", "sentiment": "positive"},
                {"source": "Rotten Tomatoes", "text": "Al Pacino's recent performances have been lackluster and uninspired.", "sentiment": "negative"},
                {"source": "Variety", "text": "Al Pacino's portrayal of Jimmy Hoffa in The Irishman was a career highlight.", "sentiment": "positive"},
                {"source": "The Guardian", "text": "Al Pacino's over-the-top performance in Scarface is a bit much for my taste.", "sentiment": "negative"},
                {"source": "Rolling Stone", "text": "Al Pacino's performance in Dog Day Afternoon is one of the most intense and gripping in cinema history.", "sentiment": "positive"}
            ],
            "Robert Di Niro": [
                {"source": "IMDb", "text": "Robert Di Niro is a versatile actor who can play both dramatic and comedic roles with ease.", "sentiment": "positive"},
                {"source": "Rotten Tomatoes", "text": "Robert Di Niro's recent films have been disappointing and forgettable.", "sentiment": "negative"},
                {"source": "Variety", "text": "Robert Di Niro's performance in The Irishman was a return to form for the actor.", "sentiment": "positive"},
                {"source": "The Guardian", "text": "Robert Di Niro's performance in Meet the Parents is one of his funniest roles.", "sentiment": "positive"},
                {"source": "Rolling Stone", "text": "Robert Di Niro's performance in Raging Bull is one of the greatest in cinema history.", "sentiment": "positive"}
            ]
        },
         "twitter_audience_review_list": {
            "Al Pacino": {
                "@moviebuff100": "Just watched The Godfather for the first time and Al Pacino's performance blew me away. #legend #classic #cinema",
                "@filmfanatic": "Al Pacino's performance in Jack and Jill was painful to watch. #cringe #why #wasteoftalent",
                "@cinemalover": "Al Pacino's performance in Heat is one of the most underrated in his career. #masterclass #acting #genius",
                "@popcornlover": "Al Pacino's performance in The Irishman was good, but not his best work. #overrated #scorsese #netflix",
                "@moviemaniac": "Al Pacino's performance in Scent of a Woman is one of the most iconic in cinema history. #oscarwinner #legend #classic"
            },
            "Robert Di Niro": {
                "@moviebuff100": "Robert Di Niro's performance in Taxi Driver is one of the greatest in cinema history. #masterpiece #classic #genius",
                "@filmfanatic": "Robert Di Niro's performance in Dirty Grandpa was painful to watch. #cringe #why #wasteoftalent",
                "@cinemalover": "Robert Di Niro's performance in The Irishman was a return to form for the actor. #scorsese #netflix #oscarworthy",
                "@popcornlover": "Robert Di Niro's performance in Meet the Parents is one of his funniest roles. #comedy #laughoutloud #classic",
                "@moviemaniac": "Robert Di Niro's performance in Raging Bull is one of the greatest in cinema history. #oscarwinner #masterpiece #genius"
            },
            "Al Pacino Overall Sentiment": "mixed",
            "Robert Di Niro Overall Sentiment": "positive"
        },
        "weighted_average": {
            "Al Pacino": 75,
            "Robert Di Niro": 85
        },
        "winner": [
            "Winner: Robert Di Niro - Iconic Roles, Academy Awards, Golden Globe Awards, Screen Actors Guild Awards, Net Worth"
        ],
        "same_character_list": {
            "Al Pacino": {
                "movies": [
                    {
                        "name": "The Godfather",
                        "type": "Success",
                        "reviews": {
                            "positive": ["One of the greatest movies of all time", "Al Pacino's performance was outstanding"],
                            "negative": ["Some scenes were too violent"]
                        }
                    },
                    {
                        "name": "The Godfather Part II",
                        "type": "Success",
                        "reviews": {
                            "positive": ["Another masterpiece from Francis Ford Coppola", "Al Pacino's portrayal of Michael Corleone was brilliant"],
                            "negative": ["Some viewers found the movie too long"]
                        }
                    },
                    {
                        "name": "The Godfather Part III",
                        "type": "Failure",
                        "reviews": {
                            "positive": ["Al Pacino's performance was still great despite the weak script"],
                            "negative": ["The movie was a disappointment compared to the first two Godfather movies"]
                        }
                    },
                    {
                        "name": "Scarface",
                        "type": "Success",
                        "reviews": {
                            "positive": ["A classic gangster movie", "Al Pacino's performance was iconic"],
                            "negative": ["Some viewers found the violence excessive"]
                        }
                    },
                    {
                        "name": "Carlito's Way",
                        "type": "Success",
                        "reviews": {
                            "positive": ["A great crime drama", "Al Pacino's performance was excellent"],
                            "negative": ["Some viewers found the movie slow-paced"]
                        }
                    }
                ],
                "factors": {
                    "Range of characters played": 3,
                    "Critical acclaim for performances": 4,
                    "Box office success": 4,
                    "Consistency of success": 3
                }
            },
            "Robert Di Niro": {
                "movies": [
                    {
                        "name": "The Godfather Part II",
                        "type": "Success",
                        "reviews": {
                            "positive": ["Another masterpiece from Francis Ford Coppola", "Robert Di Niro's performance as young Vito Corleone was amazing"],
                            "negative": ["Some viewers found the movie too long"]
                        }
                    },
                    {
                        "name": "Goodfellas",
                        "type": "Success",
                        "reviews": {
                            "positive": ["One of the best gangster movies ever made", "Robert Di Niro's performance was outstanding"],
                            "negative": ["Some viewers found the movie too violent"]
                        }
                    },
                    {
                        "name": "Casino",
                        "type": "Success",
                        "reviews": {
                            "positive": ["A great crime drama", "Robert Di Niro's performance was excellent"],
                            "negative": ["Some viewers found the movie too long"]
                        }
                    },
                    {
                        "name": "Meet the Parents",
                        "type": "Success",
                        "reviews": {
                            "positive": ["A hilarious comedy", "Robert Di Niro's performance was a standout"],
                            "negative": ["Some viewers found the humor too predictable"]
                        }
                    },
                    {
                        "name": "The Intern",
                        "type": "Success",
                        "reviews": {
                            "positive": ["A heartwarming comedy-drama", "Robert Di Niro's performance was charming"],
                            "negative": ["Some viewers found the movie too formulaic"]
                        }
                    }
                ],
                "factors": {
                    "Range of characters played": 4,
                    "Critical acclaim for performances": 3,
                    "Box office success": 4,
                    "Consistency of success": 4
                }
            }
        },
        "success_factors": {
            "Al Pacino": {
                "Iconic Roles": 9,
                "Academy Awards": 1,
                "Golden Globe Awards": 4,
                "Screen Actors Guild Awards": 2,
                "Emmy Awards": 0,
                "Net Worth": "$165 million"
            },
            "Robert Di Niro": {
                "Iconic Roles": 10,
                "Academy Awards": 2,
                "Golden Globe Awards": 2,
                "Screen Actors Guild Awards": 2,
                "Emmy Awards": 0,
                "Net Worth": "$500 million"
            }
        },
        "actor_performance_analysis_list": {
            "Al Pacino": {
                "The Godfather - Michael Corleone's transformation from a reluctant outsider to a ruthless mafia boss is portrayed with great depth and intensity.": "Positive",
                "Scent of a Woman - Pacino's portrayal of a blind, retired army colonel is both nuanced and powerful, earning him an Academy Award.": "Positive",
                "Scarface - Pacino's over-the-top performance as Tony Montana is iconic, but some critics argue it lacks subtlety.": "Mixed",
                "Heat - Pacino's intense portrayal of a cop obsessed with catching a master thief is a standout in an ensemble cast.": "Positive",
                "The Irishman - Pacino's portrayal of union leader Jimmy Hoffa is a highlight of Martin Scorsese's epic crime drama.": "Positive",
                "Positive Performance Count": 4,
                "Negative Performance Count": 0
            },
            "Robert De Niro": {
                "The Godfather Part II - De Niro's portrayal of a young Vito Corleone won him an Academy Award and is considered one of his best performances.": "Positive",
                "Taxi Driver - De Niro's portrayal of a mentally unstable Vietnam veteran turned vigilante is haunting and intense.": "Positive",
                "Raging Bull - De Niro's physical transformation and emotional depth in his portrayal of boxer Jake LaMotta is widely praised.": "Positive",
                "Goodfellas - De Niro's supporting role as Jimmy Conway is a standout in an already stellar cast.": "Positive",
                "Cape Fear - De Niro's portrayal of a vengeful ex-convict is chilling and intense.": "Positive",
                "Positive Performance Count": 5,
                "Negative Performance Count": 0
            }
        },
        "good_acting_vs_bad_acting_list": {
            "Al Pacino": {
                "The Godfather - Pacino's subtle and nuanced performance as Michael Corleone is a prime example of good acting.": "Good Acting",
                "Scarface - Pacino's over-the-top performance as Tony Montana is often criticized as bad acting.": "Bad Acting",
                "Positive Good Acting Count": 1,
                "Negative Good Acting Count": 0,
                "Good Acting Score": 20,
                "Bad Acting Score": 80
            },
            "Robert De Niro": {
                "The Godfather Part II - De Niro's subtle and nuanced performance as young Vito Corleone is a prime example of good acting.": "Good Acting",
                "Rocky and Bullwinkle - De Niro's performance as Fearless Leader is often criticized as bad acting.": "Bad Acting",
                "Positive Good Acting Count": 1,
                "Negative Good Acting Count": 1,
                "Good Acting Score": 50,
                "Bad Acting Score": 50
            }
        },
        "actor_performance_accuracy_list": {
            "Al Pacino": {
                "Accurate portrayal of a mafia boss in The Godfather.": "Positive",
                "Accurate portrayal of a blind, retired army colonel in Scent of a Woman.": "Positive",
                "Less accurate portrayal of a Cuban immigrant turned drug lord in Scarface.": "Negative",
                "Accurate portrayal of a cop obsessed with catching a master thief in Heat.": "Positive",
                "Accurate portrayal of union leader Jimmy Hoffa in The Irishman.": "Positive",
                "Performance Accuracy Score": 80,
                "Factors Weightage": {
                    "History": 0.3,
                    "Storyline": 0.4,
                    "Depth of Performance": 0.2,
                    "Critical Acclaim": 0.1
                }
            },
            "Robert De Niro": {
                "Accurate portrayal of young Vito Corleone in The Godfather Part II.": "Positive",
                "Accurate portrayal of a mentally unstable Vietnam veteran turned vigilante in Taxi Driver.": "Positive",
                "Accurate portrayal of boxer Jake LaMotta in Raging Bull.": "Positive",
                "Accurate portrayal of Jimmy Conway in Goodfellas.": "Positive",
                "Less accurate portrayal of a vengeful ex-convict in Cape Fear.": "Negative",
                "Performance Accuracy Score": 80,
                "Factors Weightage": {
                    "History": 0.3,
                    "Storyline": 0.4,
                    "Depth of Performance": 0.2,
                    "Critical Acclaim": 0.1
                }
            }
        },
        "actor_star_power": {
            "Al Pacino": {
                "Good Acting Score": 20,
                "Bad Acting Score": 80,
                "Performance Accuracy Score": 80,
                "Box Office Success": 90,
                "Factors Weightage": {
                    "Good Acting": 0.2,
                    "Bad Acting": -0.2,
                    "Performance Accuracy": 0.4,
                    "Box Office Success": 0.6
                },
                "Star Power": 68.8
            },
            "Robert De Niro": {
                "Good Acting Score": 50,
                "Bad Acting Score": 50,
                "Performance Accuracy Score": 80,
                "Box Office Success": 80,
                "Factors Weightage": {
                    "Good Acting": 0.4,
                    "Bad Acting": -0.4,
                    "Performance Accuracy": 0.4,
                    "Box Office Success": 0.2
                },
                "Star Power": 52
            },
            "Winner": "Al Pacino",
            "Factors Where Al Pacino Surpassed Robert De Niro": ["Box Office Success"],
            "Calculation Steps": "Star Power = (Good Acting Score * Good Acting Weightage) + (Bad Acting Score * Bad Acting Weightage) + (Performance Accuracy Score * Performance Accuracy Weightage) + (Box Office Success * Box Office Success Weightage)",
            "Box Office Success Explanation": "Al Pacino's movies have grossed more at the box office than Robert De Niro's movies on average, giving him a higher weightage in the Star Power calculation."
        },
        'success_percentage_list': {'Al Pacino': {'Action': '70%',
   'Drama': '80%',
   'Crime': '75%',
   'Thriller': '70%'},
  'Robert Di Niro': {'Action': '80%',
   'Drama': '85%',
   'Crime': '90%',
   'Thriller': '85%'}},
 'release_time_list': {'Al Pacino': 'September', 'Robert Di Niro': 'October'}
   }

    # Page title
    st.title("Actor Awards Comparison")

    # Actor selection
    #actor = st.selectbox("Select an actor", list(data["awards_list"].keys()))

    # Actor information
    col1, col2 = st.columns(2)
       
    with col1:
        get_actor_1_poster()
        actor_data_1 = data["awards_list"]["Al Pacino"]
        # Display awards comparison horizontally
        st.subheader(f"Al Pacino")
        for item in actor_data_1:
            award = item["award"]
            movie = item["movie"]
            result = item["result"]
            st.write(f"**{icon_award} {award}**")
            st.write(f"Movie: {movie}")
            st.write(f"Result: {result}")
            st.write("---")
            
    with col2:
        get_actor_2_poster()
        actor_data_2 = data["awards_list"]["Robert Di Niro"]
        # Display awards comparison horizontally
        st.subheader(f"Robert Di Niro")
        for item in actor_data_2:
            award = item["award"]
            movie = item["movie"]
            result = item["result"]
            st.write(f"**{icon_award} {award}**")
            st.write(f"Movie: {movie}")
            st.write(f"Result: {result}")
            st.write("---")
        
        

    # Page title
    st.title("Actor Media Reviews Comparison")

    # Actors' reviews
    st.subheader("Reviews")
    
    col1, col2 = st.columns(2)
    
    with col1:
        for actor, reviews in data["media_reviews_list"].items():
            if actor not in ["Winner", "Factors where Robert Di Niro surpassed Al Pacino"]:
                if(actor == 'Al Pacino'):
                    #st.write(f"**{actor}**")
                    get_actor_1_poster()
                    for movie, review_info in reviews.items():
                        if movie not in ["Overall Sentiment", "Audience Rating Summary"]:
                            review = review_info["review"]
                            media_source = review_info["media_source"]
                            sentiment = review_info["sentiment"]
                            sentiment_icon = "👍" if sentiment == "Positive" else "🤔" if sentiment == "Neutral" else "👎"
                            st.write(f"{sentiment_icon} {movie}: {review} ({media_source})")
                    st.write("---")
        
        sentiment_al_pacino = 1 if data["media_reviews_list"]["Al Pacino"]["Overall Sentiment"] == "Positive" else 0.5
        
        
    with col2:
        for actor, reviews in data["media_reviews_list"].items():
            if actor not in ["Winner", "Factors where Robert Di Niro surpassed Al Pacino"]:
                if(actor == 'Robert Di Niro'):
                    #st.write(f"**{actor}**")
                    get_actor_2_poster()
                    for movie, review_info in reviews.items():
                        if movie not in ["Overall Sentiment", "Audience Rating Summary"]:
                            review = review_info["review"]
                            media_source = review_info["media_source"]
                            sentiment = review_info["sentiment"]
                            sentiment_icon = "👍" if sentiment == "Positive" else "🤔" if sentiment == "Neutral" else "👎"
                            st.write(f"{sentiment_icon} {movie}: {review} ({media_source})")
                    st.write("---")
        
        sentiment_robert_di_niro = 1 if data["media_reviews_list"]["Robert Di Niro"]["Overall Sentiment"] == "Positive" else 0.5

    
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+gauge",
        value=sentiment_al_pacino,
        title={'text': "Al Pacino", 'font': {'size': 16}},
        domain={'x': [0, 0.5], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 1]},
               'bar': {'color': 'indianred'},
               'bgcolor': 'white',
               'steps': [{'range': [0, 1], 'color': 'lightgray'}],
               'threshold': {'line': {'color': 'red', 'width': 4}, 'thickness': 0.75, 'value': 0.5}}))

    fig.add_trace(go.Indicator(
        mode="number+gauge",
        value=sentiment_robert_di_niro,
        title={'text': "Robert Di Niro", 'font': {'size': 16}},
        domain={'x': [0.5, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 1]},
               'bar': {'color': 'lightsalmon'},
               'bgcolor': 'white',
               'steps': [{'range': [0, 1], 'color': 'lightgray'}],
               'threshold': {'line': {'color': 'red', 'width': 4}, 'thickness': 0.75, 'value': 0.5}}))

    fig.update_layout(
        title="Overall Sentiment",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Audience Rating Summary
    ##st.subheader("Audience Rating Summary")
    audience_ratings_al_pacino = data["media_reviews_list"]["Al Pacino"]["Audience Rating Summary"]
    audience_ratings_robert_di_niro = data["media_reviews_list"]["Robert Di Niro"]["Audience Rating Summary"]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=list(audience_ratings_al_pacino.keys()), y=list(audience_ratings_al_pacino.values()), name="Al Pacino", marker_color="indianred"))
    fig.add_trace(go.Bar(x=list(audience_ratings_robert_di_niro.keys()), y=list(audience_ratings_robert_di_niro.values()), name="Robert Di Niro", marker_color="lightsalmon"))

    fig.update_layout(
        title="Audience Rating Summary",
        xaxis_title="Sentiment",
        yaxis_title="Percentage",
        barmode="group",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Factors where Robert Di Niro surpassed Al Pacino
    st.subheader("Factors where Robert Di Niro surpassed Al Pacino")
    factors = data["media_reviews_list"]["Factors where Robert Di Niro surpassed Al Pacino"]
    for factor in factors:
        st.write(f"- {factor}")


    st.subheader('Comparative analysis of actors based on media opinions')

    col1, col2 = st.columns(2)
    with col1:
        for actor, opinions in data['media_opinions_list'].items():
            if(actor == 'Al Pacino'):
                #st.subheader(actor)
                get_actor_1_poster()
                display_actor_info(opinions)
            
    with col2:
        for actor, opinions in data['media_opinions_list'].items():
            if(actor == 'Robert Di Niro'):
                #st.subheader(actor)
                get_actor_2_poster()
                display_actor_info(opinions)

    

    st.markdown(
        """
        <style>
        body {
            color: #fff;
            background-color: #000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.subheader("Actor Comparison - Twitter Audience Review List")

    # Display winner information
    #st.write("# Winner")
    #st.write(data["winner"][0])

#     # Display comparative analysis for Al Pacino
#     display_comparison("Al Pacino", data["twitter_audience_review_list"]["Al Pacino"])

#     # Display comparative analysis for Robert Di Niro
#     display_comparison("Robert Di Niro", data["twitter_audience_review_list"]["Robert Di Niro"])

    col1, col2 = st.columns(2)
    with col1:
        # Display overall sentiment for Al Pacino
        display_tweets("Al Pacino", data["twitter_audience_review_list"]["Al Pacino"])
        display_sentiment("Al Pacino", data["twitter_audience_review_list"]["Al Pacino Overall Sentiment"])
        
    with col2:
        # Display overall sentiment for Robert Di Niro
        display_tweets("Robert Di Niro", data["twitter_audience_review_list"]["Robert Di Niro"])
        display_sentiment("Robert Di Niro", data["twitter_audience_review_list"]["Robert Di Niro Overall Sentiment"])

    # Display weighted average
    #display_weighted_average(data["weighted_average"])
    
    st.write(data["winner"][0])

    # Set app title and subtitle
    st.subheader("Comparative analysis of actors based on movies and factors")

    col1, col2 = st.columns(2)
    with col1:
        #st.markdown("Al Pacino")
        get_actor_1_poster()
        display_movie_reviews(data["same_character_list"]["Al Pacino"])
        display_actor_factors(data["same_character_list"]["Al Pacino"])
        display_social_media(data["same_character_list"]["Al Pacino"])

    with col2:
        #st.markdown("Robert Di Niro")
        get_actor_2_poster()
        display_movie_reviews(data["same_character_list"]["Robert Di Niro"])
        display_actor_factors(data["same_character_list"]["Robert Di Niro"])
        display_social_media(data["same_character_list"]["Robert Di Niro"])

   
    st.subheader("Actor Success Factors Comparison")

    # Display comparative success factors
    success_factors = data["success_factors"]
    actors = list(success_factors.keys())

    col1, col2 = st.columns(2)

    with col1:
        #st.subheader(actors[0])
        get_actor_1_poster()
        for factor, value in success_factors[actors[0]].items():
            st.write(display_icon(factor), factor, value)

    with col2:
        #st.subheader(actors[1])
        get_actor_2_poster()
        for factor, value in success_factors[actors[1]].items():
            st.write(display_icon(factor), factor, value)

    # Display net worth comparison
    #st.subheader("Actor Net Worth")
    net_worth_data = [success_factors[actors[0]]["Net Worth"], success_factors[actors[1]]["Net Worth"]]
    net_worth_fig = create_horizontal_bar_chart(
        net_worth_data,
        "Net Worth",
        "Net Worth (in millions)",
        actors,
        colors=['#FF7171', '#82B366']
    )
    st.plotly_chart(net_worth_fig)

    # Display performance analysis
    st.subheader("Actor Performance Analysis")
    performance_data = data["actor_performance_analysis_list"]
    #performances = list(performance_data.keys())
    actors = list(performance_data.keys())

    col1, col2 = st.columns(2)

    with col1:
        #st.subheader(actors[0])
        get_actor_1_poster()
        for movie, sentiment in performance_data[actors[0]].items():
            sentiment_icon = "👍" if sentiment == "Positive" else "🤔" if sentiment == "Neutral" else "👎"
            st.write(display_icon(movie), movie, sentiment_icon)

    with col2:
        #st.subheader(actors[1])
        get_actor_2_poster()
        for movie, sentiment in performance_data[actors[1]].items():
            sentiment_icon = "👍" if sentiment == "Positive" else "🤔" if sentiment == "Neutral" else "👎"
            st.write(display_icon(movie), movie, sentiment_icon)

#     st.subheader("Performance Analysis")

#     for performance in performances:
#         if performance != "Positive Performance Count" and performance != "Negative Performance Count":
#             st.write(performance)

    # Display performance counts
    performance_counts = [performance_data[actors[0]]["Positive Performance Count"],
                          performance_data[actors[1]]["Positive Performance Count"]]
    performance_counts_fig = create_horizontal_bar_chart(
        performance_counts,
        "Performance Counts",
        "Count",
        actors,
        colors=['#FF7171', '#82B366']
    )
    st.plotly_chart(performance_counts_fig)


    # Title and introduction
    st.header("Actor Star Power Comparison")

    # Display good acting vs. bad acting comparison horizontally
    st.subheader("Good Acting vs. Bad Acting")
    good_acting_data = data["good_acting_vs_bad_acting_list"]
    col1, col2 = st.columns(2)
    with col1:
        #st.subheader("Al Pacino")
        get_actor_1_poster()
        st.markdown(f"**Positive Good Acting Count:** {good_acting_data['Al Pacino']['Positive Good Acting Count']}")
        st.markdown(f"**Negative Good Acting Count:** {good_acting_data['Al Pacino']['Negative Good Acting Count']}")
        st.markdown(f"**Good Acting Score:** {good_acting_data['Al Pacino']['Good Acting Score']}")
        st.markdown(f"**Bad Acting Score:** {good_acting_data['Al Pacino']['Bad Acting Score']}")
    with col2:
        #st.subheader("Robert De Niro")
        get_actor_2_poster()
        st.markdown(f"**Positive Good Acting Count:** {good_acting_data['Robert De Niro']['Positive Good Acting Count']}")
        st.markdown(f"**Negative Good Acting Count:** {good_acting_data['Robert De Niro']['Negative Good Acting Count']}")
        st.markdown(f"**Good Acting Score:** {good_acting_data['Robert De Niro']['Good Acting Score']}")
        st.markdown(f"**Bad Acting Score:** {good_acting_data['Robert De Niro']['Bad Acting Score']}")

    # Display performance accuracy comparison horizontally
    st.header("Actor Performance Accuracy")
    performance_accuracy_data = data["actor_performance_accuracy_list"]
    col1, col2 = st.columns(2)
    with col1:
        #st.subheader("Al Pacino")
        get_actor_1_poster()
        st.markdown(f"**Performance Accuracy Score:** {performance_accuracy_data['Al Pacino']['Performance Accuracy Score']}")
        st.markdown("**Factors Weightage**")
        for factor, weight in performance_accuracy_data['Al Pacino']['Factors Weightage'].items():
            st.markdown(f"- {factor}: {weight}")
    with col2:
        #st.subheader("Robert De Niro")
        get_actor_2_poster()
        st.markdown(f"**Performance Accuracy Score:** {performance_accuracy_data['Robert De Niro']['Performance Accuracy Score']}")
        st.markdown("**Factors Weightage**")
        for factor, weight in performance_accuracy_data['Robert De Niro']['Factors Weightage'].items():
            st.markdown(f"- {factor}: {weight}")

    # Display star power comparison horizontally
    st.header("Star Power")
    star_power_data = data["actor_star_power"]
    col1, col2 = st.columns(2)
    with col1:
        #st.subheader("Al Pacino")
        get_actor_1_poster()
        st.markdown(f"**Good Acting Score:** {star_power_data['Al Pacino']['Good Acting Score']}")
        st.markdown(f"**Bad Acting Score:** {star_power_data['Al Pacino']['Bad Acting Score']}")
        st.markdown(f"**Performance Accuracy Score:** {star_power_data['Al Pacino']['Performance Accuracy Score']}")
        st.markdown(f"**Box Office Success:** {star_power_data['Al Pacino']['Box Office Success']}")
        st.markdown("**Factors Weightage**")
        for factor, weight in star_power_data['Al Pacino']['Factors Weightage'].items():
            st.markdown(f"- {factor}: {weight}")
        st.markdown(f"**Star Power {icon_star}** {star_power_data['Al Pacino']['Star Power']}")
    with col2:
        #st.subheader("Robert De Niro")
        get_actor_2_poster()
        st.markdown(f"**Good Acting Score:** {star_power_data['Robert De Niro']['Good Acting Score']}")
        st.markdown(f"**Bad Acting Score:** {star_power_data['Robert De Niro']['Bad Acting Score']}")
        st.markdown(f"**Performance Accuracy Score:** {star_power_data['Robert De Niro']['Performance Accuracy Score']}")
        st.markdown(f"**Box Office Success:** {star_power_data['Robert De Niro']['Box Office Success']}")
        st.markdown("**Factors Weightage**")
        for factor, weight in star_power_data['Robert De Niro']['Factors Weightage'].items():
            st.markdown(f"- {factor}: {weight}")
        st.markdown(f"**Star Power {icon_star}** {star_power_data['Robert De Niro']['Star Power']}")

    # Display winner and factors where Al Pacino surpassed Robert De Niro
    st.header("Winner and Factors")
    st.subheader("Winner")
    st.markdown(f"The winner is: **{star_power_data['Winner']}**")

    st.subheader("Factors Where Al Pacino Surpassed Robert De Niro")
    for factor in star_power_data['Factors Where Al Pacino Surpassed Robert De Niro']:
        st.markdown(f"- {factor}")

    # Display calculation steps and box office success explanation
    st.subheader("Calculation Steps")
    st.markdown(star_power_data['Calculation Steps'])

    st.subheader("Box Office Success Explanation")
    st.markdown(star_power_data['Box Office Success Explanation'])
    
    st.header("Actor Success Percentage - Genre")
    
    col1, col2 = st.columns(2)
    with col1:
        #st.subheader("Al Pacino")
        get_actor_1_poster()
        st.markdown(f"**Action:** 70%")
        st.markdown(f"**Drama:** 80%")
        st.markdown(f"**Crime:** 75%")
        st.markdown(f"**Thriller:** 70%")
        st.markdown("")
                
        st.markdown(f"**Best time for new release:** September")
    with col2:
        #st.subheader("Robert De Niro")
        get_actor_2_poster()
        st.markdown(f"**Action:** 80%")
        st.markdown(f"**Drama:** 85%")
        st.markdown(f"**Crime:** 90%")
        st.markdown(f"**Thriller:** 85%")
        st.markdown("")
        
        st.markdown(f"**Best time for new release:** October")

    
        
# Main Function
def main():
    st.title("Actor Success Metric Comparison")
    st.markdown("This app compares the achievements, reviews, opinions of actors and calculate Star Power to suggest/recommend correct time to launch shows/movies of the actors to prevent any clash and maximum box office success of both.")

    # Actor Selection
    actor_names = st.multiselect("Select Actors", ["Robert Di Niro", "Al Pacino"])
    # Data Retrieval
    if st.button("Retrieve Data"):
        if len(actor_names) == 2:
            #data = retrieve_data(actor_names)
            #display_comparison(data, actor_names)
            display_comparison()
        else:
            st.warning("Please select two actors.")


if __name__ == "__main__":
    main()
           
