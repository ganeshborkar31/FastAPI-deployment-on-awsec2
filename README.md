# Survival Prediction Web Application

This project is a simple web application built using **FastAPI** for the backend and basic **HTML, CSS, and JavaScript** for the frontend. The application predicts whether a person would survive based on their age and sex.

## Features

- **Backend**: A FastAPI server that processes the input data and returns a prediction.
- **Frontend**: A user-friendly interface to input age and sex, and view the survival prediction.
- **CORS**: Configured to handle cross-origin requests.

## Project Structure

```plaintext
my_fastapi_project/
├── app/
│   ├── main.py                # FastAPI backend code
│   └── static/
│       ├── index.html         # Frontend HTML file
│       └── (other static files like CSS and JS if any)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
