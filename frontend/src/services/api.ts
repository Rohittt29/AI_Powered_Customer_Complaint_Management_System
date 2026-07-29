import axios from 'axios';

// Create a centralized Axios instance
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for inserting tokens in the future
api.interceptors.request.use(
  (config) => {
    // const token = localStorage.getItem('token');
    // if (token) {
    //   config.headers.Authorization = `Bearer ${token}`;
    // }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for global error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Global error handling logic can go here (e.g., dispatching toast actions)
    if (error.response) {
      console.error(`API Error: ${error.response.status} - ${error.response.data?.detail || error.message}`);
    } else if (error.request) {
      console.error('API Error: No response received from server');
    } else {
      console.error('API Error: Request setup failed', error.message);
    }
    return Promise.reject(error);
  }
);
