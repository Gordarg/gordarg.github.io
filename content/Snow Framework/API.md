Notes:
===

## Path to controller: {ROOT}/controllers/{CONTROLLER}Controller.php
## GET: Send parameters as URI QueryString
## POST: Send parameters as form-data

<hr/>

Functions:
===

# Login
## CONTROLLER: auth | METHOD: POST
## PARAMS:
- Username
- Password
## RESPONSE:
- if login failed: false
- if login success:
    1. Username: Users username
    2. Token: Login token used in other api parts

<hr/>

# Validate Token

## CONTROLLER: auth | METHOD: POST
## PARAMS:
- Username
- Token
## RESPONSE:
- if was valid: true
- if was invalid: false