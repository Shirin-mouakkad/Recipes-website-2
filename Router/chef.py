from fastapi import APIRouter, Depends
from schemas.schemas import Chef_Base, Chef_Display
from sqlalchemy.orm import Session
from DB.Database import Get_DB
from DB import hash
from DB import DB_Chef
from typing import List
 
router=APIRouter(prefix='/chef', tags=['chef'])
 
#Create Chef
@router.post('/', response_model= Chef_Display)
def create_chef(request: Chef_Base, db: Session = Depends(Get_DB)):
    return DB_Chef.Create_Chef(db, request)
   
#read all chefs
 
@router.get('/', response_model=List[Chef_Display])
def Get_all_chefs(db: Session = Depends(Get_DB)):
    return DB_Chef.Get_all_chefs(db)
 
 
#Read one chef
 
@router.get('/{id}', response_model=Chef_Display)
def Get_Chef(Id: int, db: Session =Depends(Get_DB)):
    return DB_Chef.Get_Chef(db, Id)
 
#Update
 
@router.post ('/{id}/update')
def Update_Chef(Id: int, request: Chef_Base, db: Session = Depends(Get_DB)):
    return DB_Chef.Update_Chef(db, Id, request)
 
#Delete
@router.get('/{id}/delete')
def delete_Chef(Id: int, request: Chef_Base, db: Session = Depends(Get_DB)):
    return DB_Chef.delete_Chef(db, Id)