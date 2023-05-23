from sqlite3worker import Sqlite3Worker
from dataclasses import dataclass
from typing import Union
from datetime import datetime, timedelta

from passlib.hash import sha256_crypt
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

global database
database = None

def GenerateDatabase() -> None:
    global database
    if not os.path.exists("database.db"):
        database = Sqlite3Worker("database.db")
        database.execute("CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

        database.execute("CREATE TABLE token (id INTEGER PRIMARY KEY AUTOINCREMENT, userID INTEGER, accessToken TEXT, refreshToken TEXT, expiration TEXT)")

        database.execute("CREATE TABLE component (id INTEGER PRIMARY KEY AUTOINCREMENT, userID INTEGER, name TEXT)")

        database.execute("CREATE TABLE unite (id INTEGER PRIMARY KEY AUTOINCREMENT, componentID INTEGER, name TEXT)")

        database.execute("CREATE TABLE measure (id INTEGER PRIMARY KEY AUTOINCREMENT, uniteID INTEGER, value TEXT, datetime TEXT)")
    else:
        database = Sqlite3Worker("database.db")
    return

def Chiffrement(password: str) -> str:
    return sha256_crypt.hash(password)
def Compare(password: str, hash: str) -> bool:
    return sha256_crypt.verify(password, hash)

def GenerateToken(userID: int) -> str:
    return sha256_crypt.hash(str(userID) + str(datetime.now()))


@dataclass
class UserType:
    id: Union[int, None]
    username: Union[str, None]
    password: Union[str, None]

@dataclass
class TokenType:
    id: Union[int, None]
    userID: Union[int, None]
    accessToken: Union[str, None]
    refreshToken: Union[str, None]
    expiration: Union[str, None]

@dataclass
class ComponentType:
    id: Union[int, None]
    userID: Union[int, None]
    name: Union[str, None]

@dataclass
class UniteType:
    id: Union[int, None]
    componentID: Union[int, None]
    name: Union[str, None]

@dataclass
class MeasureType:
    id: Union[int, None]
    uniteID: Union[int, None]
    value: Union[str, None]
    datetime: Union[str, None]


class UserTable:
    @staticmethod
    def Insert(user: UserType) -> UserType:
        """
        Insert a new user in the database
            :param user:
            {
                "username": str,
                "password": str
            }
        """
        database.execute("INSERT INTO user (username, password) VALUES (?, ?)", [user.username, user.password])
        return UserTable.SelectBy_Username(user)[-1]

    @staticmethod
    def Update(user: UserType) -> None:
        """
        Update a user in the database
            :param user:
            {
                "id": int,  
                "username": str,
                "password": str
            }
        """
        database.execute("UPDATE user SET username = ?, password = ? WHERE id = ?", [user.username, user.password, user.id])
        return

    @staticmethod
    def Delete(user: UserType) -> None:
        """
        Delete a user in the database
            :param user:
            {
                "id": int
            }
        """
        database.execute("DELETE FROM user WHERE id = ?", [user.id])
        return

    @staticmethod
    def SelectBy_ID(user: UserType) -> list[UserType]:
        """
        Select a user in the database by id 
            :param user:
            {
                "id": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM user WHERE id = ?", [user.id])
        return [UserType(*row) for row in result]
    @staticmethod
    def SelectBy_Username(user: UserType) -> list[UserType]:
        """
        Select a user in the database by username
            :param user:
            {
                "username": str
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM user WHERE username = ?", [user.username])
        return [UserType(*row) for row in result]    
    @staticmethod
    def SelectAll() -> list[UserType]:
        result: list[tuple] = database.execute("SELECT * FROM user")
        return [UserType(*row) for row in result]

class TokenTable:
    @staticmethod
    def Insert(token: TokenType) -> TokenType:
        """
        Insert a new token in the database
            :param token:
            {
                "userID": int,
                "accessToken": str,
                "refreshToken": str,
                "expiration": str
            }
        """
        database.execute("INSERT INTO token (userID, accessToken, refreshToken, expiration) VALUES (?, ?, ?, ?)", [token.userID, token.accessToken, token.refreshToken, token.expiration])
        return TokenTable.SelectBy_AccessToken(token)[-1]
    
    @staticmethod
    def Update(token: TokenType) -> None:
        """
        Update a token in the database
            :param token:
            {
                "id": int,
                "userID": int,
                "accessToken": str,
                "refreshToken": str,
                "expiration": str
            }
        """
        database.execute("UPDATE token SET userID = ?, accessToken = ?, refreshToken = ?, expiration = ? WHERE id = ?", [token.userID, token.accessToken, token.refreshToken, token.expiration, token.id])
        return
    
    @staticmethod
    def Delete(token: TokenType) -> None:
        """
        Delete a token in the database
            :param token:
            {
                "id": int
            }
        """
        database.execute("DELETE FROM token WHERE id = ?", [token.id])
        return
    
    @staticmethod
    def SelectBy_ID(token: TokenType) -> list[TokenType]:
        """
        Select a token in the database by id
            :param token:
            {
                "id": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM token WHERE id = ?", [token.id])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_UserID(token: TokenType) -> list[TokenType]:
        """
        Select a token in the database by userID
            :param token:
            {
                "userID": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM token WHERE userID = ?", [token.userID])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_AccessToken(token: TokenType) -> list[TokenType]:
        """
        Select a token in the database by accessToken
            :param token:
            {
                "accessToken": str
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM token WHERE accessToken = ?", [token.accessToken])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_RefreshToken(token: TokenType) -> list[TokenType]:
        """
        Select a token in the database by refreshToken
            :param token:
            {
                "refreshToken": str
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM token WHERE refreshToken = ?", [token.refreshToken])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_Expiration(token: TokenType) -> list[TokenType]:
        """
        Select a token in the database by expiration
            :param token:
            {
                "expiration": str
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM token WHERE expiration = ?", [token.expiration])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[TokenType]:
        result: list[tuple] = database.execute("SELECT * FROM token")
        return [TokenType(*row) for row in result]

class ComponentTable:
    @staticmethod
    def Insert(component: ComponentType) -> ComponentType:
        """
        Insert a new component in the database
            :param component:
            {
                "userID": int,
                "name": str
            }
        """
        database.execute("INSERT INTO component (userID, name) VALUES (?, ?)", [component.userID, component.name])
        return ComponentTable.SelectBy_Name(component)[-1]
    
    @staticmethod
    def Update(component: ComponentType) -> None:
        """
        Update a component in the database
            :param component:
            {
                "id": int,
                "userID": int,
                "name": str
            }
        """
        database.execute("UPDATE component SET userID = ?, name = ? WHERE id = ?", [component.userID, component.name, component.id])
        return
    
    @staticmethod
    def Delete(component: ComponentType) -> None:
        """
        Delete a component in the database
            :param component:
            {
                "id": int
            }
        """
        database.execute("DELETE FROM component WHERE id = ?", [component.id])
        return
    
    @staticmethod
    def SelectBy_ID(component: ComponentType) -> list[ComponentType]:
        """
        Select a component in the database by id
            :param component:
            {
                "id": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM component WHERE id = ?", [component.id])
        return [ComponentType(*row) for row in result]
    @staticmethod
    def SelectBy_UserID(component: ComponentType) -> list[ComponentType]:
        """
        Select a component in the database by userID
            :param component:
            {
                "userID": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM component WHERE userID = ?", [component.userID])
        return [ComponentType(*row) for row in result]
    @staticmethod
    def SelectBy_Name(component: ComponentType) -> list[ComponentType]:
        """
        Select a component in the database by name
            :param component:
            {
                "name": str
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM component WHERE name = ?", [component.name])
        return [ComponentType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[ComponentType]:
        result: list[tuple] = database.execute("SELECT * FROM component")
        return [ComponentType(*row) for row in result]

class UniteTable:
    @staticmethod
    def Insert(unite: UniteType) -> UniteType:
        """
        Insert a new measure in the database
            :param measure:
            {
                "componentID": int,
                "name": str
            }
        """
        database.execute("INSERT INTO unite (componentID, name) VALUES (?, ?)", [unite.componentID, unite.name])
        return UniteTable.SelectBy_Name(unite)[-1]
    
    @staticmethod
    def Update(unite: UniteType) -> None:
        """
        Update a measure in the database
            :param measure:
            {
                "id": int,
                "componentID": int,
                "name": str
            }
        """
        database.execute("UPDATE unite SET componentID = ?, name = ? WHERE id = ?", [unite.componentID, unite.name, unite.id])
        return
    
    @staticmethod
    def Delete(unite: UniteType) -> None:
        """
        Delete a measure in the database
            :param measure:
            {
                "id": int
            }
        """
        database.execute("DELETE FROM unite WHERE id = ?", [unite.id])
        return
    
    @staticmethod
    def SelectBy_ID(unite: UniteType) -> list[UniteType]:
        """
        Select a measure in the database by id
            :param measure:
            {
                "id": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM unite WHERE id = ?", [unite.id])
        return [UniteType(*row) for row in result]
    @staticmethod
    def SelectBy_ComponentID(unite: UniteType) -> list[UniteType]:
        """
        Select a measure in the database by componentID
            :param measure:
            {
                "componentID": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM unite WHERE componentID = ?", [unite.componentID])
        return [UniteType(*row) for row in result]
    @staticmethod
    def SelectBy_Name(unite: UniteType) -> list[UniteType]:
        """
        Select a measure in the database by name
            :param measure:
            {
                "name": str
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM unite WHERE name = ?", [unite.name])
        return [UniteType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[UniteType]:
        result: list[tuple] = database.execute("SELECT * FROM unite")
        return [UniteType(*row) for row in result]

class MeasureTable:
    @staticmethod
    def Insert(measure: MeasureType) -> MeasureType:
        """
        Insert a new measure in the database
            :param measure:
            {
                "uniteID": int,
                "value": float,
                "datetime": datetime
            }
        """
        database.execute("INSERT INTO measure (uniteID, value, datetime) VALUES (?, ?, ?)", [measure.uniteID, measure.value, measure.datetime])
        return MeasureTable.SelectBy_UniteID(measure)[-1]
    
    @staticmethod
    def Update(measure: MeasureType) -> None:
        """
        Update a measure in the database
            :param measure:
            {
                "id": int,
                "uniteID": int,
                "value": float,
                "datetime": datetime
            }
        """
        database.execute("UPDATE measure SET uniteID = ?, value = ?, datetime = ? WHERE id = ?", [measure.uniteID, measure.value, measure.datetime, measure.id])
        return
    
    @staticmethod
    def Delete(measure: MeasureType) -> None:
        """
        Delete a measure in the database
            :param measure:
            {
                "id": int
            }
        """
        database.execute("DELETE FROM measure WHERE id = ?", [measure.id])
        return
    
    @staticmethod
    def SelectBy_ID(measure: MeasureType) -> list[MeasureType]:
        """
        Select a measure in the database by id
            :param measure:
            {
                "id": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM measure WHERE id = ?", [measure.id])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_UniteID(measure: MeasureType) -> list[MeasureType]:
        """
        Select a measure in the database by uniteID
            :param measure:
            {
                "uniteID": int
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM measure WHERE uniteID = ?", [measure.uniteID])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_Value(measure: MeasureType) -> list[MeasureType]:
        """
        Select a measure in the database by value
            :param measure:
            {
                "value": float
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM measure WHERE value = ?", [measure.value])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_Date(measure: MeasureType) -> list[MeasureType]:
        """
        Select a measure in the database by date
            :param measure:
            {
                "datetime": datetime
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM measure WHERE datetime = ?", [measure.datetime])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[MeasureType]:
        result: list[tuple] = database.execute("SELECT * FROM measure")
        return [MeasureType(*row) for row in result]
    
    @staticmethod
    def SelectBy_DateRange(dateMin: datetime, dateMax: datetime) -> list[MeasureType]:
        """
        Select a measure in the database by date
            :param measure:
            {
                "datetime": datetime
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM measure WHERE datetime BETWEEN ? AND ?", [dateMin, dateMax])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_DateRange_UniteID(dateMin: datetime, dateMax: datetime, measure: MeasureType) -> list[MeasureType]:
        """
        Select a measure in the database by date
            :param measure:
            {
                "datetime": datetime
            }
        """
        result: list[tuple] = database.execute("SELECT * FROM measure WHERE datetime BETWEEN ? AND ? AND uniteID = ?", [dateMin, dateMax, measure.uniteID])
        return [MeasureType(*row) for row in result]
