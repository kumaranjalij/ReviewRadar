import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './Style/CompanyDashboard.css';

function CompanyDashboard() {
  const { companyName } = useParams();
  const [companyData, setCompanyData] = useState(null);
  const [newReview, setNewReview] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);

  useEffect(() => {
    // Function to fetch data from backend API
    const fetchData = async () => {
      try {
        const response = await fetch(`http://review-radar-backend-svc:5001/${companyName}`);
        const data = await response.json();

        console.log("companyData:",data);

        setCompanyData(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [companyName]);

  const analyzeReview = async () => {
    try {
      // Define analyzeReview function
      const response = await fetch(`http://review-radar-backend-svc:5001/${companyName}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sentence: newReview }),
      });
      const data = await response.json();

      console.log("analysisResult:",data);
      
      setAnalysisResult(data);
    } catch (error) {
      console.error('Error analyzing review:', error);
    }
  };

  return (
    <div className="company-dashboard">
      {companyData ? (
        <>
          <h1>{companyData.company}</h1>
          <div className="images-container">
            {/* First Image Section: Number of reviews on each topic */}
            <h2>Number of Reviews on Each Topic</h2>
            <br/>
            <p style={{ fontSize: '1.1rem', lineHeight: '1.6' }}>This figure provides insight into the distribution of reviews across different topics. Each topic represents a specific aspect of customer feedback, ranging from product quality and satisfaction to buying experience and device functionality. By analyzing the number of reviews associated with each topic, companies can better understand the areas that are receiving the most attention from customers. This information enables businesses to prioritize their efforts and allocate resources effectively to address any areas of concern or capitalize on strengths. Understanding the volume of reviews for each topic helps companies tailor their strategies for enhancing customer experience and overall satisfaction.</p>
            <br/>
            <img src={`data:image/png;base64,${companyData.images[0]}`} alt="Number of Reviews on Each Topic" />

            {/* Second Image Section: Sentiment analysis by topic */}
            <h2>Sentiment Analysis by Topic</h2>
            <br/>
            <p style={{ fontSize: '1.1rem', lineHeight: '1.6' }}>This figure presents a sentiment analysis breakdown across different topics discussed in customer reviews. Each topic represents a distinct aspect of the customer experience, ranging from product quality to service satisfaction. By analyzing sentiment trends within each topic, businesses can gain valuable insights into how customers perceive various aspects of their offerings. Understanding the sentiment associated with each topic allows companies to pinpoint areas of strength and weakness in their products or services. Positive sentiment indicates areas where customers are satisfied, while negative sentiment highlights areas for improvement. By leveraging sentiment analysis, businesses can prioritize their efforts to address customer concerns and enhance overall satisfaction. This analysis enables companies to tailor their strategies more effectively, focusing on areas that require attention to drive positive sentiment and mitigate negative feedback. Ultimately, sentiment analysis by topic provides actionable insights that can inform decision-making and help businesses deliver better experiences for their customers.</p>
            <br/>
            <img src={`data:image/png;base64,${companyData.images[1]}`} alt="Sentiment Analysis by Topic" />
          </div>
          <p className="conclusion" style={{ fontWeight: 'bold' }}>{companyData.message}</p>

          <div className="review-container">
                <div className="add-voice">
                <h2>Add Your Voice</h2>
                </div>
    
                <p style={{ fontSize: '1.1rem', lineHeight: '1.6' }}>Have something to say about a brand? Share your thoughts by typing a new review into our text area. Review Radar will instantly analyze it, providing insights into the topic and sentiment of your review.</p>
                <br/>
                <textarea
                    className="review-textarea"
                    value={newReview}
                    onChange={(e) => setNewReview(e.target.value)}
                    placeholder="Type a new review here..."
                />
                <button className="analyze-button" onClick={analyzeReview}>Analyze</button>

            </div>
          {analysisResult && (
            <div className="analysis-result">
              <p>Predicted Topic: {analysisResult.predicted_topic}</p>
              <p>Sentiment: {analysisResult.sentiment}</p>
            </div>
          )}
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default CompanyDashboard;
