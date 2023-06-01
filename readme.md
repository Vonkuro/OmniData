# API

## User
### Register
#### Request
```
POST /api/user/register/

{
    "username": "username",
    "password": "password"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Username already exists"
}

201 Created
{
    "message": "User created"
}
``` 

### Login
#### Request
```
POST /api/user/login/

{
    "username": "username",
    "password": "password"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid username or password"
}

200 OK
{
    "accessToken":"token",
    "refreshToken":"token"
}
```

### Refresh Token
#### Request
```
POST /api/user/refresh/

{
    "refreshToken":"token"
}
```
#### Response
```
404 Not Found
{
    "message": "Refresh token not found"
}

200 OK
{
    "accessToken":"token",
    "refreshToken":"token"
}
```



## Components 
### Get all components from user
```
POST /api/components/
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

200 OK
{
    "components": [
        {
            "id": 1,
            "userID": 1,
            "name": "Component 1"
        },
        {
            "id": 2,
            "userID": 1,
            "name": "Component 2"
        }
    ]
}
```

### Get component by id
```
POST /api/components/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Component not found"
}

200 OK
{
    "id": 1,
    "name": "Component 1",
    "userID": 1
}
```

### Create component
```
POST /api/components/add/
{
    "token":{
        "accessToken":"token"
    },
    "component":{
        "name": "Component 1"
    }
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

201 Created
{
    "message": "Component created"
}
```

### Delete component
```
POST /api/components/delete/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Component not found"
}

200 OK
{
    "message": "Component deleted"
}
```


## Unite
### Get all unites from user
```
POST /api/unites/
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

200 OK
{
    "unites": [
        {
            "id": 1,
            "name": "Unite 1",
            "componentID": 1
        },
        {
            "id": 2,
            "name": "Unite 2",
            "componentID": 1
        }
    ]
}
```

### Get unite by id
```
POST /api/unites/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Unite not found"
}

200 OK
{
    "id": 1,
    "name": "Unite 1",
    "componentID": 1
}
```

### Get unite by component id
```
POST /api/unites/component/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Unite not found"
}

200 OK
{
    "id": 1,
    "name": "Unite 1",
    "componentID": 1
}
```

### Create unite
```
POST /api/unites/add/
{
    "token":{
        "accessToken":"token"
    },
    "unite":{
        "name": "Unite 1",
        "componentID": "1
    }
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

201 Created
{
    "message": "Unite created"
}
```

### Delete unite
```
POST /api/unites/delete/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Unite not found"
}

200 OK
{
    "message": "Unite deleted"
}
```

## Measures
### Get all measures from user
```
POST /api/measures/
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

200 OK
{
    "measures": [
        {
            "id": 1,
            "uniteID": 1,
            "value": 1.0,
            "datetime": "2021-01-01 00:00:00
        },
        {
            "id": 2,
            "uniteID": 1,
            "value": 2.0,
            "datetime": "2021-01-01 00:00:00
        }
    ]
}
```

### Get measure by id
```
POST /api/measures/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Measure not found"
}

200 OK
{
    "id": 1,
    "uniteID": 1,
    "value": 1.0,
    "datetime": "2021-01-01 00:00:00
}
```

### Get measure by unite id
```
POST /api/measures/unite/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Measure not found"
}

200 OK
{
    "id": 1,
    "uniteID": 1,
    "value": 1.0,
    "datetime": "2021-01-01 00:00:00
}
```

### Create measure
```
POST /api/measures/add/
{
    "token":{
        "accessToken": "token"
    },
    "measure":{
        "uniteID": 1,
        "value": 1.0,
        "datetime": "2021-01-01 00:00:00
    }
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

201 Created
{
    "message": "Measure created"
}
```

### Delete measure
```
POST /api/measures/delete/:id
{
    "accessToken":"token"
}
```
#### Response
```
401 Unauthorized
{
    "message": "Invalid token"
}

404 Not Found
{
    "message": "Measure not found"
}

200 OK
{
    "message": "Measure deleted"
}
```
