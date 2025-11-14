import axios from 'axios';

const apiUrl = 'http://localhost:5000';

export const predictPrice = async (carData) => {
  try {
    const response = await axios.post(`${apiUrl}/predict_price`, carData);
    return response.data.predicted_price;
  } catch (error) {
    console.error('Error predicting price:', error);
  }
};
