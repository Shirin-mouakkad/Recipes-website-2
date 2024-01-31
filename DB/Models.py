from DB.Database import Base
from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy import UniqueConstraint,PrimaryKeyConstraint,ForeignKey
from sqlalchemy.orm.relationships import Relationship


class Chefs(Base):
  __tablename__ = 'Chefs'
  id = Column(Integer, primary_key=True, index=True)
  Chef_Firstname = Column(String)
  Chef_Lasttname= Column(String)
  Nationality = Column(String)
  Photo = Column(String)
  Password = Column(String)
  Rating= Column(Integer)
  rating_no= Column(Integer)
  Recipes=Relationship('Recipes',back_populates='Chef')
  ChefReviews=Relationship('ChefsReview',back_populates='Chef')


class Users(Base):
  __tablename__ = 'Users'
  id = Column(Integer, primary_key=True, index=True)
  Firstname = Column(String)
  Lasttname= Column(String)
  Photo = Column(String)
  Password = Column(String)
  Email=Column(String )
  RecipeReviews= Relationship('RecipeReview',back_populates='User')
  ChefsReviews= Relationship('ChefsReview',back_populates='User')

class Admin(Base):
  __tablename__ = 'Admin'
  id = Column(Integer, primary_key=True, index=True)
  Name = Column(String)
  Photo = Column(String)
  Password = Column(String)
  Email = Column(String)

class RecipeReview(Base):
  __tablename__ = 'Recipe Review'
  id = Column(Integer, primary_key=True, index=True)
  Review = Column(String)
  Recipe_Id= Column(Integer, ForeignKey('Recipes.id'))
  User_ID= Column(Integer,ForeignKey('Users.id'))
  Rating= Column(Integer)
  __table_args__ = (UniqueConstraint('User_ID','Recipe_Id'),)
  User=Relationship("Users",back_populates='RecipeReviews')
  Recipe=Relationship("Recipes",back_populates='RecipeReview')

class ChefsReview(Base):
  __tablename__ = 'Chefs Review'
  id = Column(Integer, primary_key=True, index=True)
  Chef_Id= Column(Integer,ForeignKey('Chefs.id'))
  User_ID= Column(Integer,ForeignKey('Users.id'))
  Rating= Column(Integer)
  __table_args__ = (UniqueConstraint('User_ID','Chef_Id'),)
  User=Relationship('Users',back_populates='ChefsReviews')
  Chef=Relationship('Chefs',back_populates='ChefsReviews')

class Recipe_ingrediants(Base):
  __tablename__ = 'Recipe_ingrediants'
  id=Column(Integer,primary_key=True,index=True,autoincrement=True)
  Recipe_Id= Column(Integer,ForeignKey('Recipes.id'))
  ingrediant_ID= Column(Integer, ForeignKey('Ingrediants.id'))
  __table_args__ = (UniqueConstraint('Recipe_Id','ingrediant_ID'),)
  Recipe=Relationship("Recipes",back_populates='Ingrediants')
  Ingrediant=Relationship("Ingrediants",back_populates='Ingrediants_Recipe')

class Ingrediants(Base):
  __tablename__ = 'Ingrediants'
  id = Column(Integer, primary_key=True, index=True)
  Ingrediants = Column(String)
  Category= Column(String)   
  Ingrediants_Recipe=Relationship("Recipe_ingrediants",back_populates='Ingrediant') 

class Recipes(Base):
  __tablename__ = 'Recipes'
  id = Column(Integer, primary_key=True, index=True)
  Name = Column(String)
  Desc= Column(String)
  Category = Column(String)
  Rating = Column(Integer)
  Rating_no = Column(Integer)
  Vegan= Column(Boolean)
  Duration= Column(String)
  Chef_Id=Column(Integer, ForeignKey('Chefs.id'))
  Chef=Relationship('Chefs',back_populates='Recipes')
  Ingrediants=Relationship("Recipe_ingrediants",back_populates='Recipe')
  RecipeReview=Relationship("RecipeReview",back_populates='Recipe')