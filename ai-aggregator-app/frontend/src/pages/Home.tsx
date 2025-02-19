import React, { useState } from 'react';
import ResponseDisplay from '../components/ResponseDisplay';

const Home: React.FC = () => {
    const [query, setQuery] = useState('');
    const [responses, setResponses] = useState<string[]>([]);
    const [loading, setLoading] = useState(false);

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setLoading(true);
        setResponses([]);

        try {
            const response = await fetch('/api/v1/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query }),
            });

            const data = await response.json();
            setResponses(data.responses);
        } catch (error) {
            console.error('Error fetching responses:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen">
            <h1 className="text-3xl font-bold mb-4">AI Aggregator</h1>
            <form onSubmit={handleSubmit} className="mb-4">
                <input
                    type="text"
                    value={query}
                    onChange={handleInputChange}
                    placeholder="Ask your question..."
                    className="border p-2 rounded"
                    required
                />
                <button type="submit" className="ml-2 p-2 bg-blue-500 text-white rounded">
                    Submit
                </button>
            </form>
            {loading && <p>Loading...</p>}
            <ResponseDisplay responses={responses} />
        </div>
    );
};

export default Home;