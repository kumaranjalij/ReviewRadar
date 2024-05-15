print("hello world")
import pandas as pd

file = pd.read_csv("Apple_reviews.csv")


### arinoode ithokke evda kodukkanam enn.
# Enthayalum model ondakkana vara mathi model.py da akath


# Assign each sentence to a topic
topic_assignments = nmf_model.transform(tfidf_matrix).argmax(axis=1)

topic_names = {
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

# Create a DataFrame to store the review text, the respective topic number, and the topic name
df_topics = pd.DataFrame({"Review": preprocessed_sentences,
                           "Topic Number": topic_assignments,
                           "Topic Name": [topic_names[i] for i in topic_assignments]})

# Print the DataFrame to verify the creation and addition of the "Topic Name" column
#print(df_topics)

# Make pickle file of our model
