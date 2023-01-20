# Python OpenAI Quickstart Project

## A - Acessing OpenAI

To execute this project scripts on ChatGPT an authentication
to the OpenAI API is required. 

For this purpose sign up for an openai account:

[https://beta.openai.com/signup]

After creating your account and confirming your email
you will be redirected to the main screen
[https://beta.openai.com/overview]

On the top right corner click on your account and select 
'View API keys'

In the 'API keys' page click on "+ Create new secret key"

A new API key will be generated.

**Copy and store safely this key.**

The API key will be used later, before running the python scripts,
as an environment variable.
 

## B - Managing dependencies

To manage dependencies such as the `openai` library 
in this project we will be using `poetry`

### Poetry dependency management

**1. Install Poetry**

[https://python-poetry.org/docs]

Linux, macOS, Windows (WSL): 

```curl -sSL https://install.python-poetry.org | python3 -```


**2. Add to path**

On Mac (unix): 

```export PATH="$HOME/.local/bin:$PATH"```

On Windows:

```export PATH="%APPDATA%\Python\Scripts:$PATH"```

**3. Set virtual enviroments to project directory**

```poetry config virtualenvs.in-project true```

If you are cloning the project jump to step 5 once you
already have the project created and its properties defined on 
the `pyproject.toml` file.

**4. Create new project**

```poetry new python_poetry_project```

```cd python_poetry_project```


Instead of modifying the `pyproject.toml` file by hand, you can use the add command

```poetry add openai```

```poetry add pytest```

**5. Install dependencies**

Inside your project directory run the following:

```poetry install```

Poetry will create a virtualenv locally inside your project folder `./venv`

## C - Executing python scripts

Once poetry has created your virtual environment inside your
project directory you have to activate it.

To activate the virtualenv use:

```source ./venv/bin/activate```

To run our scripts on OpenAI we export the generated API key
as an environment variable:

```export 'OPENAI_API_KEY'='yourAPIkey'```


To run a file with poetry in your virtualenv run:
 
```poetry run python path/file.py```

**openai_wrapper.py**

```poetry run python python_openai_quickstart/openai_wrapper.py```


**main.py**

```poetry run python python_openai_quickstart/main.py```