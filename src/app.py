import fastapi
import os
import uvicorn
from dataclasses import dataclass
import datetime
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    from .database import Database as db
except:
    from database import Database as db
    
app = fastapi.FastAPI()
db.GenerateDatabase()

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, db.UserType):
            return {
                "id": obj.id,
                "username": obj.username,
                "password": obj.password
            }
        if isinstance(obj, db.TokenType):
            return {
                "id": obj.id,
                "userID": obj.userID,
                "accessToken": obj.accessToken,
                "refreshToken": obj.refreshToken,
                "expiration": obj.expiration
            }
        if isinstance(obj, db.ComponentType):
            return {
                "id": obj.id,
                "name": obj.name,
                "userID": obj.userID
            }
        if isinstance(obj, db.UniteType):
            return {
                "id": obj.id,
                "name": obj.name,
                "componentID": obj.componentID
            }
        if isinstance(obj, db.MeasureType):
            return {
                "id": obj.id,
                "value": obj.value,
                "uniteID": obj.uniteID,
                "datetime": obj.datetime
            }
        return super().default(obj)

@app.get("/")
def Index():
    return fastapi.Response(status_code=200, content="Hello World !")

@app.post("/api/user/register/")
def UserRegister(user: db.UserType):
    """
    Register a new user
        :param user:
        {
            "username": str,
            "password": str
        }

    """
    if len(db.UserTable.SelectBy_Username(user)) > 0:
        return fastapi.Response(status_code=401)
    
    user.password = db.Chiffrement(user.password)
    db.UserTable.Insert(user)
    return fastapi.Response(status_code=201)

@app.post("/api/user/login/")
def UserLogin(user: db.UserType):
    """
    Login a user
        :param user:
        {
            "username": str,
            "password": str
        }

    """
    if len(db.UserTable.SelectBy_Username(user)) == 0:
        return fastapi.Response(status_code=404)

    if len(db.UserTable.SelectBy_Username(user)) > 1:
        return fastapi.Response(status_code=500)

    if not db.Compare(user.password, db.UserTable.SelectBy_Username(user)[0].password):
        return fastapi.Response(status_code=401)
    
    # Suppression des anciens tokens
    for token in db.TokenTable.SelectBy_UserID(db.TokenType(userID=db.UserTable.SelectBy_Username(user)[0].id)):
        db.TokenTable.Delete(token)

    # Création des nouveaux tokens
    token: db.TokenType = db.TokenType(
        userID=db.UserTable.SelectBy_Username(user)[0].id,
        accessToken=db.GenerateToken(db.UserTable.SelectBy_Username(user)[0].id),
        refreshToken=db.GenerateToken(db.UserTable.SelectBy_Username(user)[0].id),
        expiration=(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    )
    db.TokenTable.Insert(token)
    return fastapi.Response(status_code=200, content=json.dumps({"accessToken": token.accessToken, "refreshToken": token.refreshToken}, cls=JsonEncoder))

@app.post("/api/user/refresh/")
def UserRefresh(token: db.TokenType):
    """
    Refresh a user token
        :param token:
        {
            "refreshToken": str
        }

    """
    if len(db.TokenTable.SelectBy_RefreshToken(token)) == 0:
        return fastapi.Response(status_code=404)

    if len(db.TokenTable.SelectBy_RefreshToken(token)) > 1:
        return fastapi.Response(status_code=500)

    user = db.UserTable.SelectBy_ID(db.UserType(id=db.TokenTable.SelectBy_RefreshToken(token)[0].userID))[0]

    # Suppression des anciens tokens
    for token in db.TokenTable.SelectBy_UserID(db.TokenType(userID=user.id)):
        db.TokenTable.Delete(token)

    # Création des nouveaux tokens
    token: db.TokenType = db.TokenType(
        userID=user.id,
        accessToken=db.GenerateToken(user.id),
        refreshToken=token.refreshToken,
        expiration=(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    )
    db.TokenTable.Insert(token)
    return fastapi.Response(status_code=200, content=json.dumps({"accessToken": token.accessToken, "refreshToken": token.refreshToken}))





@app.post("/api/components/")
def ComponentsGetAll(token: db.TokenType):
    """
    Get all components
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    return fastapi.Response(status_code=200, content=json.dumps(db.ComponentTable.SelectAll(), cls=JsonEncoder))

@app.post("/api/components/{id}")
def ComponentsGetByID(id: int, token: db.TokenType):
    """
    Get a component by id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    if len(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))) == 0:
        return fastapi.Response(status_code=404)

    if len(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))) > 1:
        return fastapi.Response(status_code=500)

    return fastapi.Response(status_code=200, content=json.dumps(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))[0].__dict__, cls=JsonEncoder))


@app.post("/api/components/add/")
def ComponentsAdd(token: db.TokenType, component: db.ComponentType):
    """
    Add a component
        :param token:
        {
            "accessToken": str,
        }
        :param component:
        {
            "name": str,
            "description": str,
            "price": float,
            "quantity": int
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    db.ComponentTable.Insert(component)
    return fastapi.Response(status_code=201)

@app.post("/api/components/delete/{id}")
def ComponentsDelete(id: int, token: db.TokenType):
    """
    Delete a component by id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    if len(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))) == 0:
        return fastapi.Response(status_code=404)

    if len(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))) > 1:
        return fastapi.Response(status_code=500)

    db.ComponentTable.Delete(db.ComponentType(id=id))
    return fastapi.Response(status_code=200)





