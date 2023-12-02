# FastAPI Email Validation API Server

The FastAPI Email Validation API is a simple and efficient web service built using the FastAPI framework in Python. The primary purpose of this API is to validate email addresses, either individually or in bulk, and provide quick and accurate results regarding their validity.

## Features

- **Single Email Validation:** Submit a single email address to the `/v1/validate-emails/{email}` endpoint to check its validity against general email rules and a disposable email blocklist.

- **Bulk Email Validation:** Submit a list of email addresses to the `/v1/validate-emails/` endpoint for bulk validation. The API returns a list of results for each email address, including validation status and error messages if applicable.

- **API Key Authentication:** Secure your API by requiring an API key for authentication. Include the `X-API-Key` header with your requests to validate access.

- **Performance Metrics:** The API provides information about the time taken to validate each email, aiding in performance analysis and optimization.

## Installation and Usage

To set up and run the FastAPI Email Validation API, follow the installation instructions provided in the README.md file. After installation, you can use various API endpoints to validate emails and receive detailed results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/s-azizkhan/fastapi-email-validation-server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-email-validation-server
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and set your environment variables:

   ```dotenv
    API_PREFIX=/api
    API_SECRET_KEY=XXX
   ```

5. Run the FastAPI application:

   ```bash
   uvicorn app:app --reload --port 8000
   ```

## Example

Assuming the FastAPI server is running at `http://127.0.0.1:8000`:

### Validate a Single Email

```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/validate-emails/user@example.com
```

### Validate Bulk Emails

```bash
curl -X POST -H "Content-Type: application/json" -d '{"emails": ["user1@example.com", "user2@example.com"]}' http://127.0.0.1:8000/api/v1/validate-emails
```

## Usage

- **Validate a Single Email:** Send a POST request to `/api/v1/validate-emails/{email}` with a JSON payload containing a single email.

- **Validate Bulk Emails:** Send a POST request to `/api/v1/validate-emails` with a JSON payload containing a list of emails.

Make sure to include the `X-API-Key` header with the correct API key for authentication.

### API Key Authentication

To use the API key authentication:

- Include the `X-API-Key` header with the API key value when making requests.
- The default API key in this example is "your-secret-key." Replace it with your actual API key in the `validate_api_key` middleware.

**Example with API key:**

```bash
curl -X POST -H "Content-Type: application/json" -H "X-API-Key: your-secret-key" http://127.0.0.1:8000/api/v1/validate-emails/user@example.com
```

If the API key is missing or invalid, the server will respond with a 403 Forbidden error.

## Contributors

- [S.Aziz Khan](https://github.com/s-azizkhan)

## Contributing

If you would like to contribute to the development of the FastAPI Email Validation API, feel free to fork the repository, make improvements, and submit a pull request.
