from fastapi import APIRouter, Depends
from schemas.schemas import Recipe_Base, Recipe_Display
from sqlalchemy.orm import Session
from DB import DB_Recipes
from DB.Database import Get_DB
from typing import List

router=APIRouter(prefix='/recipe', tags=['recipe'])

#Create a new Recipe

@router.post('/new')
def Create_Recipes(request: Recipe_Base, db: Session = Depends(Get_DB)):
    return DB_Recipes.Create_Recipes(db, request)

#Read one recipe

@router.get('/{id}', response_model=Recipe_Display)
def get_Recipe(Id: int, db: Session =Depends(Get_DB)):
    return DB_Recipes.get_Recipe(db, Id)

#Read All Recipes
 
 @router.get('/', response_model=List[Recipe_Display])
def Get_all_Recipe(db: Session = Depends(Get_DB)):
    return DB_Recipes.Get_all_Recipe(db)

#Update Recipe

@router.post ('/{id}/update')
def Update_Recipe(Id: int, request: Recipe_Base, db: Session = Depends(Get_DB)):
    return DB_Recipes.Update_Recipe(db, Id, request)
 
#Delete Recipe

@router.get('/{id}/delete')
def delete_Recipe(Id: int, request: Recipe_Base, db: Session = Depends(Get_DB)):
    return DB_Recipes.delete_Recipe(db, Id)
