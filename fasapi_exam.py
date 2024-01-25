from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List

from utlity import read_questions_from_excel, add_new_question_to_excel

api = FastAPI()
security = HTTPBasic()

# User credentials
USERS = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin": "4dm1N"
}

class Question(BaseModel):
    question: str
    subject: str
    correct: List[str]
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str = None
    remark: str = None

# Verify if user is authenticated
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = credentials.username
    password = credentials.password
    if user not in USERS or USERS[user] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

@api.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    return {"message": "Login successful"}

@api.get("/healthcheck")
def health_check():
    return {"status": "API is functional"}







@api.post("/questions/new")
def create_new_question(question):
    # Assuming question is received as JSON data
    # Call utility function to add new question
    success = add_new_question_to_excel(question)
    if success:
        return {"message": "New question added successfully"}
    else:
        return {"message": "Failed to add the new question"}

@api.get("/questions/")
def get_questions():
    # Call utility function to retrieve questions from Excel
    questions = read_questions_from_excel()
    if questions is not None:
        return questions.to_dict(orient='records')
    else:
        return {"message": "Failed to retrieve questions"}
