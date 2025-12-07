from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Purple Deployment</title>
            <style>
                body {
                    background-color: #9b59b6; /* Purple */
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify_content: center;
                    align_items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 { font-size: 3rem; }
            </style>
        </head>
        <body>
            <h1>This is Purple Deployment from FastAPI</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    # Running on port 8003
    uvicorn.run(app, host="0.0.0.0", port=8003)