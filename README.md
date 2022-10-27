# Flask-Login, Cookies, and Sessions

## Learning Goals

- Create an application that requires users to authenticate with Flask-Login.
- Retrieve data from cookies to allow users to access data from previous
  sessions.

***

## Key Vocab

- **Identity and Access Management (IAM)**: a subfield of software engineering that
  focuses on users, their attributes, their login information, and the resources
  that they are allowed to access.
- **Authentication**: proving one's identity to an application in order to
  access protected information; logging in.
- **Authorization**: allowing or disallowing access to resources based on a
  user's attributes.
- **Session**: the time between a user logging in and logging out of a web
  application.
- **Cookie**: data from a web application that is stored by the browser. The
  application can retrieve this data during subsequent sessions.

***

## Introduction

**Authentication** is the process of using pieces of a user's digital identity
to allow or disallow access to a web application. This is typically accomplished
with a username and password, though some institutions choose to use biometric
data like fingerprints or multi-factor authentication (usually through use of a
phone in addition to a username and password).

> **Note: Authentication only determines whether or not a user can access an
> application as a whole. Authorization is the process of determining which
> resources they can access within the application- we'll learn more about that
> later.**

Flask provides us with a simple bare-bones library called **Flask-Login** to
handle authentication. In this introduction to authentication, we will be
looking at a grocery list API and adding Flask-Login to tailor the experience
to individual users.

Before we get started, run the following commands to configure your application
and populate your database:

```console
$ pipenv install
$ pipenv shell
$ cd app
$ flask db upgrade
$ python seed.py
```

***

## Resources

- [Introduction to Identity and Access Management (IAM) - auth0](https://auth0.com/docs/get-started/identity-fundamentals/identity-and-access-management)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
