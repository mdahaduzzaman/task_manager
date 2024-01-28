# README

Welcome to TASK MANAGER

![Task-manager](/static/images/task-manager-login.PNG)

Start by cloning the repositories:

```
git clone https://github.com/mdahaduzzaman/task_manager.git
```

Then create a new virtual environment for not conflicting with others project

```
py -m venv .env_task
```

Activate the virtual environment by using the following command

```
env_task\Scripts\activate
```

Install all the dependencies by using the following command

```
pip install -r requirements.txt
```

# DATABASE CONFIGURATION

Create a new PostgreSQL Database and collect the credentials then add this credentials to the .env file 

> DB_NAME='name of the database example TASK_DB'
> DB_USER='name of the database root user example TASK_ROOT_USER'
> DB_PASSWORD='password of the root db user'
> DB_HOST='host address example localhost'
> DB_PORT='port example 5432'

And restore the attached file named **db_backup.sql** then run the following command

```
python manage.py runserver
```

The development server will start at [localhost](http://127.0.0.1:8000/)

# API ENDPOINTS

These endpoints allow you to GET all tasks, single task where each task contains multiple images and POST, PUT, PATCH a single Task at once with multiple images

## GET [http://127.0.0.1:8000/api/tasks/] 

`response` 200 OK ✅

```
[
  {
    "id": 33,
    "user": 4,
    "title": "Wash my Bikes",
    "description": "Bike is too dirty it needs to be clean within 1 tarikh",
    "due_date": "2024-02-01",
    "priority": "medium",
    "is_completed": false,
    "created_at": "2024-01-29T00:09:27.441647+06:00",
    "updated_at": "2024-01-29T00:09:27.441647+06:00",
    "images": [
      {
        "image": "http://127.0.0.1:8000/media/Tasks/Image/33_bikes.jpeg"
      }
    ]
  },
  ....
]
```

## GET [http://127.0.0.1:8000/api/tasks/33/]

`response` 200 OK ✅

```
{
  "id": 33,
  "user": 4,
  "title": "Wash my Bikes",
  "description": "Bike is too dirty it needs to be clean within 1 tarikh",
  "due_date": "2024-02-01",
  "priority": "medium",
  "is_completed": false,
  "created_at": "2024-01-29T00:09:27.441647+06:00",
  "updated_at": "2024-01-29T00:09:27.441647+06:00",
  "images": [
    {
      "image": "http://127.0.0.1:8000/media/Tasks/Image/33_bikes.jpeg"
    }
  ]
}
```

## POST [http://127.0.0.1:8000/api/tasks/]

`response` 201 CREATED ✅

```
{
  "user": 4,
  "title": "Wash my Bikes",
  "description": "Bike is too dirty it needs to be clean within 1 tarikh",
  "due_date": "2024-02-01",
  "priority": "medium",
  "is_completed": false,
  "uploaded_images": [
    > `images` is replaced by `uploaded_images` where multiple image file is upload possible
  ]
}
```


## PUT [http://127.0.0.1:8000/api/tasks/33/]

`response` 200 OK ✅

```
{
  "id": 33,
  "user": 4,
  "title": "Wash my Bikes",
  "description": "Bike is too dirty it needs to be clean within 1 tarikh",
  "due_date": "2024-02-01",
  "priority": "medium",
  "is_completed": false,
  "created_at": "2024-01-29T00:09:27.441647+06:00",
  "updated_at": "2024-01-29T00:09:27.441647+06:00",
  "uploaded_images": [
    > `images` is replaced by `uploaded_images` where multiple image file is upload possible new image is stored in db old image delete
  ]
}
```
## PATCH [http://127.0.0.1:8000/api/tasks/33/]

`response` 200 OK ✅

```
{
  "id": 33,
  "user": 4,
  "title": "Wash my Bikes",
  "description": "Bike is too dirty it needs to be clean within 1 tarikh",
  "due_date": "2024-02-01",
  "priority": "medium",
  "is_completed": false,
  "created_at": "2024-01-29T00:09:27.441647+06:00",
  "updated_at": "2024-01-29T00:09:27.441647+06:00",
  "uploaded_images": [
    > `images` is replaced by `uploaded_images` where multiple image file is upload possible new image is stored in db old image delete
  ]
}
```

## DELETE [http://127.0.0.1:8000/api/tasks/33/]

`response` 204 No Content ✅

