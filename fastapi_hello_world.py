"""
Create a minimal FastAPI application with a root endpoint (GET /) that returns a JSON response with a “Hello World” message.
Structure the application in a clean and maintainable way, following common FastAPI best practices.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Example API",
    version="1.0.0",
    description="Simple Hello World endpoint"
)


@app.get("/", tags=["health"])
def read_root() -> dict:
    return {"message": "hello world"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    # Ou via CLI: uvicorn fastapi_hello_world:app --reload
