# To run: uvicorn adapters.inbound.fastapi_adapter:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("adapters.inbound.fastapi_adapter:app", host="0.0.0.0", port=8000, reload=True)
