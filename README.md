# nanodegree-blog
Multi user blog, created as part of my Full Stack Nanodegree Program.
This blog has many features as user registration, email confirmation,
user can makes CRUD of post and comments also, and can give likes to
a post.

## Table of content

- [Requirements](#requirements)
- [Quick Started](#quick-started)
- [Deployment](#deployment)


## Requirements
- [Python 3](https://www.python.org/downloads/release/python-353/)
- [Virtualenv `optional`](https://virtualenv.pypa.io/en/stable/)
- [A Google Cloud Account](console.developers.google.com)
- A SendGrid Account or any other Email Service


## Quick Started
Once you have all the requirements setup:

**Note:** Before seting up the environment, create a new project
in the google console.

1. Clone this repository.
  * Run `git clone https://github.com/oldani/nanodegree-blog.git`
in the console
2. If using `virtualenv`
  * Create an env by running `virtualenv -p python3 env`
3. In the project repository
  * Run `pip install requirements.txt`
  * Edit the `env.example` file, replacing all the env vars
example values with real ones. Once done rename the file to
`.env`.
4. Once everything setup run `python manage.py runserver`
5. Go to `http://localhost:5000/`.


## Deployment
This project have been develop using the Google App Engine
Flexible Environment, so for running this in production you
will need a account with billing activated, due to these
environments does not have free tier.

For deploying this you will need the [Cloud SDK](https://cloud.google.com/sdk/)

**Note:** Before running this command, make sure
you set all the `env vars` values you want in PROD
in the `.env` file, due to gcloud will push it.

Once install just run `gclound app deploy`.
