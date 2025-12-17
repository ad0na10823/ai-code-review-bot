from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    event = request.headers.get("X-Github-Event")
    payload = await request.json()

    if event != "pull_request":
        return {"status": "ignored"}
    
    print("Pull request event received")
    return {"status": "ok"}