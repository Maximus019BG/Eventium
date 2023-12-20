import axios from 'axios';

const API_BASE_URL = 'http://your-django-api-url';

export const fetchData = async (endpoint: string) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/${endpoint}`);
    return response.data;
  } catch (error) {
    console.error('API request failed', error);
    throw error;
  }
};