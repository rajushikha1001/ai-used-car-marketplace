import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [carData, setCarData] = useState({});
  const [predictedPrice, setPredictedPrice] = useState(null);

  const predictPrice = async () => {
    try {
      const response = await axios.post('http://localhost:5000/predict_price', carData);
      setPredictedPrice(response.data.predicted_price);
    } catch (error) {
      console.error('Error predicting price:', error);
    }
  };

  return (
    <div>
      <h1>AI-Powered Used Car Marketplace</h1>
      <input 
        type="text" 
        value={carData.make || ''} 
        onChange={(e) => setCarData({ ...carData, make: e.target.value })} 
        placeholder="Car Make"
      />
      {/* Other input fields for car data */}
      <button onClick={predictPrice}>Predict Price</button>
      {predictedPrice && <h2>Predicted Price: ${predictedPrice}</h2>}
    </div>
  );
}

export default App;
