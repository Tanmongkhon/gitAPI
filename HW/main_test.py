@app.post("/hw/insert")
async def hw_insert(name, hw_name, status,value):
    data = Action.insert_data(name, hw_name, status,value)
    return data