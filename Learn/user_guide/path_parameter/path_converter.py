from fastapi import FastAPI 

app = FastAPI()


@app.get("/file/{file_path:path}")
async def read_file(file_path: str):
    return {
        "file_path": file_path
    }