@app.post("/api/unites/")
def UnitesGetAll(token: db.TokenType):
    """
    Get all unites
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    return fastapi.Response(status_code=200, content=json.dumps(db.UniteTable.SelectAll(), cls=JsonEncoder))

@app.post("/api/unites/{id}")
def UnitesGetByID(id: int, token: db.TokenType):
    """
    Get a unite by id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    if len(db.UniteTable.SelectBy_ID(db.UniteType(id=id))) == 0:
        return fastapi.Response(status_code=404)

    if len(db.UniteTable.SelectBy_ID(db.UniteType(id=id))) > 1:
        return fastapi.Response(status_code=500)

    return fastapi.Response(status_code=200, content=json.dumps(db.UniteTable.SelectBy_ID(db.UniteType(id=id))[0].__dict__, cls=JsonEncoder))

@app.post("/api/unites/component/{id}")
def UnitesGetByComponentID(id: int, token: db.TokenType):
    """
    Get a unite by component id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)


    if len(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))) == 0:
        return fastapi.Response(status_code=404)

    if len(db.ComponentTable.SelectBy_ID(db.ComponentType(id=id))) > 1:
        return fastapi.Response(status_code=500)

    return fastapi.Response(status_code=200, content=json.dumps(db.UniteTable.SelectBy_ComponentID(db.ComponentType(id=id)), cls=JsonEncoder))


@app.post("/api/unites/add/")
def UnitesAdd(token: db.TokenType, unite: db.UniteType):
    """
    Add a unite
        :param token:
        {
            "accessToken": str,
        }
        :param unite:
        {
            "name": str,
            "componentID": int
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    db.UniteTable.Insert(unite)
    return fastapi.Response(status_code=201)

@app.post("/api/unites/delete/{id}")
def UnitesDelete(id: int, token: db.TokenType):
    """
    Delete a unite by id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    if len(db.UniteTable.SelectBy_ID(db.UniteType(id=id))) == 0:
        return fastapi.Response(status_code=404)

    if len(db.UniteTable.SelectBy_ID(db.UniteType(id=id))) > 1:
        return fastapi.Response(status_code=500)

    db.UniteTable.Delete(db.UniteType(id=id))
    return fastapi.Response(status_code=200)





@app.post("/api/measures/")
def MeasuresGetAll(token: db.TokenType):
    """
    Get all measures
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)
    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)
    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)
    return fastapi.Response(status_code=200, content=json.dumps(db.MeasureTable.SelectAll(), cls=JsonEncoder))

@app.post("/api/measures/{id}")
def MeasuresGetByID(id: int, token: db.TokenType):
    """
    Get a measure by id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)
    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)
    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)
    if len(db.MeasureTable.SelectBy_ID(db.MeasureType(id=id))) == 0:
        return fastapi.Response(status_code=404)
    if len(db.MeasureTable.SelectBy_ID(db.MeasureType(id=id))) > 1:
        return fastapi.Response(status_code=500)
    return fastapi.Response(status_code=200, content=json.dumps(db.MeasureTable.SelectBy_ID(db.MeasureType(id=id))[0].__dict__), cls=JsonEncoder)

@app.post("/api/measures/unite/{id}")
def MeasuresGetByUniteID(id: int, token: db.TokenType):
    """
    Get a measure by unite id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)
    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)
    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)
    if len(db.UniteTable.SelectBy_ID(db.UniteType(id=id))) == 0:
        return fastapi.Response(status_code=404)
    if len(db.UniteTable.SelectBy_ID(db.UniteType(id=id))) > 1:
        return fastapi.Response(status_code=500)
    return fastapi.Response(status_code=200, content=json.dumps(db.MeasureTable.SelectBy_UniteID(db.UniteType(id=id)), cls=JsonEncoder))

@app.post("/api/measures/add/")
def MeasuresAdd(token: db.TokenType, measure: db.MeasureType):
    """
    Add a measure
        :param token:
        {
            "accessToken": str,
        }
        :param measure:
        {
            "name": str,
            "description": str,
            "uniteID": int
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    db.MeasureTable.Insert(measure)
    return fastapi.Response(status_code=201)

@app.post("/api/measures/delete/{id}")
def MeasuresDelete(id: int, token: db.TokenType):
    """
    Delete a measure by id
        :param id: int
        :param token:
        {
            "accessToken": str,
        }

    """
    if len(db.TokenTable.SelectBy_AccessToken(token)) == 0:
        return fastapi.Response(status_code=401)

    if len(db.TokenTable.SelectBy_AccessToken(token)) > 1:
        return fastapi.Response(status_code=500)

    if db.TokenTable.SelectBy_AccessToken(token)[0].expiration < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return fastapi.Response(status_code=401)

    if len(db.MeasureTable.SelectBy_ID(db.MeasureType(id=id))) == 0:
        return fastapi.Response(status_code=404)

    if len(db.MeasureTable.SelectBy_ID(db.MeasureType(id=id))) > 1:
        return fastapi.Response(status_code=500)

    db.MeasureTable.Delete(db.MeasureType(id=id))
    return fastapi.Response(status_code=200)
