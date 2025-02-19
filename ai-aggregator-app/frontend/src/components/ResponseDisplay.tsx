import React from 'react';

interface ResponseDisplayProps {
    responses: string[];
}

const ResponseDisplay: React.FC<ResponseDisplayProps> = ({ responses }) => {
    return (
        <div className="response-display">
            <h2 className="text-xl font-bold mb-4">Aggregated Responses</h2>
            <div className="responses-list">
                {responses.length > 0 ? (
                    responses.map((response, index) => (
                        <div key={index} className="response-item p-4 border rounded-lg mb-2">
                            <p>{response}</p>
                        </div>
                    ))
                ) : (
                    <p>No responses available.</p>
                )}
            </div>
        </div>
    );
};

export default ResponseDisplay;