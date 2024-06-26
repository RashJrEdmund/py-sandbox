## Setup For basic-flask-app

- Make sure to Create a virtual environment (v-e), and install required modules as per my main [documentation](../../README.md#configuring-a-virtual-environment-v-e)

### Starting the app

- after everything is setup and installed. you should be able to run

```bash
  # default entry file name is "main.py"
  $ flask --app `main_app_name.py` run
```

- ### bonus for using files

  - If you name the entry file as `app.py` or `wsgi.py`, you can simply start the serve by running

  ```bash
    flask run
  ```

___
___

### Available Routes

- [Index Route](#index-route)

- [Get All User](#get-all-users)

- [Get One User](#get-one-user)

- [Get All User](#get-all-users)

- [Create User](#create-user)

- ### Index Route

  ```bash
    @Get("/")

    -  # response : status - 200
      "Hello world"
  ```

- ### Get all users

  ```bash
    @Get("/users")

    -  # response : status - 200
      "getting all user"
  ```

- ### Get One user

  ```bash
    @Get("/users/<user_name>")

    -  # response : status - 200
      "Hello {user_name}"
  ```

- ### Create user

  ```bash
    @Post("/users/")

    -  # response : status - 200
      "creating user: method: {request_method}, name: json.name"
  ```
