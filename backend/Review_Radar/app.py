#import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import joblib
import spacy
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import base64
import logging
from logging.handlers import RotatingFileHandler

#configure logging
# logging.basicConfig(filename='app.log' , level= logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define a rotating file handler
handler = RotatingFileHandler('app.log', maxBytes=90*1024*1024, backupCount=10)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Get the root logger and configure it
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Create flask app
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://anjali:Anjali%402000@localhost:3306/review_radar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


class NewReview(db.Model):
    __tablename__ = 'new_reviews'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255))
    reviews = db.Column(db.Text)  # Corrected column name to 'reviews'

#load models and vectorizer
try:
    Apple_nmf_model = pickle.load(open("Apple_model.pkl", "rb"))
    Apple_vectorizer = pickle.load(open("Apple_vectorizer.pkl","rb"))
    Samsung_nmf_model = pickle.load(open("Samsung_model.pkl","rb"))
    Samsung_vectorizer = pickle.load(open("Samsung_vectorizer.pkl","rb"))
    logging.info("Models and vectorizer loaded successfully")
except Exception as e:
    logging.error('Error loading models and vectorizer: %s',str(e))

# Load the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

#defining topic names
Apple_topic_names = {
    0: "Ordering and Customer Service",
    1: "Product Quality and Experience",
    2: "Buying Experience",
    3: "Expectations and Product Quality",
    4: "Issues with Device Functionality",
    5: "Condition and Packaging of Items",
    6: "Appreciation towards Service and Delivery",
    7: "Satisfaction with Product Condition",
    8: "Recommendations and Satisfaction",
    9: "Overall Satisfaction with Purchase"
}
Samsung_topic_names = {
    0: "Customer Experience & Satisfaction",
    1: "Product Quality & Value",
    2: "Appreciation & Satisfaction with Features",
    3: "General Product Satisfaction",
    4: "Device Functionality & Performance",
    5: "Buying Experience & Recommendation",
    6: "Excellent Product & Service",
    7: "Aesthetic & Functional Appeal",
    8: "Device Usage & Performance",
    9: "Overall Happiness & Satisfaction"
}

def preprocess_sentence(sentence):
    # Parse the sentence using spaCy
    doc = nlp(sentence)

    # Lemmatization, removing stop words, punctuation, and non-alphanumeric tokens
    words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

    # Join the words back into a sentence
    preprocessed_sentence = ' '.join(words)

    return preprocessed_sentence


@app.route("/")
def Home():
    logging.info("Home page is accessed")
    return "hai this is the home page"


@app.route("/<company_name>")
def company_home(company_name):
    logging.info("accessed home page of company %s", company_name)
    print("the dashboard endpoint was accessed")
    if company_name.lower() == "apple":
        # Data for Apple
        with open("./images/Apple1.png", "rb") as file:
            image1_data = base64.b64encode(file.read()).decode('utf-8')
        with open("./images/Apple2.png", "rb") as file:
            image2_data = base64.b64encode(file.read()).decode('utf-8')
        data = {
            "company": "Apple",
            "images": [image1_data, image2_data],
            "message": "The firm should focus more on the 'Ordering and Customer Service' aspect, as it has the highest percentage of negative reviews (25.43%). There is scope for improvement in the 'Ordering and Customer Service' aspect, as it has the highest percentage of neutral reviews (43.87%). The firm is performing well in the 'Buying Experience' aspect, as it has the highest percentage of positive reviews (96.58%)."
        }
    elif company_name.lower() == "samsung":
        # Data for Samsung
        with open("./images/Samsung1.png", "rb") as file:
            image1_data = base64.b64encode(file.read()).decode('utf-8')
        with open("./images/Samsung2.png", "rb") as file:
            image2_data = base64.b64encode(file.read()).decode('utf-8')
        data = {
            "company": "Samsung",
            "images": [image1_data, image2_data],
            "message": " The firm should focus more on the 'Device Usage & Performance' aspect, as it has the highest percentage of negative reviews (23.03%). There is scope for improvement in the 'Customer Experience & Satisfaction' aspect, as it has the highest percentage of neutral reviews (45.72%). The firm is performing well in the 'Appreciation & Satisfaction with Features' aspect, as it has the highest percentage of positive reviews (98.44%)."
        }
    else:
        # Default message for other companies
        data = {"company": company_name}

    return jsonify(data)


@app.route('/<company_name>/analyze', methods=['POST'])
def analyze_review(company_name):
    logging.info('Analyzing review %s', company_name)
    if company_name.lower() == "apple":
        vectorizer = Apple_vectorizer
        nmf_model = Apple_nmf_model
        topic_names = Apple_topic_names
    elif company_name.lower() == "samsung":
        vectorizer = Samsung_vectorizer
        nmf_model = Samsung_nmf_model
        topic_names = Samsung_topic_names
    else:
        logging.warning("invalid company name")
        return jsonify({"error": "Invalid company name"})

    data = request.get_json(force=True)
    new_review_text = data.get('sentence', '')

    # Save the review to the database
    new_review = NewReview(company_name=company_name, reviews=new_review_text)
    db.session.add(new_review)
    db.session.commit()
    logging.info("review added to database for company %s", company_name)

    # Preprocess the new review
    preprocessed_new_review = preprocess_sentence(new_review_text)

    # Transform the preprocessed review into a TF-IDF vector
    tfidf_vector = vectorizer.transform([preprocessed_new_review])

    # Use the trained NMF model to transform the TF-IDF vector into a topic distribution
    topic_distribution = nmf_model.transform(tfidf_vector)

    # Identify the topic with the highest probability
    predicted_topic = topic_distribution.argmax()
    topic_name = topic_names[predicted_topic]

    # Analyze the sentiment of the review
    sentiment_score = sid.polarity_scores(new_review_text)
    sentiment = "positive" if sentiment_score["compound"] > 0 else "negative" if sentiment_score["compound"] < 0 else "neutral"
    logging.info("Sentiment analyszed for company %s", company_name)

    # Prepare response
    response = {
        "company": company_name,
        "predicted_topic": topic_name,
        "sentiment": sentiment
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=5001)