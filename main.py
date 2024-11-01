from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class Item(BaseModel):
    name :str
    age : int 
    height : int 




@app.get("/" , description="Its a good route" , deprecated=True )
def user():
    return "I'm an admin"

@app.put("/",deprecated=True)
async def user():
    return {"name": "Ansuman Shukla",
             "age" : 20,
             "body":"I'm a zen coder"}

@app.get("/users/{item_id}" ,deprecated=True)
async def get_item(item_id: int):
    return "The user is "+ str(item_id)


class foodEnums(str ,Enum):
    fruit = "fruit"
    vegitable = "vegitable"
    meat = "meat"

# @app.get("/food/{food_items}" , deprecated=True)
# async def get_food(food_items: foodEnums):

#     if food_items == foodEnums.fruit:

#         return {"food_items":"fruit" ,
#                 "message":" is a fruit"}
    
#     if food_items.value == "vegitable":

#         return  {"food_items":"vegitable" ,
#                  "message":" is a vegitable"}
    

fake_food_db = [{"food_items":"meat"} ,{"food_items":"fish"},{"food_items":"vegitable"}]

@app.get("/get_food")
async def get_food(start : int = 0, end : int = 12):
    
    return fake_food_db[start:end]



@app.get("/food/{item_id}")
async def get_food(item_id: int , short : bool | None = False):
    item = {"item_id": item_id}
    if short:
        item.update({"description": "A short description"})
        return item
    else:
        item.update({"description": "A very long description of item"})
        return item
    

@app.get("/course/{course_id}/{chapter_id}")
def get_course(course_id : int, chapter_id : int):
    return {"course_id":course_id ,"chapter_id":chapter_id}
