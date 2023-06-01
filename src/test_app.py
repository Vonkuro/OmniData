import os
import datetime
import requests
import json
from fastapi import FastAPI
from fastapi.testclient import TestClient

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists("database/database.db"):
    os.remove("database/database.db")

try:
    from .app import app
except:
    from app import app

testApp = TestClient(app)

def test_create_app():
    response = testApp.get("/")
    assert response.status_code == 200
    assert response.text == "Hello World !"

def test_create_user():
    response = testApp.post("/api/user/register", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 201

    response = testApp.post("/api/user/register", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 401
def test_login_user():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test2"
    })
    assert response.status_code == 401

    response = testApp.post("/api/user/login", json={
        "username": "test2",
        "password": "test"
    })
    assert response.status_code == 404
def test_refresh_token():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    response = testApp.post("/api/user/refresh", json={
        "refreshToken": json.loads(response.text)["refreshToken"]
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    response = testApp.post("/api/user/refresh", json={
        "refreshToken": "test"
    })
    assert response.status_code == 404



def test_create_component():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/components/add/", json={
        "token":{
            "accessToken": access_token
        },
        "component":{
            "name": "test"
        }
    })
    assert response.status_code == 201
    response = testApp.post("/api/components/add/", json={
        "token":{
            "accessToken": access_token
        },
        "component":{
            "name": "test2"
        }
    })
    assert response.status_code == 201
    
    response = testApp.post("/api/components/add/", json={
        "token":{
            "accessToken": "issou"
        },
        "component":{
            "name": "test"
        }
    })
    assert response.status_code == 401
def test_getall_components():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/components", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)[0]
    assert len(json.loads(response.text)) == 2
def test_get_component_by_id():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/components/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)
    assert json.loads(response.text)["name"] == "test"
    assert json.loads(response.text)["id"] == 1

    response = testApp.post("/api/components/2", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)
    assert json.loads(response.text)["name"] == "test2"
    assert json.loads(response.text)["id"] == 2

    response = testApp.post("/api/components/3", json={
        "accessToken": access_token
    })
    assert response.status_code == 404
def test_delete_component_by_id():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/components/delete/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 200

    response = testApp.post("/api/components/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 404

    response = testApp.post("/api/components/delete/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 404




def test_create_unites():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/unites/add/", json={
        "token":{
            "accessToken": access_token
        },
        "unite":{
            "name": "test",
            "componentID": 2
        }
    })
    assert response.status_code == 201
    response = testApp.post("/api/unites/add/", json={
        "token":{
            "accessToken": access_token
        },
        "unite":{
            "name": "test2",
            "componentID": 2
        }
    })
    assert response.status_code == 201
    
    response = testApp.post("/api/unites/add/", json={
        "token":{
            "accessToken": "issou"
        },
        "unite":{
            "name": "test",
            "componentID": 2
        }
    })
    assert response.status_code == 401
def test_getall_unites():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/unites", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)[0]
    assert len(json.loads(response.text)) == 2
def test_get_unites_by_id():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/unites/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)
    assert json.loads(response.text)["name"] == "test"
    assert json.loads(response.text)["id"] == 1

    response = testApp.post("/api/unites/2", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)
    assert json.loads(response.text)["name"] == "test2"
    assert json.loads(response.text)["id"] == 2

    response = testApp.post("/api/unites/3", json={
        "accessToken": access_token
    })
    assert response.status_code == 404
def test_get_unites_by_component_id():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/unites/component/2", json={
        "accessToken": access_token
    })
    assert response.status_code == 200
    assert json.loads(response.text)[0]
    assert len(json.loads(response.text)) == 2

    response = testApp.post("/api/unites/component/9", json={
        "accessToken": access_token
    })
    assert response.status_code == 404
def test_delete_unites_by_id():
    response = testApp.post("/api/user/login", json={
        "username": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert json.loads(response.text)["accessToken"]

    access_token = json.loads(response.text)["accessToken"]

    response = testApp.post("/api/unites/delete/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 200

    response = testApp.post("/api/unites/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 404

    response = testApp.post("/api/unites/delete/1", json={
        "accessToken": access_token
    })
    assert response.status_code == 404





# if __name__ == "__main__":
#     test_create_app()
#     test_create_user()
#     test_login_user()
#     test_refresh_token()
#     test_create_component()
#     test_getall_components()
#     test_get_component_by_id()
#     test_delete_component_by_id()
#     test_create_unites()
#     test_getall_unites()
#     test_get_unites_by_id()
#     test_get_unites_by_component_id()
#     test_delete_unites_by_id()


