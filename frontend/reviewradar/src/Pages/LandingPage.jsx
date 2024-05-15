import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Style/LandingPage.css';

function LandingPage() {

    const navigate = useNavigate();

  const handleCompanyChange = (event) => {
    const selectedCompany = event.target.value;
    if (selectedCompany) {
      
      console.log(selectedCompany);

      navigate(`/company-dashboard/${selectedCompany}`);
    }
  };

  return (
    <div className="landing-page">
      <h1 className="title">Review Radar</h1>
      <p className="subtitle">Review Radar is your go-to tool for gaining deep insights into customer feedback about various brands. With Review Radar, you can analyze reviews of different brands, understand customer sentiments, and pinpoint key aspects of products or services that companies should focus on. Whether you're a business owner striving to enhance customer satisfaction or a consumer curious about what others are saying, Review Radar has you covered.</p>
      <div className="dropdown-container">
        <select className="dropdown" onClick={handleCompanyChange}>
          <option value="">Select Company</option>
          <option value="apple">
            <Link  className="link">
              Apple
            </Link>
          </option>
          <option value="samsung">
            <Link  className="link">
              Samsung
            </Link>
          </option>
        </select>
      </div>
    </div>
  );
}

export default LandingPage;


