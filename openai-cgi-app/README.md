# OpenAI CGI App

This project is a CGI application that interacts with the OpenAI API. It is designed to handle HTTP requests, process input data, and return responses formatted as HTML.

## Project Structure

```
openai-cgi-app
├── cgi-bin
│   ├── openai_cgi.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd openai-cgi-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your OpenAI API key:**
   Ensure that your OpenAI API key is set in your environment variables or modify the `openai_cgi.py` script to include your API key directly (not recommended for production).

## Usage

To run the CGI script, ensure your web server is configured to execute CGI scripts. Place the `cgi-bin` directory in the appropriate location for your web server (e.g., `/usr/lib/cgi-bin/` for Apache).

You can access the CGI script via a web browser or a tool like `curl`:

```bash
curl -d "input=your_input_here" http://yourserver/cgi-bin/openai_cgi.py
```

## CGI Script Overview

The `openai_cgi.py` script handles incoming HTTP requests, processes the input data, interacts with the OpenAI API, and returns the response in HTML format. 

## License

This project is licensed under the MIT License. See the LICENSE file for more details.