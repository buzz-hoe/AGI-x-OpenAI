#!/usr/bin/env python3

import cgi
import cgitb
import json
import openai
import os

# Enable CGI error reporting
cgitb.enable()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("Content-Type: text/html")    # HTML is following
    print()                             # End of headers

    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Get user input from the form
    user_input = form.getvalue("input")

    # Check if input is provided
    if user_input:
        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            output = response['choices'][0]['message']['content']
        except Exception as e:
            output = f"Error: {str(e)}"
    else:
        output = "No input provided."

    # Generate HTML response
    print("<html>")
    print("<head><title>OpenAI CGI Response</title></head>")
    print("<body>")
    print("<h1>OpenAI Response</h1>")
    print(f"<p>{output}</p>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()