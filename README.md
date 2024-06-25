## About
This project is useful for any restaurant that wishes to have website, I built a website that has a core operation of taking orders from customers and displays it to restaurant's admin and some other uses as well.
This project is built using HTML, CSS, JavaScript, django, and SQLite.

## Distinctiveness
This project is not similar to anything we have already created. It's not a social media app nor an e-commerce. It's not similar to other years projects either.
It's a unique project that serves a specific purpose, which is to help restaurants manage their orders.
In other projects all the users are have same set of functions but in this project admin will have some additional set of functions like adding a new item into the Restaurant's menu.


## Complexity
In terms of complexity, I used Django with more than one model (explained below) and several javascript files to the frontend.
I also used SQLite database to store the data. The project has several views, templates, and URLs.
I have used different API's so that the website runs fast.
I have used only a single javascript file instead of using different JS files for every HTML file

### Files and directories
- `restaurant` is the main project directory.
    - `static/restaurant` - contains all the static files
        - `index.js` - contains all the functions that are required by website, some important functions are
            - `allorder()` - this function fetches data using an asynchronous API call and displays all orders that are made, this functions is only for admin login.
            - `allitems()` - this function fetches data using an asynchronous API call and displays all items using another function `displayItem()` - this function is used in multiple pages within the websit.
            - `recommendation()` - this is a bit similar to `allitems()` but it only displays items that a used ordered previously
            - `displayItem()` - this function fetches data using an asynchronous API call and displays items and it creates a form for each item which on submitted, a order will be placed 
            - `menu()` - used to display items based on their category.

        - This folder also contains some images, I have used `img5.webp` , that can be used as background website

    - `templates/restaurant` contains all the html file
        - `login.html` - contains a login form for users to login
        - `register.html` - contains a register form for users to register
        - `index.html` once if the user is authenticated they are directed to this page, here all the items that are ordered previously are displayed at top using `recommendation()` method in JS and then all items of the restaurant sre displayed using `allitems()` function.
        - `layout.html` - contains the basic layout of every html page
        - `menu.html` - here items are displayed based on their category
        - `myorder.html` - displays the users order
        - `allorders.html` - displays allorders made through our website and view the detais of each order and close the order after delivery, this page can viewed only if you are a superuser
        - `add.html` - this page is used by admin to add new item into the menu

    - `admin.py` - here I added some admin classes and re-registered User model.
    - `models.py` - here I have defined 5 models. `User` contains user details, `Category` contains what type of food is served, `Item` contains details of diferent items, `Sale` contains details of how many and what all itmes are ordered by a user, `Order` contains details of a order by a user
    - `urls.py` - here I defined what are the valid urls that can be accessed within our website
    - `views.py` - here I have defined functions that are used by urls to fetch data and do some tasks some important functions are
        - `login_view()` - for user to login
        - `logout_view()` and `logout()` - for user to logout
        - `register()` - for user to register
        - `add()` - used by admin to add a new item to database
        - `allorders()` - used by admin to view all orders
        - `cancleorder()` - used by admin to close an order after delivery
        - `myorder()` - used by user to view their orders
        - `menu()` - used to display items based on their category
        - `index()` - used to display all items and recommendation
- `db.sqlite3` - it is the databse file
- `manage.py` - it is used to run the server
- `project5` - project directory.

## Installation
- Install project dependencies by running `pip install -r requirements.txt`. Dependencies include Django if you already installed it you can skip this step.
- Make and apply migrations by running `python manage.py makemigrations` and then `python manage.py migrate`.
- Create superuser with `python manage.py createsuperuser` to access the contents that a admin have.
- Run server by running `python manage.py runserver`.