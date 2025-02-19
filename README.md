# AI Aggregator Application

This project is an AI aggregator web application that integrates multiple AI models to provide users with refined responses based on their queries. The application consists of a backend built with FastAPI and a frontend developed using React.

## Project Structure

```
ai-aggregator-app
├── backend
│   ├── app
│   │   ├── main.py                # Entry point for the backend application
│   │   ├── api
│   │   │   ├── v1
│   │   │   │   └── endpoints.py   # API endpoints for version 1
│   │   ├── core
│   │   │   ├── config.py          # Configuration settings
│   │   │   └── merge_responses.py # Logic for merging and ranking responses
│   │   ├── models
│   │   │   └── ai_models.py       # Data models for AI services
│   │   └── services
│   │       ├── chatgpt_service.py # Service for ChatGPT API
│   │       ├── gemini_service.py  # Service for Gemini API
│   │       ├── claude_service.py  # Service for Claude API
│   │       ├── grok_service.py     # Service for Grok API
│   ├── requirements.txt            # Python dependencies for the backend
│   └── README.md                   # Documentation for the backend
├── frontend
│   ├── public
│   │   └── index.html             # Main HTML file for the frontend
│   ├── src
│   │   ├── components
│   │   │   ├── App.tsx            # Main component of the React application
│   │   │   ├── Header.tsx         # Header component
│   │   │   ├── Footer.tsx         # Footer component
│   │   │   └── ResponseDisplay.tsx # Component for displaying AI responses
│   │   ├── pages
│   │   │   └── Home.tsx           # Home page component
│   │   ├── styles
│   │   │   └── main.css           # Main CSS styles
│   │   ├── App.tsx                # Another entry point for the React app
│   │   ├── index.tsx              # Entry point for rendering the React app
│   │   └── api
│   │       └── apiClient.ts       # Functions for making API calls to the backend
│   ├── package.json                # Configuration file for npm
│   ├── tailwind.config.js          # Tailwind CSS configuration
│   ├── postcss.config.js           # PostCSS configuration
│   ├── tsconfig.json               # TypeScript configuration
│   └── README.md                   # Documentation for the frontend
├── .gitignore                      # Files and directories to ignore by Git
└── README.md                       # Overall project documentation
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

- Access the frontend application in your browser at `http://localhost:3000`.
- Input your query in the provided interface, and the application will aggregate responses from multiple AI models.

## Contributing

Feel free to submit issues or pull requests to improve the application!
