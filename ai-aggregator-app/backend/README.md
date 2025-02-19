# AI Aggregator Backend

This is the backend for the AI Aggregator application, which integrates multiple AI models to provide aggregated responses to user queries.

## Project Structure

- **app/**: Contains the main application code.
  - **main.py**: Entry point for the FastAPI application.
  - **api/**: Contains API versioning and endpoint definitions.
    - **v1/**: Version 1 of the API.
      - **endpoints.py**: Defines the API endpoints and route handlers.
  - **core/**: Contains core functionality and configuration.
    - **config.py**: Configuration settings, including API keys and environment variables.
    - **merge_responses.py**: Logic for merging and ranking responses from different AI models.
  - **models/**: Defines data models for interacting with AI services.
    - **ai_models.py**: Request and response schemas.
  - **services/**: Contains service logic for interacting with various AI APIs.
    - **chatgpt_service.py**: Logic for ChatGPT API interactions.
    - **gemini_service.py**: Logic for Gemini API interactions.
    - **claude_service.py**: Logic for Claude API interactions.
    - **grok_service.py**: Logic for Grok API interactions.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd ai-aggregator-app/backend
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Update the `config.py` file with your API keys and other necessary configurations.

5. **Run the application**:
   ```
   uvicorn app.main:app --reload
   ```

## Usage

Once the backend is running, you can access the API at `http://localhost:8000/api/v1/`. Use the defined endpoints to send queries and receive aggregated responses from the integrated AI models.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.