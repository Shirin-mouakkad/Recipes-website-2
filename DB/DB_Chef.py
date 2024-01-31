from .hash import Hash
from sqlalchemy.orm.session import Session
from schemas.schemas import Chef_Base
from .Models import Chefs
from typing import Optional

def Create_Chef(db: Session, request: Chef_Base):
    New_chef= Chefs(
        Chef_Firstname=request.Chef_Firstname,
        Chef_Lasttname=request.Chef_Lasttname,
        Nationality=request.Nationality,
        Photo=request.Photo,
        Password=Hash.bcrypt(request.Password),
        Rating=request.rating,
        rating_no=request.rating_no,
        Email=request.Email

    )

    db.add(New_chef)
    db.commit()
    db.refresh(New_chef)
    return New_chef

def Get_all_chefs(db:Session):
    return db.query(Chefs).all()

def get_Chef(db:Session,Id:int):
    return db.query(Chefs).filter(Chefs.id==Id)

def get_chefs_filtered(
        db:Session,
        Rating:Optional[int]=None,
        Nationality:Optional[str]=None
        ):
    query = db.query(Chefs)
    if Rating is not None:
        query.filter(Chefs.Rating==Rating)
    if Nationality is not None:
        query.filter(Chefs.Nationality==Nationality)
    return query.all

def Update_Chef(
        db:Session,
        Chef_ID:int,
        request:Chef_Base
        ):
    query = db.query(Chefs)
    query.filter(Chefs.id==Chef_ID)
    query.update({Chefs.rating_no:request.rating_no,Chefs.Rating:request.rating})
    db.commit()
    return query.all()
    
def delete_Chef(db:Session,Id:int):
    query=db.query(Chefs)
    query.filter(Chefs.id==Id)
    db.delete(query)
    db.commit
    return query.all()


    