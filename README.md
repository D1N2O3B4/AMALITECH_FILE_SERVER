# LIZZY'S FILE SERVER

    This project is a file server application built with Django. It allows users to upload, download, and email files of various formats. The application also includes custom user authentication via email and a custom login view.

## Logging
    Added logging functionality to the implementation of register, forgot password
    and share file endpoints, to perform some logging into a file if a
    request is to fail during it's execution.

# Deployed link and admin credentials
* email: admin@admin.com
* password: password
* [Deployed link](http://d1n2o3b4.pythonanywhere.com/)

# ER diagram of database design
![ER diagram of database](https://github.com/GideonAg/File-Server-Backend/assets/99260218/0faa88f4-06ed-4b78-b7c5-dcc2a1ca4fcb)

<!-- TOC -->
  * [Email Authentication](#login)
    * [Backend(backends.py)](#Backend)
    * [JSON Body](#json-body)
    * [Error Responses](#error-responses)
    * [Successful Response Example](#successful-response-example)

<!-- TOC -->


## EMAIL AUTHENTICATION

### Request Information


