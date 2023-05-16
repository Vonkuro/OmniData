from sqlite3worker import Sqlite3Worker
from dataclasses import dataclass
from typing import Union
from datetime import datetime, timedelta

import os

if not os.path.exists("database.db"):
    db: Sqlite3Worker = Sqlite3Worker("database.db")
    db.execute("CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

    db.execute("CREATE TABLE token (id INTEGER PRIMARY KEY AUTOINCREMENT, userID INTEGER, accessToken TEXT, refreshToken TEXT, expiration TEXT)")
    db.execute("ALTER TABLE token ADD CONSTRAINT fk_user FOREIGN KEY (userID) REFERENCES user(id)")

    db.execute("CREATE TABLE component (id INTEGER PRIMARY KEY AUTOINCREMENT, userID INTEGER, name TEXT)")
    db.execute("ALTER TABLE component ADD CONSTRAINT fk_user FOREIGN KEY (userID) REFERENCES user(id)")

    db.execute("CREATE TABLE unite (id INTEGER PRIMARY KEY AUTOINCREMENT, componentID INTEGER, name TEXT)")
    db.execute("ALTER TABLE unite ADD CONSTRAINT fk_component FOREIGN KEY (componentID) REFERENCES component(id)")

    db.execute("CREATE TABLE measure (id INTEGER PRIMARY KEY AUTOINCREMENT, uniteID INTEGER, value TEXT)")
    db.execute("ALTER TABLE measure ADD CONSTRAINT fk_unite FOREIGN KEY (uniteID) REFERENCES unite(id)")
else:
    db: Sqlite3Worker = Sqlite3Worker("database.db")


@dataclass
class UserType:
    id: Union[int, None]
    username: Union[str, None]
    password: Union[str, None]

@dataclass
class TokenType:
    id: Union[int, None]
    userID: Union[int, None]
    user: Union[UserType, None]
    accessToken: Union[str, None]
    refreshToken: Union[str, None]
    expiration: Union[str, None]

@dataclass
class ComponentType:
    id: Union[int, None]
    userID: Union[int, None]
    user: Union[UserType, None]
    name: Union[str, None]

@dataclass
class UniteType:
    id: Union[int, None]
    componentID: Union[int, None]
    component: Union[ComponentType, None]
    name: Union[str, None]

@dataclass
class MeasureType:
    id: Union[int, None]
    uniteID: Union[int, None]
    unite: Union[UniteType, None]
    value: Union[str, None]


class UserTable:
    @staticmethod
    def Insert(username: str, password: str) -> int:
        db.execute("INSERT INTO user (username, password) VALUES (?, ?)", [username, password])
        return db.lastrowid

    @staticmethod
    def Update(id: int, username: str, password: str) -> None:
        db.execute("UPDATE user SET username = ?, password = ? WHERE id = ?", [username, password, id])
        return

    @staticmethod
    def Delete(id: int) -> None:
        db.execute("DELETE FROM user WHERE id = ?", [id])
        return

    @staticmethod
    def SelectBy_ID(id: int) -> list[UserType]:
        result: list[tuple] = db.execute("SELECT * FROM user WHERE id = ?", [id])
        return [UserType(*row) for row in result]
    @staticmethod
    def SelectBy_Username(username: str) -> list[UserType]:
        result: list[tuple] = db.execute("SELECT * FROM user WHERE username = ?", [username])
        return [UserType(*row) for row in result]    
    @staticmethod
    def SelectAll() -> list[UserType]:
        result: list[tuple] = db.execute("SELECT * FROM user")
        return [UserType(*row) for row in result]

class TokenTable:
    @staticmethod
    def Insert(userID: int, accessToken: str, refreshToken: str, expiration: str) -> int:
        db.execute("INSERT INTO token (userID, accessToken, refreshToken, expiration) VALUES (?, ?, ?, ?)", [userID, accessToken, refreshToken, expiration])
        return db.lastrowid
    
    @staticmethod
    def Update(id: int, userID: int, accessToken: str, refreshToken: str, expiration: str) -> None:
        db.execute("UPDATE token SET userID = ?, accessToken = ?, refreshToken = ?, expiration = ? WHERE id = ?", [userID, accessToken, refreshToken, expiration, id])
        return
    
    @staticmethod
    def Delete(id: int) -> None:
        db.execute("DELETE FROM token WHERE id = ?", [id])
        return
    
    @staticmethod
    def SelectBy_ID(id: int) -> list[TokenType]:
        result: list[tuple] = db.execute("SELECT * FROM token WHERE id = ?", [id])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_UserID(userID: int) -> list[TokenType]:
        result: list[tuple] = db.execute("SELECT * FROM token WHERE userID = ?", [userID])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_AccessToken(accessToken: str) -> list[TokenType]:
        result: list[tuple] = db.execute("SELECT * FROM token WHERE accessToken = ?", [accessToken])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_RefreshToken(refreshToken: str) -> list[TokenType]:
        result: list[tuple] = db.execute("SELECT * FROM token WHERE refreshToken = ?", [refreshToken])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectBy_Expiration(expiration: datetime) -> list[TokenType]:
        result: list[tuple] = db.execute("SELECT * FROM token WHERE expiration = ?", [expiration])
        return [TokenType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[TokenType]:
        result: list[tuple] = db.execute("SELECT * FROM token")
        return [TokenType(*row) for row in result]


class ComponentTable:
    @staticmethod
    def Insert(userID: int, name: str) -> int:
        db.execute("INSERT INTO component (userID, name) VALUES (?, ?)", [userID, name])
        return db.lastrowid
    
    @staticmethod
    def Update(id: int, userID: int, name: str) -> None:
        db.execute("UPDATE component SET userID = ?, name = ? WHERE id = ?", [userID, name, id])
        return
    
    @staticmethod
    def Delete(id: int) -> None:
        db.execute("DELETE FROM component WHERE id = ?", [id])
        return
    
    @staticmethod
    def SelectBy_ID(id: int) -> list[ComponentType]:
        result: list[tuple] = db.execute("SELECT * FROM component WHERE id = ?", [id])
        return [ComponentType(*row) for row in result]
    @staticmethod
    def SelectBy_UserID(userID: int) -> list[ComponentType]:
        result: list[tuple] = db.execute("SELECT * FROM component WHERE userID = ?", [userID])
        return [ComponentType(*row) for row in result]
    @staticmethod
    def SelectBy_Name(name: str) -> list[ComponentType]:
        result: list[tuple] = db.execute("SELECT * FROM component WHERE name = ?", [name])
        return [ComponentType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[ComponentType]:
        result: list[tuple] = db.execute("SELECT * FROM component")
        return [ComponentType(*row) for row in result]


class UniteTable:
    @staticmethod
    def Insert(componentID: int, name: str) -> int:
        db.execute("INSERT INTO unite (componentID, name) VALUES (?, ?)", [componentID, name])
        return db.lastrowid
    
    @staticmethod
    def Update(id: int, componentID: int, name: str) -> None:
        db.execute("UPDATE unite SET componentID = ?, name = ? WHERE id = ?", [componentID, name, id])
        return
    
    @staticmethod
    def Delete(id: int) -> None:
        db.execute("DELETE FROM unite WHERE id = ?", [id])
        return
    
    @staticmethod
    def SelectBy_ID(id: int) -> list[UniteType]:
        result: list[tuple] = db.execute("SELECT * FROM unite WHERE id = ?", [id])
        return [UniteType(*row) for row in result]
    @staticmethod
    def SelectBy_ComponentID(componentID: int) -> list[UniteType]:
        result: list[tuple] = db.execute("SELECT * FROM unite WHERE componentID = ?", [componentID])
        return [UniteType(*row) for row in result]
    @staticmethod
    def SelectBy_Name(name: str) -> list[UniteType]:
        result: list[tuple] = db.execute("SELECT * FROM unite WHERE name = ?", [name])
        return [UniteType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[UniteType]:
        result: list[tuple] = db.execute("SELECT * FROM unite")
        return [UniteType(*row) for row in result]


class MeasureTable:
    @staticmethod
    def Insert(componentID: int, uniteID: int, value: float, date: datetime) -> int:
        db.execute("INSERT INTO measure (componentID, uniteID, value, date) VALUES (?, ?, ?, ?)", [componentID, uniteID, value, date])
        return db.lastrowid
    
    @staticmethod
    def Update(id: int, componentID: int, uniteID: int, value: float, date: datetime) -> None:
        db.execute("UPDATE measure SET componentID = ?, uniteID = ?, value = ?, date = ? WHERE id = ?", [componentID, uniteID, value, date, id])
        return
    
    @staticmethod
    def Delete(id: int) -> None:
        db.execute("DELETE FROM measure WHERE id = ?", [id])
        return
    
    @staticmethod
    def SelectBy_ID(id: int) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE id = ?", [id])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_ComponentID(componentID: int) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE componentID = ?", [componentID])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_UniteID(uniteID: int) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE uniteID = ?", [uniteID])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_Value(value: float) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE value = ?", [value])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_Date(date: datetime) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE date = ?", [date])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectAll() -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure")
        return [MeasureType(*row) for row in result]
    
    @staticmethod
    def SelectBy_DateRange(dateMin: datetime, dateMax: datetime) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE date BETWEEN ? AND ?", [dateMin, dateMax])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_DateRange_ComponentID(dateMin: datetime, dateMax: datetime, componentID: int) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE date BETWEEN ? AND ? AND componentID = ?", [dateMin, dateMax, componentID])
        return [MeasureType(*row) for row in result]
    @staticmethod
    def SelectBy_DateRange_UniteID(dateMin: datetime, dateMax: datetime, uniteID: int) -> list[MeasureType]:
        result: list[tuple] = db.execute("SELECT * FROM measure WHERE date BETWEEN ? AND ? AND uniteID = ?", [dateMin, dateMax, uniteID])
        return [MeasureType(*row) for row in result]
