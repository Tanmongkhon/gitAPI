import uvicorn
from fastapi import FastAPI


app = FastAPI()



@app.get("/")
async def read_root():
    return {"Con": "Start"}

@app.get("/hw")
async def read_root():
    return {"Con": "Start"}


if __name__ == "__main__":
    uvicorn.run(app, host="10.96.24.87", port=80)