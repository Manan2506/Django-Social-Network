# Social Network API

This is a RESTful API for a social network application built with Django and Django REST framework. It allows users to sign up, log in, send and manage friend requests, and search for users.

## Features

- User registration and authentication
- Sending, accepting, and rejecting friend requests
- Listing friends and pending friend requests
- Searching for users

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST framework
- PostgreSQL (or any other preferred database)

### Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/social-network-api.git
   cd social-network-api

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt

4. **Configure settings**

   Open 'settings.py' and add your configurations directly:

   ```sh
    # settings.py

    SECRET_KEY = 'your_secret_key'
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'yourdatabase',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

5. **Apply migrations**

   ```sh
   python manage.py migrate

6. **Create a superuser**

   ```sh
   python manage.py createsuperuser

7. **Generate Dummy users(Optional)**

   ```sh
   python manage.py generate_dummy_users <number_of_users>

8. **Run the development server**

   ```sh
   python manage.py runserver

## API Documentation

To simplify testing the API, you can use the Postman collection provided. Follow these steps:

### Postman Collection

1. **Download the Postman collection JSON file**. Link - [social-network.postman_collection.json](https://drive.google.com/file/d/13zE_6a3wfsHRJZ7o7zvzrECR89fDmz_q/view?usp=sharing)
2. **Open Postman**.
3. **Click on Import** in the top left corner.
4. **Select the Collection tab**.
5. **Click on Upload Files** and select the downloaded JSON file.
6. Once imported, you will see the collection listed in your Postman under the Collections tab.

### Available API Endpoints

The Postman collection includes endpoints for:

#### Authentication

- **Signup**
- **Login**
- **Refresh Token**

#### Friend Requests

- **Send Friend Request**
- **Accept Friend Request**
- **Reject Friend Request**
- **List Friends**
- **List Pending Friend Requests**

#### User Search

- **Search Users**

### Example Request

Here’s an example of how to use the Postman collection to send a friend request:

1. Open Postman and select the **Send Friend Request** request from the imported collection.
2. Ensure you have obtained an access token by logging in with the **Login** request and copying the access token from the response.
3. In the **Send Friend Request** request, go to the **Headers** tab, select **Bearer Token**, and paste the copied access token.
4. Update the request body with the `receiver_id` of the user you want to send a friend request to.
5. Click **Send** to make the request.

### Pagination

The "Search Users" API uses pagination for listing users. You can specify the page_size parameter in `CustomPagination` class to customize the number of results per page.


### Throttling

The "Send Friend Request" API uses throttling to limit the number of requests a user can make. The default rate limit for sending friend requests is 3/minute.