from passlib.context import CryptContext

pwd_Contex=CryptContext(schemes='bcrypt', deprecated='auto')

def Hash(Password: str):
    return pwd_Contex.hash(Password)

def Verify(Hashed_Password, Plain_Password):
    return pwd_Contex.verify(Plain_Password, Hashed_Password)