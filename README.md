## Welcome To My Py Sandbox

- Checkout the actual sandbox docs, where I study and also build the game "Attack On Monsters" [here](./sand-box/README.md)
  - Note I build it using the NeoVim editor

- Or checkout my flask apps docs [here](./flask-apps/README.md)

## Configuring a virtual environment (v-e)

__Note__: _you are gonna have to create a v-e in both the sand-box and flask-app(s) folders(though I haven't installed any modules in the sand-box app)_

- for this i'm using the `virtualenv` command
- __STEPS TO CREATE VIRTUAL ENVIRONMENT__
  
  - in the projects directory, at top level, run

    ```bash
      # if using the virtualenv package
      $ virtualenv venv

      # if using the default venv from python
      # on linux
      $ python3 -m venv venv
    ```

  - This should create a `venv` folder (which is the virtual environment)

  - Next, you have to __activate__ the virtual environment. To do so, execute

    ```bash
      # for linux
      $ source venv/bin/activate
    ```

    - Deactivate it by simply executing the `deactivate` on your terminal

  - you should see you file path look similar to this

    ```bash
      (venv) username@computer:~/full/path/py-sandbox/which-ever-path-you-on/$
    ```

  - You should be able to safely install packages with `pip`

- Now, to install the packages in requirements.txt file of that folder, execute

  ```bash
    $ pip install -r requirements.txt
    # the -r means it should read from the requirements.txt file
  ```

- ### ADDING YOUR OWN PACKAGES

  - After every package installation, I advice you update the requirements.txt file with

    ```bash
      $ pip freeze > requirements.txt
      # it's like package.json in JavaScript, but for python
    ```

  - you should even combine the installation command with the freeze command like so to execute all at once

    ```bash
      pip install `module_name` && pip freeze > requirements.txt
    ```

  - use `pip list --local` to see all locally installed modules in your virtual env

### Cool new commands

- `>>`
  - to use with command like `echo` or `pip freeze` to add content to the end of a file

- ##### Example

  - `echo "some text content" >> test_file.txt` to add the text "some text content" to the test_file.txt. this file will be created if not exit
  
- `>`
  - Same as the `>>` pattern above but will completely replace the content of the file

---
---
---

### Cool command combo

- `find . -type d -name "__pycache__" -exec rm -rf {} +`
  - to find and delete all "__pycache__" folders in the current working directory

- #### Explanation

  - `find .` : Start searching from the current directory (.)
  - `-type d` : Look for directories (d)
  - `-name "__pycache__"` : Match directories named "__pycache__"
  - `-exec rm -rf {} +` : For each found directory, execute the rm -rf command on it ({} is replaced by the found directory paths)
