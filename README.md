
# Distinctiveness
This project is uniquely designed to address the specific needs of restaurants looking to establish an online presence and streamline their order management process. Unlike social media applications, e-commerce platforms, or other generic web applications, this project focuses on a niche functionality: enabling restaurants to efficiently manage customer orders through a web interface.

One of the key aspects that sets this project apart is its dual-user functionality. Unlike typical web applications where all users have the same set of capabilities, this project distinguishes between two types of users: customers and restaurant admins. While customers can browse the menu, place orders, and check the status of their orders, the admin has additional functionalities. The admin interface is equipped with the capability to add new items to the menu, update or remove existing items, and view all incoming orders in real-time. This bifurcation creates a unique user experience tailored specifically to the needs of restaurants, focusing on both customer engagement and operational efficiency.

Moreover, this project differs significantly from traditional e-commerce sites. While an e-commerce website typically involves a shopping cart, checkout process, and perhaps some product management, this project emphasizes real-time interaction between the customer and the restaurant. It does not involve a generic catalog of products for broad consumer purchase but rather a dynamic, editable menu that reflects the unique offerings of a specific restaurant. The focus is not on payment gateways or shipping logistics, but on simplifying and optimizing the order-taking process, ensuring that orders are efficiently communicated to the restaurant staff, and that customers receive timely updates


# Complexity
The complexity of this project lies in both its backend architecture and frontend interactivity, leveraging a combination of Django, JavaScript, and SQLite to provide a robust and efficient solution.
- ## Backend Complexity
    From a backend perspective, the project utilizes Django, a powerful Python web framework known for its scalability and versatility. The use of Django is not limited to basic CRUD operations; rather, it involves multiple models that reflect the different components of a restaurant’s ordering system. For example:
    - ### Menu Model:
        This model stores the details of each menu item, such as the item name, description, price, and availability status. The menu is dynamic, allowing the admin to update it in real-time, which adds a layer of complexity to both the database management and the user interface.
    - ### Order Model:
        This model is designed to handle incoming orders. It tracks the customer details, the items ordered, quantities, order status (pending, in preparation, completed, etc.), and timestamps. Managing the state of each order requires careful coordination between the backend and the frontend, ensuring that updates are reflected accurately and promptly.
    - ### User Model:
        This includes the differentiation between customers and admins. The authentication and authorization process ensures that only admins can access certain parts of the application, such as the menu management interface. This involves the creation of custom permissions and user roles, adding another layer of complexity.

    Additionally, this project integrates various APIs to enhance the user experience and improve performance. For example, APIs may be used to fetch real-time data for items or to enable seamless communication with external services like delivery platforms. The integration of these APIs requires handling asynchronous operations, error management, and ensuring compatibility across different systems.

- ## Forntend Complexity
    On the frontend, this project utilizes a single JavaScript file to handle dynamic interactions across various pages, rather than segmenting scripts by page. This approach necessitates more sophisticated JavaScript code to manage multiple functions, handle DOM manipulation, and ensure smooth user interactions. Some of the functionalities managed by this JavaScript include:
    - ### Real time order updates:
        JavaScript is used to periodically fetch updates from the server, allowing the customer and admin to see order status changes in real-time without needing to refresh the page.
    - ### Dynamic menu Updates:
        The menu interface allows for dynamic updates by the admin. JavaScript handles the addition, removal, and modification of menu items on the fly, ensuring that changes are immediately visible to both the customer and the admin.
    - ### Interactive User Interface Elements:
        JavaScript manages the interactivity of various UI components, such as modals, dropdowns, and buttons. This enhances the user experience by making the website more responsive and interactive.

- ## Database Management
    The project uses SQLite as its database management system, which is well-suited for web applications due to its simplicity and effectiveness in handling moderate amounts of data. However, using SQLite in a web application involves optimizing database queries to ensure fast performance and responsiveness, especially when dealing with concurrent users. This requires efficient indexing, caching strategies, and careful management of database connections.

- This project also involves setting up several views, templates, and URLs to create a seamless and intuitive user experience. Each view is tailored to a specific function, such as displaying the menu, managing orders, or handling user authentication. The use of Django templates allows for dynamic content rendering, which is crucial for maintaining a consistent and engaging user interface.

