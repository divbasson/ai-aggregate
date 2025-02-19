import React from 'react';

const Footer: React.FC = () => {
    return (
        <footer className="bg-gray-800 text-white py-4">
            <div className="container mx-auto text-center">
                <p>&copy; {new Date().getFullYear()} AI Aggregator. All rights reserved.</p>
                <p>
                    <a href="/privacy" className="text-gray-400 hover:text-white">Privacy Policy</a> | 
                    <a href="/terms" className="text-gray-400 hover:text-white"> Terms of Service</a>
                </p>
            </div>
        </footer>
    );
};

export default Footer;