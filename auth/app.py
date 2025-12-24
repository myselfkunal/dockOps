from fastapi import FastAPI
import secrets

app = FastAPI()

@app.get("/token")
async def get_token(user_id: str):
    random_token = secrets.token_urlsafe(16)
    return {
        "token": f"{user_id}-{random_token}"
        }

