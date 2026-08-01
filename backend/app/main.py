from fastapi import FastAPI


app = FastAPI(
    title="MentorOS API",
    description="Backend principal do MentorOS",
    version="0.1.0"
)


@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "MentorOS API"
    }