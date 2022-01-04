<h1 align="center">Matzone Online Shop</h1>

![Matzone](./static/images/homepage.jpg)

# [Matzone](https://ms3-bju-project.herokuapp.com/)

## Contents
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

   |As a    |I want to be able to..                   |So that I can…                                                                    
---|--------|-----------------------------------------|----------------------------------------------------------------------------------
 1.|Shopper |View a list of products                  |Select some to purchase                                                           
 2.|Shopper |View individual product details          |Identify the price, description, product rating, product image and available sizes
 3.|Shopper |Easily view the items in shopping bag and total of my purchases at any time |Avoid spending too much
 4.|Site User|Easily register for an account |Have a personal account and to be able to view my profile
 5.|Site User|Easily login and logout  |Access my personal account information
 6.|Site User|Receive an email confirmation after registering |Verify that my account registration was successful
 7.|Site User|Have a personalised user profile |View my personal order history, order confirmation and save my payment information
 8.|Shopper |Sort the list of available products |Easily identify the best rated, best priced and categorically sorted products
 9.|Shopper |Sort a specific category of product |Find the best priced or best rated product in a specific category or sort the products in that category by name
10.|Shopper |Sort multiple categories of products simultaneously |Find the best priced or best rated products across broad categories such as ‘Rubber mats’ or ‘Coir mats’ etc.
11.|Shopper |Search for a product by name or description |Find a specific product I would like to purchase
12.|Shopper |Easily see what I’ve searched for and the number of results |Quickly decide whether the product I want is available
13.|Shopper |Easily select the size and quantity of a product when purchasing it |Ensure I don’t accidently select the wrong product, size or quantity 
14.|Shopper |View items in my bag to be purchased |Identify the total cost of my purchase and all items I will receive
15.|Shopper |Adjust the quantity of individual items in my shopping bag |Easily make changes to my purchase before checkout
16.|Shopper |Easily enter my payment information |Checkout quickly and without any hassles
17.|Shopper |Feel my personal and payment information is safe and secure |Confidently provide the information needed to make a purchase
18.|Shopper |View an order confirmation after checkout |Verify that I haven’t made ay mistake
19.|Shopper |Receive an email confirmation after checkout |Keep the confirmation of what I have purchased for my records
20.|Shopper |Review and rate the products I purchased |I can provide my views and experience about the product which will help other shoppers make decision before buying a specific product
21.|Shopper |Contact the Store Owner for details about a product or service |I can clear my doubts about a particular product or service
23.|Store Owner |Add a product |Add new items to my store
24.|Store Owner |Edit/Update a product |Change product prices, descriptions, images and other product criteria
25.|Store Owner |Delete a product |Remove items that are no longer for sale

## **Database Model**

Relational databases are widely used to store complex data.  It's primary key, foreign key ralationships makes data retrieval easy for the developers. It's speed, acccuracy, simplicity, security, accessibility and multi user functionality are the major factors make it popular. This project uses various models that need to establish relationships between and in such case the developer decided to use relational database for backend storage. SQLite was used during development and Heroku Postgres in production. The database schema diagram explains the relationship between models.


### **Key Models**

#### **User**

- This model is created by Django admin for user creation and management.

#### **UserProfile**

- Created on registration for each user, holds user information that can be used to speed up checkout process.

- Stores order history for previous orders to encourage repeat orders.

#### **Product**

- Holds the infomation about a product including name, description, basepprice, image and rating.

- The foreign key to 'ProductImage' is very important as it allows multiple images attach to this particular product.

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

