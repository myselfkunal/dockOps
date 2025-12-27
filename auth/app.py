from fastapi import FastAPI, HTTPException
import secrets
from pathlib import Path

app = FastAPI()

TOKEN_FILE = Path("auth/tokens.txt")

def save_token(token: str):
    with TOKEN_FILE.open("a") as f:
        f.write(token + "\n")

def token_exists(token: str) -> bool:
    if not TOKEN_FILE.exists():
        return False
    with TOKEN_FILE.open("r") as f:
        tokens = f.read().splitlines()
    return token in tokens

@app.get("/token")
async def get_token(user_id: str):
    token = f"{user_id}-{secrets.token_hex(8)}"
    save_token(token)
    return {"token": token}

@app.get("/validate")
async def validate_token(token: str):
    if token_exists(token):
        return {"valid": True}
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
    

