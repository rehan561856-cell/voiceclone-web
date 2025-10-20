from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import uvicorn, uuid, shutil

app = FastAPI()

@app.post("/clone")
async def clone_voice(text: str = Form(...), sample: UploadFile = File(...)):
    uid = str(uuid.uuid4())
    input_path = f"/tmp/{uid}_input.wav"
    output_path = f"/tmp/{uid}_output.wav"
    with open(input_path, "wb") as f:
        f.write(await sample.read())
    shutil.copy(input_path, output_path)  # placeholder
    return FileResponse(output_path, media_type="audio/wav", filename="output.wav")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
