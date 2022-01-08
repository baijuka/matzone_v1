<h1 align="center">Matzone Online Shop</h1>

![Matzone](./static/wireframe/sitepicture.png)

# [Matzone](https://ms4-matzone-v1.herokuapp.com/)

## <a name="contents"></a>Contents
1. [Summary](#summary)
1. [UX](#ux)
    1. [Strategy](#strategy)
    1. [Scope](#scope)
    1. [Structure](#structure)
    1. [Skeleton](#skeleton)
    1. [Surface](#surface)
1. [Features](#features)
    1. [Existing Features](#existing-features)
    1. [Features left to implement](#left-to)
1. [Known Bugs](#bugs)
1. [Technologies used](#tech)
1. [Testing](#testing)
1. [Deployment](#deployment)
    1. [Github Pages](#github)
    1. [heroku](#heroku)
1. [Credits](#credits)
    1. [Content](#content)
    1. [Acknowledgements](#acks)

# <a name="summary"></a> Summary
A clean environment is essential for healthy living. Every home, office or place of work ensure that their floors are clean and dust/dirt free.  Matzone comes 
to help those who want to protect their floor dust/dirt free by providing high quality durable rubber mats with various choices and purposes. They supply mats for
offices, homes, garages, workshops, shops and many other institutions. Mats provided by Matzone are made from natural latex and coconut fibre from Kerala, India. 
The ultimate objective of this website is to help its customers(users) to choose and order mats of their choice as easily as possible.  Moreover, Matzone is an 
imaginary online shop deveoped as part of an educational project.

# <a name="ux"></a> UX
The primary objective of Matzone is to provide its users a user-friendly, intuitive website capable of providing all required information about how to use the 
website within a user-friendly platform.

## <a name="Strategy"></a> Strategy
### **Viewing and Navigation**
As a |I want to be able to.. |So that I can…                                                                    
---|--------|-----------------------------------------
Shopper |View a list of products                  |Select some to purchase                                                           
Shopper |View individual product details          |Identify the price, description, product rating, product image and available sizes
Shopper |Easily view the items in shopping bag and total of my purchases at any time |Avoid spending too much

### **Registration and User Accounts**
As a |I want to be able to.. |So that I can…                                                                    
---|--------|-----------------------------------------
Site User|Easily register for an account |Have a personal account and to be able to view my profile
Site User|Easily login and logout  |Access my personal account information
Site User|Receive an email confirmation after registering |Verify that my account registration was successful
Site User|Have a personalised user profile |View my personal order history, order confirmation and save my payment information

### **Sorting and Searching**
As a |I want to be able to.. |So that I can…                                                                    
---|--------|-----------------------------------------
Shopper |Sort the list of available products |Easily identify the best rated, best priced and categorically sorted products
Shopper |Sort a specific category of product |Find the best priced or best rated product in a specific category or sort the products in that category by name
Shopper |Sort multiple categories of products simultaneously |Find the best priced or best rated products across broad categories such as ‘Rubber mats’ or ‘Coir mats’ etc.
Shopper |Search for a product by name or description |Find a specific product I would like to purchase
Shopper |Easily see what I’ve searched for and the number of results |Quickly decide whether the product I want is available

### **Purchasing and Checkout**
As a |I want to be able to.. |So that I can…                                                                    
---|--------|-----------------------------------------
Shopper |Easily select the size and quantity of a product when purchasing it |Ensure I don’t accidently select the wrong product, size or quantity 
Shopper |View items in my bag to be purchased |Identify the total cost of my purchase and all items I will receive
Shopper |Adjust the quantity of individual items in my shopping bag |Easily make changes to my purchase before checkout
Shopper |Easily enter my payment information |Checkout quickly and without any hassles
Shopper |Feel my personal and payment information is safe and secure |Confidently provide the information needed to make a purchase
Shopper |View an order confirmation after checkout |Verify that I haven’t made ay mistake
Shopper |Receive an email confirmation after checkout |Keep the confirmation of what I have purchased for my records

### **Review/Rate Products and Contact Store Owner**
As a |I want to be able to.. |So that I can…                                                                    
---|--------|-----------------------------------------
Shopper |Review and rate the products I purchased |I can provide my views and experience about the product which will help other shoppers make decision before buying a specific product
Shopper |Contact the Store Owner for details about a product or service |I can clear my doubts about a particular product or service

### **Admin and Store Management**
As a |I want to be able to.. |So that I can…                                                                    
---|--------|-----------------------------------------
Store Owner |Add a product |Add new items to my store
Store Owner |Edit/Update a product |Change product prices, descriptions, images and other product criteria
Store Owner |Delete a product |Remove items that are no longer for sale

## <a name="scope"></a> Scope
#### **Requirements**
1. A home page with navbar and footer.
2. A responsive design.
3. A page where all products are displayed.
4. An option to register and login/logout.
5. Defensive programming, e.g. confirmation on buying, deleting, logging out, etc.
6. A profile page where registered users can add and edit personal information, see their orders and reviews.
7. A shop page.
8. An about page where users can get more information about the company and/or available products.
9. A contact page with contact form where users can contact the site’s owner.
10. Individual pages for products to display its details.
11. Indication/banner for offers or deals.
12. A shopping cart icon with relevant info that is displayed at all times.
13. An admin page with options to Create, Read, Edit and Delete (CRUD) products.
14. An option to search the site.
15. An option to filter and sort.
16. An indication of search term and numbers of results.
17. A checkout page with details on the shopping items.
18. An option to adjust items in the shopping bag.
19. Secure checkout via Stripe payment.
20. Email confirmation on purchase.

#### **Extra requirements**
1. An option to delete a profile.
2. An option to recover the password.
3. The option to see reviews on products.
4. The option to Create, Read, Edit and Delete (CRUD) own reviews.

## <a name="structure"></a> Structure
## **Structure Level**
### **Interaction Design and Information Design**
The overall look is kept the same on each page as much as possible, to enhance single-use-learning:
- The header and footer are kept mostly the same on each page.
- Buttons are styled in the same way.
- The layout is consistent inside each page.
- The use of colours are kept the same on each page.

The navigation is kept simple and consistent:
- responsive navigation bar at the top of the page.
- A landing page with clearly indicating the options and information for first time users.
- The logo at the top of the page is also the link to the home page.
- Buttons can be used to navigate.

The information provided should be easily visible:
- Visual aids are used, like icons and complementary colours.
- The amount of information is kept to a minimum.
- The user gets an indication on which page they are, e.g. by using headers.

The user is given feedback, in order to enhance a pleasant user experience:
- The user gets a visual feedback during certain actions (e.g. focussing on, clicking on, hovering over buttons and links).
- Messages(toasts) are used to confirm or inform about current actions.
- The user get's a feedback when an error has occurred (via warning text or error handlers). In case of error handlers there is a button that 
leads back to the home page.

### **The pages**
        FRONTEND  
The website has 19 pages, plus 3 error handler pages. Each page will have a navbar and a footer.
The links in the navigation bar are shown depending on whether a user is logged in or not and if the user is the admin or not.
The main navigation bar has links to home, products, shop, about, contact, account, shopping basket and search.
When a user is logged in, the register and login links are hidden and a profile link and logout link are shown.
When the user is admin, an extra link for site managing is shown.  

The footer has a section with contact details, an overview of some important links and links to socials.

#### Description of the pages

- **The landing page/home page:**  
This is the first page a user sees when they come to the site. There is a hero image and a CTA-text and button for the products.
Below that there is a section for the shop where the user can see the latest products and a link to the shop page.

- **The products page:**  
On this pages all the products are displayed.  All the products are displayed with a corresponding image, 
the name of the product and a link to the individual product.

- **The product details page:**  
This is where the individual product is displayed. The user can get more information about the  product, 
like description and price. There is an option to choose the amount and the departure date.

- **The about page:**  
This page has a short description about the website and the background of the  products.

- **The contact page:**  
This page has a contact form, where the user can ask questions or give remarks. 
A confirmation email is sent to the user’s email address after submitting.

- **The sign up page:**  
This page has a signup form where the user can register and create an account. After registration 
the user is asked to confirm their email address. After confirmation the user is redirected to the
home page. There is a button to go to the login page, if a user already has an account.

- **The sign in page:**  
This page has a login form where users that have an account can login. After login the user will be 
redirected to the home page. There is a button to the register page, in case the user has no account.

- **The profile page:**  
This is the personal page of the user. Here the user can see and edit their shipping information, 
see an overview of their orders (with a link to that order) and any reviews they have written 
(with a link to that product).

- **The product management page:**  
On this page, the admin can add a new product or  product by filling in the form. After submitting the admin 
is redirected to the individual page of the added product.

- **The edit product page:**  
On this page, the admin can edit an existing product by editing the pre filled form. After submitting the admin is redirected to the individual
page of the added product.

- **The delete product confirmation page:**  
On this page, the admin can confirm the delete action.  Pressing 'Yes' will lead to permanent deletion of the product and 'Cancel' will abandon 
cancellation and redirects to products listing page.

- **The shopping bag page:**  
This page contains all the items the user has put in their shopping bag. It has an overview of the product, the amount, the price, 
the subtotal and the grand total. There is a button to go back to the shop page and a button to go to the checkout page.

- **The checkout page:**  
This page has an form the user has to fill out iot complete their order. The user has to provide delivery information and credit card details. 
After submitting the form, the user gets a confirmation email. There is also an order summary.

- **The checkout success page:**  
This page is shown when the payment was successfull. It has an overview of the order, delivery details and payment details. 

- **The order history page:**  
This page is used to display the history orders made by each individual user. Users should be logged in to view this page.

- **The review page:**  
This page is intented for logged in users to add product rating and reviews. 

- **The 403 error handler page:**   
This page is shown in case of forbidden access.

- **The 404 error handler page:**  
This page is shown in case no page is found.

- **The 500 error handler page:**  
This page is shown in case of an internal service error.


        BACKEND 
During development the Sqlite3 database is used. This is the default database used by Django.
During production PostgreSQL is used in conjunction with deployment on Heroku.

### **Database Model**

Relational databases are widely used to store complex data.  It's primary key, foreign key ralationships makes data retrieval easy for the developers. It's speed, acccuracy, simplicity, security, accessibility and multi user functionality are the major factors make it popular. This project uses various models that need to establish relationships between and in such case the developer decided to use relational database for backend storage. SQLite was used during development and Heroku Postgres in production. The database schema diagram explains the relationship between models.

![Database](./static/wireframe/schemadiagram.png)

## **Skeleton Level**
### Wireframes
- [Home Page](https://github.com/baijuka/matzone_v1/blob/main/static/wireframe/index.pdf)  
- [Products Page](https://github.com/baijuka/matzone_v1/blob/main/static/wireframe/product-list.pdf)  
- [Product Details Page](https://github.com/baijuka/matzone_v1/blob/main/static/wireframe/product-details.pdf)  
- [About Page](https://github.com/baijuka/matzone_v1/blob/main/static/wireframe/about.pdf)  
- [Product Management Page](https://github.com/baijuka/matzone_v1/blob/main/static/wireframe/product-management.pdf)  
- [Contact Page](https://github.com/baijuka/matzone_v1/blob/main/static/wireframe/contact.pdf)  

--------------------
**Interaction design:**
* User friendly interface to ensure usability and to encourage the user to return
* Responsive and visible links which change on hover to provide user feedback as they navigate the site
* Ability to exit pop ups so a user is not forced to use the browser navigation tools

**Information Architecture:**
* Navigation bar at the top of the page
* Footer at the bottom of the page - sticky to the bottom so it is only visible when the bottom of the page is reached
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive images to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* All features appropriate size and responsive for mobile and desktop viewing
* All information is appropriate and relative to the subject and not misleading or hard to find

## <a name="skeleton"></a> Skeleton
**Wireframes** for desktop, tablet and mobile deiveces were created using Balsamiq Desktop App.  
-   Home Page Wireframe -<a href="./static/wireframe/index.pdf" target="_blank" >Home Page</a>
-   About Page - <a href="./static/wireframe/about.pdf" target="_blank" >About</a>
-   Product List Page - <a href="./static/wireframe/product-list.pdf" target="_blank" >All Products</a>
-   Product Detail Page - <a href="./static/wireframe/product-details.pdf" target="_blank" >Product Detail</a>
-   Contact Page - <a href="./static/wireframe/contact.pdf" target="_blank" >Contact</a>
-   Product Management Page - <a href="./static/wireframe/product-management.pdf" target="_blank" >Product Management</a>


## <a name="surface"></a> Surface
The intention of the website is to be clean, crisp and clear

* The font family chosen is 'Roboto' which is simple and allowing letters to be settled into their natural width.
* The colour scheme selected is shades of Materialze blue-grey and off-white with black font. Shades of blue, orange and red were used for buttons to match the context.
* Color scheme was chosen considering users from all aspects of life. Too bright and vibrant colors were avoided to accommodate users with different visual capacities.

### Mockups
* <a href="./static/mockup/mockup.pdf" target="_blank" >Mockups</a>



### **Key Models**

#### **User**

- This model is created by Django admin for user creation and management.

#### **UserProfile**

- Created on registration for each user, holds user information that can be used to speed up checkout process.

- Stores order history for previous orders to encourage repeat orders.

#### **Product**

- Holds the infomation about a product including name, description, basepprice, image and rating.

- The relationship to 'Category' is descriptive.

#### **ProductVariation**

- The product table does not keep the size.  Each product has may or may have various sizes and values. This model was created to keep size, value and corresponding stock. This table has a foreign key relationship with Product(parent).

#### **Category**

- This model divides the products into category according to their types.

- Considering the chances of blank spaces we also give it a friendly name.

#### **Order**

- Stores information about an order such as user, order number, delivery details and total cost.

#### **OrderLineItem**

- This model stores each product in each order by its name, size, quantity and a subtotal.

#### **Contact**

- This model sends the users' name, email and messages into admin.

#### **Review**

- This model keeps the customer reviews of various products.  This model has foreign key relationship with Product model.

[Back to contents](#contents)

## **Features**

### **Existing Features**

#### **Across the Site**

- **Navbar** - consistent on all pages and provides quick access to all areas of the site.

- **Search Bar** - allows the user to search a particular product with a key word.

- **Toasts** - Bootstrap toasts give interaction to users after each action carried out. Shows the shopping bag view for quick checkout option. Avoids confusion and gives user a better experience.

- **Responsive** - Bootstrap's grid system and various media queries had been used throughout the project to ensure responsiveness.

- **User Profile** - allow users to save their information for easy acess for next visit. Order history encourages repeat order.

- **Bag Item Counts** - the number of items in the shopping bag tells users how many items they have added to the bag.

- **Navbar Banner** - tells the user about free classes and free delivery offer.

- **Footer** - tells the user about the site purpose and developer info.

#### **Page Specific**

#### ***Home***

- Hero image slides gives potential customers a brief idea what the dojo providing.

- The quick links give the users quick access to specific areas of the site.

- The featured products section draws users attention that there is a shop in the site to encourage potential purchases.

#### ***Products***

- Product cards show the essential details of the product (name, rating, price and category)

- View Prouct details button tells the user there's more to explore.

- Bootstrap Breadcrumb indicates which page the user is on and how many products are avaliable on the page.

- The filtering bar allows the users to sort the products by specific query.

- Back to top button allows the users to go back to the top at any time.

#### ***Product Detail***

- In addtion to the information the products page gives to the user, the product detail page gives the user a brief description about the product.

- There are also more images displayed when applicable.

- The user then has an option of choosing a color or size for that specific product if it applies.

- Two buttons provided at the bottom to add to bag or keep shopping.

#### ***Bag***

- Allows line item quantities to be altered or removed from the bag and updates on each change.

- Shows bag total, delivery, and grand total of the order.

- Provides link to the specific product, allow easy alteration to sizes and colors etc.

- If bag total is less than free delivery threshold, amount required to receive free delivery is shown.

#### ***Checkout***

- Shows order summary and form to input delivery details.

- Payment handled by Stripe and reliability improved by use of webhooks.

    *Registered users*

- If delivery details previously saved, form will be pre-populated with them.

- Option to save delivery details for future purchases.

#### ***Checkout Success***

- Shows a summary of the order identifier, contact info and delivery information provided, as well as details of the order itself. On checkout the user is sent a confirmation email with details about their order.

- A quick link to go back to the shop.

#### ***My Profile***

#### *Registered User*

- Default contact and delivery info

- Ability to update to make future checkouts quicker

- View previous orders using same template as checkout success page

#### ***Add/Edit Product***

#### *Super users*

- Can add/edit a product, chosing all of its required features.

- Can choose whether or not the product shows on home page featured product section.

- On submitting the addition/change, super user is sent to the updated product detail page.

#### **Secure Accounts**

Account security is covered by Django's allauth.

#### **CRUD functionality**

*All users:*

- Read all products

*Registered users:*

- Update their delivery details

*Super users:*

- Create, update and delete any products

#### **Static and image file hosting**

Static and image files are served from an Amazon S3 Bucket.

#### **Confirm delete**

When users request to delete an 'orderline' product from their shopping bag or a superuser request to delete an product, an alert pops up to confirm if they wish to do so to prevent accidental deletion.

#### **Access protection**

Routes are protected using Django's @login_required route decorators to ensure non-super-users cannot interfere with the database.

404 and 500 error handling Pages for 404 and 500 errors keep the user on the site when something goes wrong, allowing them to return to the content with minimal disruption.

### **Features Left to Implement**

- Blog app to display industry and Kumite Dojo news, including comments feature to engage with the community and gather more feedback.

- Wishlisht for users to save their favourite products.

- Product reviews, so the users can come back and leave a review after their purchase.

- "Learning App" to show karate techniques and videos etc.

[Back to contents](#contents)

## **Technologies Used**

### **Languages**

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

- [Python](https://www.python.org/)

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### **Frameworks**

- [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/)

- [Django](https://www.djangoproject.com/)

- [jQuery](https://jquery.com/)

### **Database**

- [sqlite3](https://www.sqlite.org/index.html)

- [Heroku Postgres](https://www.heroku.com/postgres)

### **Extensions and kits**

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- [Pillow](https://pillow.readthedocs.io/en/stable/)

- [stripe](https://stripe.com/docs)

### **Project Management**

- [Amazon AWS](https://aws.amazon.com/?nc2=h_lg) (S3, IAM)

- [Github](https://github.com/)

- [Heroku](https://heroku.com)

### **Tools**

- [Balsamiq](https://balsamiq.com/wireframes/)

- [QuicDBD](https://www.quickdatabasediagrams.com/)

- [Font Awesome](https://fontawesome.com/)

- [Google Font](https://fonts.google.com/)

[Back to contents](#contents) 

# **Testing**
For testing results, see [TEST.md](https://github.com/baijuka/matzone_v1/blob/main/TEST.md)

## **Deployment**

### **Requirements**

[Python 3](https://www.python.org/downloads/) - core code

[pipenv](https://pypi.org/project/pipenv/) - package installation and python environment control

[Git](https://git-scm.com/) - version control

[Amazon AWS S3 Bucket](https://aws.amazon.com/) - host the site's static and media files

<details>
<summary>How to clone Matzone and run locally</summary>
<br>

To clone this project from its [GitHub repository](https://https://github.com/baijuka/matzone_v1):

1.From the repository, click **Code**

2.Go to the Clone >> HTTPS section, copy the clone URL for the repository

3.Go to your local IDE open your CLI

4.Change the current working directory to the location where you want the cloned directory to be made

5.Type `git clone`, and then paste the URL you copied in Step 2

```
git clone https://github.com/baijuka/matzone_v1.git
```

6.Press Enter. Your local clone will be created

7.Create a file called env.py to hold your app's environment variables, which should contain the following:

```
import os
os.environ["SECRET_KEY"] = "app secret key of your choice"
os.environ["STRIPE_PUBLIC_KEY"] = "stripe public key generated by stripe"
os.environ["STRIPE_SECRET_KEY"] = "Stripe secret key generated by stripe"
os.environ["STRIPE_WH_SECRET"] = "webhook secret key generated by stripe"
os.environ["DEVELOPMENT"] = "True"
```

To find your Stripe keys, login to Stripe and then under the **Developers** tab look for the 'Publishable Key' and 'Secret Key'

The webhook secret key can be found under Webhooks once you have created an endpoint, which should be set to receive all events and match this url structure:

```
<your site's base url>/checkout/wh/
```

You will need a different endpoint for the local version and deployed site, updating the STRIPE_WH_SECRET accordingly in their respective environment variables.

8.Make sure the following are listed in your .gitignore file to prevent any environment variables being pushed publicly:

```
env.py
__pycache__/
*.sqlite3
*.pyc
```
9.Create and activate virtual environment using:
```
pipenv shell
```

10.Install all the app requirements using:

```
pip install requirements.txt
```

11.Apply database migrations using:

```
python manage.py migrate
```
12.Create a new superuser and fill in your own details using:

```
python manage.py createsuperuser
```

13.The app can now be running loacally using:
```
python manage.py runserver
```
</details>
<details>
<summary>How to deploy to Heroku</summary>
<br>

1.Log In to Heroku

2.Select **Create new app** from the dropdown in the Heroku dashboard

3.Choose a unique name('matzone-v1') for the app and the location nearest to you

4.Under **Resources** search and add **Heroku Postgres** database to your app and choose the free plan

5.Go to your CLI install **dj_database_url** and **psycopg2** so that you can sue Postges on your deployed site, commands are:
```
pipenv install dj_database_url
pipenv install Psycopg2-binary
```

6.Add those packages to requirements.txt using:
```
pip freeze > requirements.txt
```

7.Go to settings.py, setup the new database using code below:
```
import dj_database_url
```
```
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
```

9.Set debug using:
```
DEBUG = "DEVELOPMENT" in os.environ
```

10.Get database url from heroku settings > config vars or using:
```
heroku config
```
https://ms4-matzone-v1.herokuapp.com/checkout/wh/

```
11.Get the new `STRIPE_WH_SECRET` and added it to the config vars.

12.Now your site is fully deployed at [https://ms4-matzone-v1.herokuapp.com/](https://ms4-matzone-v1.herokuapp.com/)

</details>

[Back to contents](#contents) 

## **Testing**

Full details of testing can be found [here.](testing.md)

[Back to contents](#contents) 

## **Credits**

### **Resources and Tutorials**

- [Django Docs](https://docs.djangoproject.com/en/3.2/)

- [Code Institute Boutique Ado walk through](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/)

- [Coding Point - Django Tutorial for beginners](https://www.youtube.com/playlist?list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK) - create "ProductImage" model and attach multiple images to single product.

- [Django Ecommerce | Build Advanced Django Web Application](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/) - learned create variation model and variation manager from this course

### **Code modified from other sources**

- [How to Customize Django Admin](https://www.youtube.com/watch?v=yEJH6sZFsAY&list=PLgnySyq8qZmrxJvJbZC1eb7PD4bu0a-sB&index=7&t=252s) - Banners and featured products

- [Upload Multiple Images to a Django Model without plugins](https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/) - upload multiple images in django admin product model

- [Add a Custom Favicon to your Django Web App](https://www.ordinarycoders.com/blog/article/add-a-custom-favicon-to-your-django-web-app) - add favicon to the site

### **Content**

- [Martial Arts Inc](https://martialartsinc.com/) - used this site as an inspiration

- [Blitzsports.com](https://www.blitzsport.com/) - all products images and descriptions

### **Media**

- [pixabay](https://pixabay.com/) - logo and hero images

### **Acknowledgements**

I would like to thank:

- My mentor Antonio Rodriguez for his patience and generosity with his times.

- Help and support from fellow students in the Slack community.

11.Set `DATABASE_URL` in env.py

12.Log into heroku via Heroku CLI using:
```
heroku login -i
```

13.Migrate the database into Postgres using:
```
python manage.py migrate
```

14.Import all product data using the fixtures created during development

15.Create a new superuser and fill in your own details using:
```
python manage.py createsuperuser
```

16.Install gunicorn
```
pipenv install gunicorn
```

17.Add the package into requirements
```
pip freeze > requirements.txt
```

18.Create a file call **Procfile** and include the following, making sure not to leave a blank line after it:
```
web:gunicorn kumite_dojo.wsgi:application
```

19.Disable Heroku's static file collection (temporarily)
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app kumite-dojo
```

20.Add the hostname of your heroku app to settings.py
```
ALLOWED_HOSTS = ["ms4-matzone-v1.herokuapp.com/", "localhost"]
```

21.Commit all changeds to github

22.Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars** and set Django secret key where you can find in your env.py as **SECRET_KEY**

23.Initial heroku git remote using:
```
heroku git:remote -a matzone
```

24.Deploy to Heroku using:
```
git push heroku main
```

25.Your deployed site can be launched by clicking **Open App** from its page within Heroku.

26.Back in Heroku, select the **Deploy** tab and under **Deployment method** choose GitHub

27.Go to **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**, under **Automatic deploys** choose **Enable Automatic Deploys**
</details>

<details>
<summary>Setting up an S3 Bucket (Amazon Simple Storage Service)</summary>
<br>

1.Create an [Amazon AWS](https://aws.amazon.com/?nc2=h_lg) account

2.Search for **S3** and create a new bucket name it the same as your Heroku app(matzone-v1)

- uncheck block all public access box

- check "I acknowledge that the current settings might result in this bucket and the objects within becoming public."

3.Under **Properties > Static**website hosting

- enable

- index.html as Index document

- error.html as Error document

- save

4.Under **Permissions > CORS** use:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

5.Under **Permissions > Bucket** Policy:

- Generate Bucket Policy and take note of **Bucket ARN**

- Chose **S3 Bucket Policy** as Type of Policy

- For **Principal**, enter *

- Actions **Get Object** and **Put Object**

- Enter **ARN** noted above

- **Add statement**

- **Generate policy**

- Copy the **policy JSON Document** paste into **Edit bucket policy**

- Add a /* onto the end of the **resource key**

- Save changes

6.Under **Access Control List (ACL)**:

- For **Everyone (public access)**, tick **List**

- Accept that everyone in the world may access the Bucket

- Save changes

</details>

<details>

<summary>Setting up AWS IAM (Identity and Access Management)</summary>

<br>

1.From the **IAM dashboard** within **AWS**, select User Groups:

- Create new group e.g. manage-kumite-dojo

- Click through without adding a policy

- **Create Group**

2.Select **Policies**:

- Create policy

- Under **JSON** tab, click **Import managed policy**

- Choose **AmazongS3FullAccess**

- Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy:

```
                "Resource": [
			                "arn:aws:s3:::kumite-dojo",
			                "arn:aws:s3:::kumite-dojo/*"
                ]
```

- Click **next step** and go to **Review policy**

- Give the policy a name e.g. kumite-dojo-policy and description

- **Create Policy**

3.Go back to **User Groups** and choose the group created earlier

- Under **Permissions > Add permissions**, choose **Attach Policies** and select the one just created

- **Add Permissions**

4.Under **Users:**

- Choose a user name e.g. kumite-dojo-staticfiles-user

- Select **Programmatic access** as the **Access type**

- Click Next

- Add the user to the Group just created

- Click Next and **Create User**

5.**Download the .csv containing the access key and secret access key. This will NOT be available to download again**

</details>

<details>

<summary>Connecting Django to S3</summary>

<br>

1.Install boto3 and django-storages

```
pipenv install boto3
pipenv install django-storages
pip freeze > requirements.txt
```

2.Add 'storages' to settings.py ` INSTALLED_APPS`

3.Go to settings.py and set the bucket config, 

```
if "USE_AWS" in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "kumite-dojo"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

```

4.Add the values from the **.csv** you downloaded to your Heroku Config Vars under Settings:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
USE_AWS=True
```
5.Delete the `DISABLE_COLLECTSTATIC` variable from your Config Vars and deploy your Heroku app

6. Create custom_storage.py with code below:

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

7.Go to settings.py, set the static and media files storage and location and override static and media urls in production:

```
# Static and media files
STATICFILES_STORAGE = "custom_storages.StaticStorage"
STATICFILES_LOCATION = "static"
DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
MEDIAFILES_LOCATION = "media"

# Override static and media URLs in production
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
```

8.With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it, making sure they are publicly accessible under **Permissions**

9.Add stripe keys in Config Vars in heroku, making sure the name matches settings.py

10.Add stripe webhook endpoint with the deployed site url:

```
https://ms4-matzone-v1.herokuapp.com/checkout/wh/

```
11.Get the new `STRIPE_WH_SECRET` and added it to the config vars.

12.Now your site is fully deployed at [https://ms4-matzone-v1.herokuapp.com/](https://ms4-matzone-v1.herokuapp.com/)

</details>

[Back to contents](#contents) 

## **Testing**

Full details of testing can be found [here.](testing.md)

[Back to contents](#contents) 

## **Credits**

### **Resources and Tutorials**

- [Django Docs](https://docs.djangoproject.com/en/3.2/)

- [Code Institute Boutique Ado walk through](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/)


### **Code modified from other sources**


### **Content**


### **Media**



### **Acknowledgements**

I would like to thank:

- My mentor Antonio Rodriguez for his patience and generosity with his times.

- Help and support from fellow students in the Slack community.

- Tutor support and student care team.

### **Disclaimer**

This site was developed for educational purposes only.

[Back to contents](#contents) 
