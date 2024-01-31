from sqlalchemy.orm.session import Session
from schemas.schemas import Recipe_Base
from Models import Recipes,Recipe_ingredients,RecipeReview
from typing import Optional

def Create_Recipes(db: Session, request: Recipe_Base):
    New_Recipe= Recipes(
        Name= request.Name,
        Desc=request.Desc,
        Category= request.Category,
        Rating= request.Rating,
        Rating_No= request.rating_no,
        Vegan=request.Vegan,
        Duration= request.Duration
    )

    db.add(New_Recipe)
    db.commit()
    db.refresh(New_Recipe)
    return New_Recipe

def Get_all_Recipe(db:Session):
    return db.query(Recipes).all()

def get_Recipe(db:Session,Id:int):
    return db.query(Recipes).filter(Recipes.id==Id)


def Update_User(
        db:Session,
        Recipe_ID:int,
        request:Recipe_Base
        ):
    query = db.query(Recipes)
    query.filter(Recipes.id==Recipe_ID)
    query.update
    ({
        Recipes.Name:request.Name,
        Recipes.Desc:request.Desc,
        Recipes.Category:request.Category,
        Recipes.Rating:request.Rating,
        Recipes.Rating_no:request.rating_no,
        Recipes.Vegan:request.Vegan,
        Recipes.Duration:request.Duration
    })
    db.commit()
    return query.all()

#delete recipe
    
def delete_User(db:Session,Id:int):
    query1=db.query(Recipes).filter(Recipes.id==Id)
    query2=db.query(Recipe_ingredients).filter(Recipe_ingredients.Recipe_Id==Id).all()
    query3=db.query(RecipeReview).filter(RecipeReview.Recipe_Id==Id).all()
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
    
  


    