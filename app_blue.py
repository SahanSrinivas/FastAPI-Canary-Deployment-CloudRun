from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

# --- GLOBAL STATE ---
# We use this variable to simulate whether the app is broken or not.
is_healthy = True

# 1. HEALTH CHECK ENDPOINT (Cloud Run uses this)
@app.get("/health")
async def health_check(response: Response):
    global is_healthy
    if is_healthy:
        # Normal state: Respond with 200 OK
        response.status_code = status.HTTP_200_OK
        return {"status": "healthy"}
    else:
        # Broken state: Respond with 500 Error
        # Cloud Run will see this and eventually kill the container
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "unhealthy"}

# 2. KILL SWITCH (Visit this to simulate a crash)
@app.get("/break")
async def break_app():
    global is_healthy
    is_healthy = False
    return {
        "message": "APP BROKEN! The health check will now return 500 Error.",
        "instruction": "Wait 2 minutes for Cloud Run to restart me, or visit /heal to fix manually."
    }

# 3. HEAL BUTTON (Visit this to fix it manually without waiting)
@app.get("/heal")
async def heal_app():
    global is_healthy
    is_healthy = True
    return {"message": "APP HEALED! The health check is passing again."}

# 4. MAIN HOMEPAGE (The Blue Screen)
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Blue Deployment</title>
            <style>
                body {
                    background-color: #3498db; /* Blue */
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify_content: center;
                    align_items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 { font-size: 3rem; }
                p { font-size: 1.2rem; }
            </style>
        </head>
        <body>
            <h1>This is Blue Deployment from FastAPI</h1>
            <p>Try visiting <a href="/break" style="color: yellow;">/break</a> to test the health check failure.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    # Cloud Run will ignore this and use the Dockerfile CMD, but this helps for local testing
    uvicorn.run(app, host="0.0.0.0", port=8001)