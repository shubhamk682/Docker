from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0",debug=True)