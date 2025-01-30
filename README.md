# stage-0-backend
*HNG 12 Internship backend track stage-0*

A publicly accesible API that provides
personal data in json format. It doesn't require authentication. Implementation was achieved using python's FastAPI framework

# Local Setup
1. Clone the repository

        git clone https://github.com/Ayo-Oni-515/stage-0-backend.git

2. Install dependencies

    Dependencies are available in requirements.txt

    * fastapi
    * uvicorn

    To install dependencies on local machine

        pip install -r requirements.txt

3. Test locally by using this command then click on the localhst link provided in the terminal.

        uvicorn main:app --reload

## API Documentation
To access online, use endpoint URL:

    https://stage-0-backend.onrender.com/

Typical JSON Response Format (200 OK):

    {
        "email": "ayodejioni1505@gmail.com",
        "current_datetime": "2025-01-30T14:30:35Z",
        "github_url": "https://github.com/Ayo-Oni-515/stage-0-backend"
    }

Usage

    import requests

    response = requests.get("https://stage-0-backend.onrender.com/")
    print(response.json())


To hire API developers, visit: https://hng.tech/hire/python-developers