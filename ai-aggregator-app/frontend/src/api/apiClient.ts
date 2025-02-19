import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://localhost:8000/api/v1', // Adjust the base URL as needed
    headers: {
        'Content-Type': 'application/json',
    },
});

export const fetchAggregatedResponse = async (query) => {
    try {
        const response = await apiClient.post('/aggregate', { query });
        return response.data;
    } catch (error) {
        console.error('Error fetching aggregated response:', error);
        throw error;
    }
};