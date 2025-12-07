from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/health", status_code=200)
async def health_check():
    return JSONResponse(content={"status": "healthy"}, status_code=200)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Green Deployment</title>
            <style>
                body {
                    background-color: #2ecc71; /* Green */
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
            <h1>This is Green Deployment from FastAPI</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    # Running on port 8002
    uvicorn.run(app, host="0.0.0.0", port=8002)
