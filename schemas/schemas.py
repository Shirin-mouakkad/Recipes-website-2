from pydantic import BaseModel
from collections import namedtuple

class Chef_Base(BaseModel):
    Chef_Firstname: str
    Chef_Lasttname: str
    Nationality: str
    Photo: str
    Password: str
    Email: str
    rating: int
    rating_no: int

#Chef display for chefs who create new accounts
    
class Chef_Display(BaseModel):
    Chef_Firstname: str
    Chef_Lasttname: str
    Nationality: str
    Photo: str
    Email: str
    rating: int
    rating_no: int
    class Config():
        orm_mode=True
    

class User_Base(BaseModel):
    Firstname: str
    Lasttname: str
    Photo: str
    Password: str
    Email: str

#User display for users who create new accounts

class User_Display(BaseModel):
    Firstname: str
    Lastname: str
    Photo: str
    Email: str
    class Config():
        orm_mode=True

class Recipe_Base(BaseModel):
    Name: str
    Desc: str
    Category: str
    Vegan: bool
    Duration: str
    Rating: int
    rating_no: int
  
class Ingredient_Base(BaseModel):
    Name: str
    Category: str
   
class RecipeReview_Base(BaseModel):
    Recipe_ID: int
    User_ID:int
    Rating: int
    Review: int

class ChefsReview_Base(BaseModel):
    chef_id: int
    User_ID: int 
    Rating: int
    

class Admin_Base(BaseModel):
    Name: str
    Email: str
    Password: str


class RecipeIngredient_Base(BaseModel):
    RecipeId:int
    IngredientId: int


#Chef display for chefs who create new accounts
   
class Chef_Display(BaseModel):
    Chef_Firstname: str
    Chef_Lasttname: str
    Nationality: str
    Photo: str
    Email: str
    rating: int
    rating_no: int
    class Config():
        orm_mode=True

#User display for users who create new accounts
 
class User_Display(BaseModel):
    Firstname: str
    Lastname: str
    Photo: str
    Email: str
    class Config():
        orm_mode=True

#Recipe display 

class Recipe_Display(BaseModel):
    Name: str
    Desc: str
    Category: str
    Vegan: bool
    Duration: str
    Rating: int
    rating_no: int
    class Config():
        orm_mode=True