# Files and directories
- ## `restaurant` is the main project directory.
    - ### `static/restaurant` - contains all the static files
        - `index.js` - contains all the functions that are required by website, some important functions are
            - `allorder()` - this function fetches data using an asynchronous API call and displays all orders that are made, this functions is only for admin login.
            - `allitems()` - this function fetches data using an asynchronous API call and displays all items using another function `displayItem()` - this function is used in multiple pages within the websit.
            - `recommendation()` - this is a bit similar to `allitems()` but it only displays items that a used ordered previously
            - `displayItem()` - this function fetches data using an asynchronous API call and displays items and it creates a form for each item which on submitted, a order will be placed 
            - `menu()` - used to display items based on their category.

        - This folder also contains some images, I have used `img5.webp` , that can be used as background website

    - ### `templates/restaurant` contains all the html file
        - `login.html` - contains a login form for users to login
        - `register.html` - contains a register form for users to register
        - `index.html` once if the user is authenticated they are directed to this page, here all the items that are ordered previously are displayed at top using `recommendation()` method in JS and then all items of the restaurant sre displayed using `allitems()` function.
        - `layout.html` - contains the basic layout of every html page
        - `menu.html` - here items are displayed based on their category
        - `myorder.html` - displays the users order
        - `allorders.html` - displays allorders made through our website and view the detais of each order and close the order after delivery, this page can viewed only if you are a superuser
        - `add.html` - this page is used by admin to add new item into the menu

    - ### `admin.py` 
        - here I added some admin classes and re-registered User model.
    - ### `models.py` 
        - here I have defined 5 models. `User` contains user details, `Category` contains what type of food is served, `Item` contains details of diferent items, `Sale` contains details of how many and what all itmes are ordered by a user, `Order` contains details of a order by a user
    - ### `urls.py` 
        - here I defined what are the valid urls that can be accessed within our website
    - ### `views.py` 
        - here I have defined functions that are used by urls to fetch data and do some tasks some important functions are
        - `login_view()` - for user to login
        - `logout_view()` and `logout()` - for user to logout
        - `register()` - for user to register
        - `add()` - used by admin to add a new item to database
        - `allorders()` - used by admin to view all orders
        - `cancleorder()` - used by admin to close an order after delivery
        - `myorder()` - used by user to view their orders
        - `menu()` - used to display items based on their category
        - `index()` - used to display all items and recommendation
- ## `db.sqlite3` - it is the databse file
- ## `manage.py` - it is used to run the server
- ## `project5` - project directory.

# Installation
- Install project dependencies by running `pip install -r requirements.txt`.
- Make and apply migrations by running `python manage.py makemigrations` and then `python manage.py migrate`.
- Create superuser with `python manage.py createsuperuser` to access the contents that a admin have.
- Run server by running `python manage.py runserver`.

# Working Of Website
- ## Login 
    - ### User login
        - Create an account by clicking `Register` on top right of screen, Fill the form and click `Register` button
        - Then login using your credentials
        - You can login using `jayanth` as username and `j123` as password.
    - ### Admin login
        - Admin means superuser, run `python manage.py createsuperuser` in terminal to create superuser.
        - Admin can login using `kp` as username and `kp123` as password, which are created by me. Follow this step if you are facing trouble in creating superuser.
        
- ## View items of Restaurant
    - ### View all items
        - After login you will be able to see all the items that the restaurant is offering.
    - ### View items based on category
        - Click on `Menu` on top of the screen, you will be directed to menu page.
        - Here you can view items based on their category.
        - Click on the drop down and select a category, items listed in that category will be displayed.
    - For each item it shows name, price of each plate and shows if its veg or non-veg.
    - This feature is avaliable to both user and admin.
    

- ## Place an order
    - View the item you want to order, follow the steps from `View items of Restaurant`.
    - Click on `+` to add number of plates you want to order, you can order at most 10 plates, as you click on `+` the amount of that item will be displayed.
    - Click on `Add to cart` to add the item to cart.
    - This feature is avaliable to both user and admin.

- ## View and Cancle your order
    - ### View your order
        - Click on `My Orders` on the navbar, you will be directed to your My Orders page.
        - Here you can view all the orders you have placed.
    - ### Cancle your order
        - Click on `Cancle Order` to cancle your order.
    - This feature is avaliable to both user and admin.

- ## Add a new item to menu
    - Click on `Add Item` on nav-bar.
    - Fill the form and click `Add Item` button.
    - Now you can view this item, follow the steps mentioned in Working/View Items of Restaurant.
    - This feature is avaliable to admin only.

- ## All Orders
    - Click on `All Orders` on nav-bar.
    - Here you can view all the orders that have been placed.
    - ### View Order
        - Click on `View Order` to view the details of order.
    - ### Cancle Order
        - Click on `Clear` to clear the order.
        - Ideally admin does this after order is delivered.
    - This feature is avaliable to admin only.