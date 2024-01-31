from typing import List
from fastapi import APIRouter, Depends
from schemas.schemas import User_Base, User_Display
from sqlalchemy.orm import Session
from DB.Database import Get_DB
from DB import DB_User
 
 
router=APIRouter(prefix='/user', tags=['user'])
 
#Create User
@router.post('/', response_model= User_Display)
def create_user(request: User_Base, db: Session = Depends(Get_DB)):
    return DB_User.Create_User(db, request)
   
 
#Read all users (list of all users)
 
@router.get('/', response_model=List[User_Display])
def get_all_users(db: Session = Depends(Get_DB)):
    return DB_User.Get_all_Users(db)
 
 
#Read one user (user that fulfils elements in filter)
 
@router.get('/{id}', response_model=User_Display)
def get_User(Id: int, db: Session =Depends(Get_DB)):
    return DB_User.get_user(db, Id)
 
 
#Update
 
@router.post ('/{id}/update')
def Update_User(Id: int, request: User_Base, db: Session = Depends(Get_DB)):
    return DB_User.Update_User(db, Id, request)
 
 
#Delete
@router.get('/{id}/delete')
def delete_User(Id: int, request: User_Base, db: Session = Depends(Get_DB)):
    return DB_User.delete_User(db, Id)