# SimpleAPI

SimpleAPI is a restful API provids simple service that stores and returns configurations using FastAPI and PostgreSQL.

The entire API is contained within the `app` folder.

`tests_runner.sh` runs command line script that provids you tests instructions (if you want to run tests inside docker please take a look at tests instructions below).

All stuffs `dockerized` (build instructions described below).

<br>

# Endpoints and config schema

| Name   | Method      | URL
| ---    | ---         | ---
| List   | `GET` | `/configs` 
| Create | `POST` | `/configs` 
| Get    | `GET` | `/configs/{name}` 
| Update | `PUT` | `/configs/{name}` 
| Delete | `DELETE` | `/configs/{name}` 

#### Schema

* **Config**
  + Name (string of length no more than 120 characters)
  + Metadata (nested key:value pairs where both key and value are strings of length no more than 160 characters)

---

## `GET /configs` 

### Request

    $ curl -X GET "http://localhost:5057/configs" -H "accept: application/json"

### Response

#### if no configs added yet :
```shell  
status code 200

``` 
response headers:
```shell
content-length: 19 
content-type: application/json 
date: Tue, 06 Jan 2020 10:40:11 GMT 
server: uvicorn 
```

response body:

``` shell
{"Configs":"Empty"}
```

#### else :

```shell  
status code 200

``` 
response headers:
```shell
content-length: 256 
content-type: application/json 
date: Tue, 06 Jan 2020 10:47:28 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "Configs": [
    {
      "name": "datacenter-1",
      "metadatac": {
        "monitoring": {
          "enabled": "true"
        },
        "limits": {
          "cpu": {
            "enabled": "false",
            "value": "300m"
          }
        }
      }
    },
    {
      "name": "datacenter-2",
      "metadatac": {
        "monitoring": {
          "enabled": "true"
        },
        "limits": {
          "cpu": {
            "enabled": "true",
            "value": "250m"
          }
        }
      }
    }
  ]
}
```

---

## `POST /configs` 

### Request

Create a new config: 

    $ curl -X POST "http://localhost:5057/configs" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"datacenter-1\",\"metadata\":{\"monitoring\":{\"enabled\":\"true\"},\"limits\":{\"cpu\":{\"enabled\":\"false\",\"value\":\"300m\"}}}}"

### Response

#### None-exists name :
```shell  
status code 200

``` 
response headers:
```shell
content-length: 147 
content-type: application/json 
date: Tue, 06 Jan 2020 10:49:52 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "New config has created": {
    "name": "datacenter-1",
    "metadata": {
      "monitoring": {
        "enabled": "true"
      },
      "limits": {
        "cpu": {
          "enabled": "false",
          "value": "300m"
        }
      }
    }
  }
}
```

#### Exists name :

```shell 
status code 400

``` 
response headers:
```shell
content-length: 32 
content-type: application/json 
date: Tue, 06 Jan 2020 10:52:48 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "detail": "name already exists"
}
```

---

## `GET /configs/{name}` 

### Request

    $ curl -X GET "http://localhost:5057/configs/datacenter-1" -H "accept: application/json"

### Response

#### Exists name :

``` shell
status code 200
```

response headers:

``` shell
content-length: 132 
content-type: application/json 
date: Tue, 06 Jan 2020 10:54:17 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "Config": {
    "name": "datacenter-1",
    "metadatac": {
      "monitoring": {
        "enabled": "true"
      },
      "limits": {
        "cpu": {
          "enabled": "false",
          "value": "300m"
        }
      }
    }
  }
}
```

#### None-exists name :

```shell 
status code 404

``` 
response headers:
```shell
content-length: 32 
content-type: application/json 
date: Tue, 06 Jan 2020 10:56:26 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "detail": "name doesn't exists"
}
```

---

## `UPDATE /configs/{name}` 

### Request

Update specific config:

    curl -X PUT "http://localhost:5057/configs/datacenter-1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"monitoring\":{\"enabled\":\"true\"},\"limits\":{\"cpu\":{\"enabled\":\"false\",\"value\":\"300m\"}}}"

### Response

#### Exists name :

``` shell
status code: 200
```

response headers:

``` shell
content-length: 147 
content-type: application/json 
date: Tue, 06 Jan 2020 10:57:55 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "The config has updated": {
    "name": "datacenter-1",
    "metadata": {
      "monitoring": {
        "enabled": "true"
      },
      "limits": {
        "cpu": {
          "enabled": "false",
          "value": "300m"
        }
      }
    }
  }
}
```

#### None-exists name : 

```shell 
status code: 404

``` 
response headers:
```shell
content-length: 32 
content-type: application/json 
date: Tue, 06 Jan 2020 10:59:26 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "detail": "name doesn't exists"
}
```

---

## `Delete /configs/{name}` 

### Request

    $ curl -X DELETE "http://127.0.0.1:5057/configs/datacenter-1" -H "accept: application/json"

### Response

#### Exists name :

``` shell
status code: 200
```

response headers:

``` shell
content-length: 50 
content-type: application/json 
date: Tue, 07 Jan 2020 06:03:48 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "The config has deleted": {
    "name": "datacenter-1"
  }
}
```

#### None-exists name : 

```shell 
status code: 404

``` 
response headers:
```shell
content-length: 32 
content-type: application/json 
date: Tue, 07 Jan 2020 06:06:27 GMT 
server: uvicorn 
```

response body:

``` shell
{
  "detail": "name doesn't exists"
}
```

---

## Swagger UI documentation

* #### Swagger UI powerd by openAPI (tests include) @ **/docs** endpoint ( http://localhost:5057/docs )
* #### Swagger UI powred by redoc @ **/redoc** endpoint ( http://localhost:5057/redoc )

<br>

# Dockerizing the app

### Prerequisites:

* docker 
* docker-compose

### Build the image and run docker-compose services

``` shell
$ docker-compose up
```

<br>

# Tests

### Types:

* Unit tests
* Integration tests

### Run instructions:

# **TODO**

