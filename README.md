
## requirements.txt
fastapi
uvicorn
jinja2
transformers
torch
python-multipart
feedparser

# RSS Headline Summarizer

This is a simple web application built using FastAPI, Jinja2, and Transformers libraries. It allows users to input an RSS feed URL and summarize the headlines using the BART summarization model.

## Features

- Real-time summarization of RSS feed headlines
- User-friendly interface with HTML templates
- Customizable summary length

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
uvicorn main:app --reload
```

Open your web browser and navigate to `http://localhost:8000`.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please contact us at [placeholder email address].
