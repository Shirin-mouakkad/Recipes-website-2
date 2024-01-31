from sqlalchemy.orm.session import Session
from schemas.schemas import User_Base, User_Display
from DB.Models import Users,RecipeReview,ChefsReview
from typing import Optional
from DB.hash import Hash

def Create_User(db: Session, request: User_Base):
    New_User= Users(
        User_Firstname=request.Firstname,
        User_Lasttname=request.Lasttname,
        Photo=request.Photo,
        Password=Hash.bcrypt(request.Password),
        Email=request.Email
    )

    db.add(New_User)
    db.commit()
    db.refresh(New_User)
    return New_User

def Get_all_Users(db:Session):
    return db.query(Users).all()

def get_User(db:Session,Id:int):
    return db.query(Users).filter(Users.id==Id)


def Update_User(
        db:Session,
        User_ID:int,
        request:User_Base
        ):
    query = db.query(Users)
    query.filter(Users.id==User_ID)
    query.update
    ({
        Users.Firstname:request.Firstname,
        Users.Lasttname:request.Lasttname,
        Users.Email:request.Email
    })
    db.commit()
    return query.all()
    
def delete_User(db:Session,Id:int):
    query1=db.query(Users).filter(Users.id==Id).first()
    query2=db.query(RecipeReview).filter(RecipeReview.User_ID==Id).all()
    query3=db.query(ChefsReview).filter(ChefsReview.User_ID==Id).all()
    try:
        for i in query2:
            db.delete(i)
        for j in query3:
            db.delete(j)
        db.delete(query1)
        db.commit()
        return 'OK'
    except:
        db.rollback()
        return 'not ok'
    


    