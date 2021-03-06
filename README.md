# Authentication System

Django application to manage authentication of users.

## Details: 

It supports registration and login of users.

It has been implemented using Django web framework. 

## Setup

Install:

Step 1: **git clone https://github.com/akash-tomar/leapmind.git**

Step 2: **cd leapmind**

Step 3: Fire up your **virtual environment**

step 4: Run the shell script with **sh start.sh**

Finally, go to your local browser and point to **localhost:8000** or **127.0.0.1:8000**


## Documentation:

### Register [/auth/signup/]

#### Registration 

This is the endpoint for the registration on the system.

- First Name
- Last Name
- Email address
- Username
- Password
- Confirm Password


### Login [/auth/login/]

#### Login to the system

You may login to the system using this action.

- Username
- Password

### Forgot Password [/auth/email/]

#### Send email link for resetting the password.

This endpoint will send a recovery email for the password to be reset.

- Email address


### Logout [/auth/logout/]

#### Logout from the current session.

You may logout the bank portal using this action. 


### Home [/]

#### Home of the system

This is the home page of the system.




### Future Tasks

- Add feature where user can get a one time password on their Email address for logging into the system.

- Send a text to the user on their mobile phone, whenever their is an unusual login to their account.

- Feature of alternate Email address for password recovery.

- Block the account temporarily on five failed attempts to login and notify the user via email.