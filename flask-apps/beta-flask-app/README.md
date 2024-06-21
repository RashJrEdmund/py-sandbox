## Setup For beta-flask-app

_This is built on and from the [basic-flask-app](../basic-flask-app/README.md)_

- Make sure to Create a virtual environment (v-e), and install required modules as per my main [documentation](../../README.md#configuring-a-virtual-environment-v-e)

### Starting the app

- after everything is setup and installed. you should be able to run

```bash
  # default entry folder name is "main/"
  $ flask --app `entry_folder_name` run
  # `entry_folder` is mostly the one with the __init__.py file
```

- ### bonus for using folders

  - Just as [starting the app and the bonus section](../basic-flask-app/README.md#starting-the-app) in the basic-flask-app documentation, there's a similar pattern when using folders.

  - If you name the entry folder name is `app` (as in this case) or `wsgi`, you can simply start the serve by running

  ```bash
    flask run
  ```

  - provided it has an `__init__.py` file

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
