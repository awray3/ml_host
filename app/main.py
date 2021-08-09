from fastapi import FastAPI
from app import model
from app.data_model import ModelInput
import uvicorn

app = FastAPI()


@app.post("/model/")
async def run(model_input: ModelInput):

    return model.main(model_input)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
