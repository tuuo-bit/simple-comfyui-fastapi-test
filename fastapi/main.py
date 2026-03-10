from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import random
import json

app = FastAPI( title = 'ComfyUI API', version = '1')

COMFY_URL = "http://ui:8188"

class GenerateRequest(BaseModel):
    positive_prompt: str = "big brown wooden table, sushi on a black plate, wassabi dip on the side, bowl of soy sauce"
    negative_prompt: str = "text, watermark, blur, hands"
    seed: int = 0

@app.post("/generate")
async def generate_image(req: GenerateRequest):     

    with open("workflows/T2Vemaonly.json", "r") as f:
        workflow = json.load(f)
    
    req.seed = random.randint( 10**15, (10**16) - 1)

    workflow["3"]["inputs"]["seed"] = req.seed
    workflow["6"]["inputs"]["text"] = req.positive_prompt
    workflow["7"]["inputs"]["text"] = req.negative_prompt

    payload = {
        "prompt": workflow,
        "client_id": "fastapi_client"
    }

    async with httpx.AsyncClient( verify=False) as client:
        try:
            response = await client.post( f"{COMFY_URL}/prompt", json=payload)
            response.raise_for_status()
            
            response = response.json()

            response["request"] = {}
            response["request"]['seed'] = req.seed
            response["request"]["+prompt"] = req.positive_prompt
            response["request"]["-prompt"] = req.negative_prompt

            return response
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))