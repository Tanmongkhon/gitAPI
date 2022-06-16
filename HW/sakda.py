 for i in data:
    if(i["status"]=="ON"):
        data = "trun"
    else:
        data = "error"
    return data