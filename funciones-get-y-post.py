from fastapi import FastAPI #Importamos el framework fastapi a nuestro entorno de trabajo
from pydantic import BaseModel #Importamos pydantic para obtener una entidad que pueda definir usuarios

#Creamos un objeto a partir de la clase FastAPI
app = FastAPI()

#Definimos nuestra entidad User (utilizando BaseModel):
class User (BaseModel):
    passangerid:int
    survived: int
    pclass: int
    name: str
    sex: str
    age: int

#Creamos un objeto en forma de lista con los primeros 25 registros echos a mano
users_list=  [
User(passangerid=1, survived=0, pclass=3, name='Braund, Mr. Owen Harris', sex='male', age=22),
User(passangerid=2, survived=1, pclass=1, name='Cumings, Mrs. John Bradley (Florence Briggs Thayer)', sex='female', age=38),
User(passangerid=3, survived=1, pclass=3, name='Heikkinen, Miss. Laina', sex='female', age=26),
User(passangerid=4, survived=1, pclass=1, name='Futrelle, Mrs. Jacques Heath (Lily May Peel)', sex='female', age=35),
User(passangerid=5, survived=0, pclass=3, name='Allen, Mr. William Henry', sex='male', age=35),
User(passangerid=6, survived=0, pclass=3, name='Moran, Mr. James', sex='male', age=0),
User(passangerid=7, survived=0, pclass=1, name='McCarthy, Mr. Timothy J', sex='male', age=54),
User(passangerid=8, survived=0, pclass=3, name='Palsson, Master. Gosta Leonard', sex='male', age=2),
User(passangerid=9, survived=1, pclass=3, name='Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)', sex='female', age=27),
User(passangerid=10, survived=1, pclass=2, name='Nasser, Mrs. Nicholas (Adele Achem)', sex='female', age=14),
User(passangerid=11, survived=1, pclass=3, name='Sandstrom, Miss. Marguerite Rut', sex='female', age=4),
User(passangerid=12, survived=1, pclass=1, name='Bonnell, Miss. Elizabeth', sex='female', age=58),
User(passangerid=13, survived=0, pclass=3, name='Saundercock, Mr. William Henry', sex='male', age=20),
User(passangerid=14, survived=0, pclass=3, name='Andersson, Mr. Anders Johan', sex='male', age=39),
User(passangerid=15, survived=0, pclass=3, name='Vestrom, Miss. Hulda Amanda Adolfina', sex='female', age=14),
User(passangerid=16, survived=1, pclass=2, name='Hewlett, Mrs. (Mary D Kingcome)', sex='female', age=55),
User(passangerid=17, survived=0, pclass=3, name='Rice, Master. Eugene', sex='male', age=2),
User(passangerid=18, survived=1, pclass=2, name='Williams, Mr. Charles Eugene', sex='male', age=0),
User(passangerid=19, survived=0, pclass=3, name='Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)', sex='female', age=31),
User(passangerid=20, survived=1, pclass=3, name='Masselmani, Mrs. Fatima', sex='female', age=0),
User(passangerid=21, survived=0, pclass=2, name='Fynney, Mr. Joseph J', sex='male', age=35),
User(passangerid=22, survived=1, pclass=2, name='Beesley, Mr. Lawrence', sex='male', age=34),
User(passangerid=23, survived=1, pclass=3, name='McGowan, Miss. Anna "Annie"', sex='female', age=15),
User(passangerid=24, survived=1, pclass=1, name='Sloper, Mr. William Thompson', sex='male', age=28),
User(passangerid=25, survived=0, pclass=3, name='Palsson, Miss. Torborg Danira', sex='female', age=8)
]

#Levantamos el server Uvicorn
#-uvicorn 3_crud:app --reload-

#Función Get:
@app.get("/usersclass/")
async def usersclass():
    return users_list
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/

#Función Get con Filtro Path
@app.get("/usersclass/{id}")
async def usersclass(id: int):#Esta variable tiene que ser la misma que en la línea 57
    users = filter(lambda user: user.passangerid == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

#Función Post
@app.post("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for saved_user in users_list:
        if saved_user.passangerid == user.passangerid:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
