import unittest
from unittest import mock
from app import analyze_review, flask_app


class TestReviewAnalyzer(unittest.TestCase):
    def setUp(self):
        # Set up Flask application context before each test
        self.app_context = flask_app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Remove Flask application context after each test
        self.app_context.pop()

    def test_apple_reviews(self):
        # Test cases for Apple products
        apple_reviews = [
            {
                "review_text": "The iPhone 12 has exceeded my expectations! The camera quality is stunning, the battery life lasts all day, and the performance is super smooth. Definitely worth the investment.",
                "predicted_topic": "Overall Satisfaction with Purchase",
                "sentiment": "positive"
            },
            {
                "review_text": "I'm really disappointed with the iPhone 12. The battery drains way too quickly, the camera quality is mediocre at best, and it feels sluggish when running multiple apps. Not what I expected from a flagship device.",
                "predicted_topic": "Expectations and Product Quality",
                "sentiment": "negative"
            },
            {
                "review_text": "The iPhone 12 offers decent performance and battery life for its price range. The camera is satisfactory for everyday use, but don't expect professional-quality shots. Overall, it's a decent mid-range option.",
                "predicted_topic": "Overall Satisfaction with Purchase",
                "sentiment": "positive"
            },
            {
                "review_text": "I've been using the iPhone 12 for a few weeks now, and I'm impressed. The sleek design, coupled with its powerful performance, makes it a joy to use. The battery easily lasts me through the day, even with heavy usage.",
                "predicted_topic": "Overall Satisfaction with Purchase",
                "sentiment": "positive"
            },
            {
                "review_text": "I regret buying the iPhone 12. The software is riddled with bugs, the camera struggles in low light, and the build quality feels cheap. Save your money and look elsewhere.",
                "predicted_topic": "Appreciation towards Service and Delivery",
                "sentiment": "negative"
            }
        ]

        # Iterate over Apple reviews and test each one
        for review in apple_reviews:
            # Simulate a request JSON with company name in URL path and review text in body
            data = {'sentence': review['review_text']}

            # Simulate the request object
            mock_request = mock.MagicMock()
            mock_request.get_json.return_value = data

            # Simulate the company name being passed in the URL path
            company_name = 'apple'

            # Call the function with simulated request and company name
            with mock.patch('app.request', mock_request):
                response = analyze_review(company_name)

            # Extract JSON data from response
            json_data = response.get_json()

            # Assert the JSON data
            self.assertEqual(json_data['company'], 'apple')
            self.assertEqual(json_data['predicted_topic'], review['predicted_topic'])
            self.assertEqual(json_data['sentiment'], review['sentiment'])

    def test_samsung_reviews(self):
        # Test cases for Samsung products
        samsung_reviews = [
            {
                "review_text": "I can't say enough good things about the Samsung S22 Ultra. The display is gorgeous, the camera takes stunning photos, and the battery lasts me well into the next day. It's hands down the best phone I've ever owned",
                "predicted_topic": "Appreciation & Satisfaction with Features",
                "sentiment": "positive"
            },
            {
                "review_text": "I had high hopes for the Samsung S22 Ultra, but it fell short. The battery drains quickly, the software is buggy, and the camera is inconsistent. I wouldn't recommend it, especially for the price",
                "predicted_topic": "Overall Happiness & Satisfaction",
                "sentiment": "negative"
            },
            {
                "review_text": "The Samsung S22 Ultra offers some unique features, but it's not without its flaws. The battery life could be better, and the software feels cluttered. If you're looking for something different, it's worth considering.",
                "predicted_topic": "Overall Happiness & Satisfaction",
                "sentiment": "positive"
            },
            {
                "review_text": "After using the Samsung S22 Ultra for a month, I'm impressed. The performance is snappy, the camera takes great photos, and the battery easily lasts me through the day. Plus, the build quality feels premium. Definitely a winner in my book.",
                "predicted_topic": "Overall Happiness & Satisfaction",
                "sentiment": "positive"
            },
            {
                "review_text": "The Samsung S22 Ultra offers a good balance between price and performance. It's not groundbreaking, but it gets the job done. The camera is decent, and the battery life is average. Overall, it's a solid option.",
                "predicted_topic": "Overall Happiness & Satisfaction",
                "sentiment": "positive"
            }
        ]

        # Iterate over Samsung reviews and test each one
        for review in samsung_reviews:
            # Simulate a request JSON with company name in URL path and review text in body
            data = {'sentence': review['review_text']}

            # Simulate the request object
            mock_request = mock.MagicMock()
            mock_request.get_json.return_value = data

            # Simulate the company name being passed in the URL path
            company_name = 'samsung'

            # Call the function with simulated request and company name
            with mock.patch('app.request', mock_request):
                response = analyze_review(company_name)

            # Extract JSON data from response
            json_data = response.get_json()

            # Assert the JSON data
            self.assertEqual(json_data['company'], 'samsung')
            self.assertEqual(json_data['predicted_topic'], review['predicted_topic'])
            self.assertEqual(json_data['sentiment'], review['sentiment'])


if __name__ == '__main__':
    unittest.main()
