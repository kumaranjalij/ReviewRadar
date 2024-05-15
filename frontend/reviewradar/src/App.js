import { BrowserRouter, Routes, Route } from "react-router-dom";

import LandingPage from "./Pages/LandingPage";
import CompanyDashboard from "./Pages/CompanyDashboard";

import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      
        <BrowserRouter>
          <Routes>

            <Route path="/" element={<LandingPage />} />
            <Route path="/company-dashboard/:companyName" element={<CompanyDashboard/>} />

          </Routes>
        </BrowserRouter>
     
    </div>
  );
}

export default App;
