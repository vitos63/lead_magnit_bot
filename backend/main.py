import uvicorn
from fastapi import FastAPI

from routers import first_questions

app = FastAPI()
app.include_router(first_questions.router)

if __name__ == "__main__":
    uvicorn.run(app)
