Go back to the [README file](https://github.com/baijuka/matzone_v1/blob/main/README.md)

# **Testing**
## Table of Contents
- [Testing User stories](#testing-user-stories)  
    * [Viewing and navigation](#viewing-and-navigation)
    * [Registration and User Accounts](#registration-and-user-accounts)
    * [Sorting and Searching](#sorting-and-searching)
    * [Purchasing and Checkout](#purchasing-and-checkout)
    * [Admin and Store Management](#admin-and-store-management)
- [Manual testing features](#manual-testing-features)
- [Code Validation](#code-validation)  
    * [HTML](#html)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)
- [Testing browser compatibility](#testing-browser-compatibility)  
- [Testing Responsiveness](#testing-responsiveness)  
- [Bugs and Problems](#bugs-and-problems)  
***

## Testing user stories
### Viewing and navigation:

## Testing user stories
### Viewing and navigation:
**1. As a shopper I want to be able to	view a list of products so that I can see what is available.**

**2. As a shopper I want to be able to	view individual destinations/products so that I can identify the price, description, product rating and other details.**  


**3. As a shopper I want to be able to	easily view my shopping cart total at any time so that I can avoid spending to much.**  
- The total amount is shown at the top of the page below the shopping bag icon:  
![shopping total]()

**4. As a shopper I want to be able to	find information about Space Travel Agency so that I can learn more about space travel and the company.**  
- The user can navigate to the about page by clicking the link in the navbar:  
![about page link]()  
or click the link in the footer:  
![about page link footer]()  

**5. As a shopper I want to be able to	contact the site owner/company so that I can get answer to my questions or get more information about certain things.**  
- The user can navigate to the contact page by clicking the link in the navbar:  
![contact page link]()  
or click the link in the footer:  
![contact page link footer]()  
- There the user can fill in a contact form:  
![contact form]()

**6. As a shopper I want to be able to	see reviews on the products so that I can make a better decision which product to buy.**  
- On the individual product page, the user can scroll down to view reviews:  
![product review]()   


### Registration and User Accounts:
**8. As a user I want to be able to	add, edit and delete my own review so that I can let others/the site owner know my experience and help other users.**  
- When a user is logged in they can go to a product page and click the 'Write Review' button. A form will appear where they can add their review.  
![add review form]()  
- When a user is logged in and the review is theirs, an edit button and a delete icon is shown on their review:  
![edit review button]()  
- If they click the edit button, they will be redirected to the edit review page and alter the form to edit their review:  
![edit review form]()  
- If they click the delete icon a modal pops up to confirm if they want to delete their review:  
![delete review confirmation]()  

**9. As a user I want to be able to	easily register for an account so that I can have a personal account and be able to view my profile.**  
- A user can click the 'MY ACCOUNT' navlink and then click 'SIGN UP' to register for an account (See #13 for the user profile page):  
![sign up link]()  
- There the user can fill in the sign up form:  
![sign up form]() 

**10. As a user I want to be able to easily login or logout so that I can access my account and personal account information.**  
- A user can click the 'MY ACCOUNT' navlink and then click 'SIGN IN' to sign in:  
![sign in link]()  
- When a user is logged in, they can click the 'MY ACCOUNT' navlink and click on 'LOG OUT':  
![sign out link]()  

**11. As a user I want to be able to easily reset my password in case I forget it so that I can recover access to my account when I forget my password.**  
- On the sign in page (see above) there is a 'Forgot Password?' link:  
![forgot password link]()  
- After clicking the link, the user will be redirected to a password recover page, where they can fill in the form to reset their password:  
![reset password form]() 

**12. As a user I want to be able to receive some kind of confirmation after registering so that I can confirm that my account registration was successful.**  
- After registration a confirmation email is sent to the address that is given.  
![confirmation email]() 
![confirmation email header]()   
![confirmation email message]()    

**13. As a user I want to be able to have a personalised user profile so that I can view my personal order history and update my personal account information and see my reviews.**  
- When a user is logged in, they can click on 'MY ACCOUNT' and then on 'my profile' to go to their personal profile page:  
![profile page link]()  
- On that page they have an overview of their delivery information, order history and reviews:  
![profile page overview]()   
For large screens   
![profile page overview]()  
For smaller screens the order history and reviews are in accordeons.  
- The user can update their delivery information by editing the form. Or they can go to the product they reviewed by clicking the 'Go to product' button.  

### Sorting and Searching:
**14. As a shopper I want to be able to	sort products by category so that I can narrow down my search.**  
- On the shop page the user can sort product by category, by clicking the relevant button for large screens.  
![sort category large screen]()
- For smaller screens the user can sort by category by selecting the relevant category from the dropdown button.  
![sort category small screen]() 

**15. As a shopper I want to be able to	filter the list of products by rating, price, name and category so that I can choose a product better.**  
- On the shop page, the user can click on the 'sort by' button and select a filter by which they want the products to be filtered.  
![filter options]()  

**16. As a shopper I want to be able to	search for a product by keywords, such as name or description so that I can find a specific product I’d like to purchase.**  
- The user can click on the search icon at the top of the page and enter a search term. All products name, category and description are queried by the search term:  
![search icon]()   

**17. As a shopper I want to be able to	easily see what I’ve searched for and the number of results so that I can see whether the product I want is available.**  
- When a user enters makes a query, the search term and the number of results are shown above the results.  
![query results]()  

### Purchasing and Checkout:  
**18. As a shopper I want to be able to view items and their details in my shopping bag so that I can see what I will purchase and what the total cost is.**  
- After a user has enter an item in their shopping bag, they can click on the 'GO TO SECURE CHECKOUT' button in the toast card     
![checkout succes button]()   
or click on the shopping bag icon at the top of the page, to go to their shopping bag.  
![shopping bag icon]() 
- On the shopping bag page the details of the items are shown, including the total cost.  
![shopping bag overview]() 

**19. As a shopper I want to be able to update items in my bag so that I can easily make changes to my purchase before checkout.**  
- On the shopping bag page each item has an option to change the quantity. This is done by clicking the + or - buttons and then click 'update'.   
![update quantity buttons]() 
- The user also has the option to delete an item. This is done by clicking the bin icon and then confirm the delete in the modal popup.  

**20. As a shopper I want to be able to easily enter my payment information so that I can check out quickly and with no hassles.**  
- On the shopping bag page, the user can click on the 'secure checkout' button to go the checkout page.  
![secure checkout button]() 
- On the checkout page, the user has to fill in their delivery information and payment details.  
![checkout form]() 

**21. As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I haven’t made any mistakes.**  
- After a successful payment, the user is redirected to the checkout success page, where an overview is shown.  
![order confirmation overview]()  

**22. As a shopper I want to be able to receive an email confirmation after checking out, so that I can keep the details of what I’ve purchased for my records.**  
- After a succesful payment an email is sent to user containing and overview of their purchase.  
![order confirmation email]()  

### Admin and Store Management:  
**23. As an admin I want to be able to add a product so that I can add new items to my store.**  
- When logged in, the admin can go the the 'product management' page by clicking 'my account' and then 'product management' in the navbar.  
![product management link]()  
- The product management page has a form where the admin can add new products.  
![add product form]()  

**24. As an admin I want to be able to edit/update product so that I can change and update my products.**  
- The admin can go to the edit product page by clicking the 'edit' button of the item they want to edit on the shop page:  
![edit product button shop page]()  
or on the 'edit' button on the indivual product page.  
![edit product button individual page]()  
- The edit product page has a prefilled form where the admin can edit the product.  
![edit product form]()  

**25. As an admin I want to be able to delete a product so that I can remove items that are no longer for sale.**  
- The admin can delete product by clicking the 'delete' button of the item they want to delete on the shop page  
![add product form]()  
or by clicking on the 'delete' button on the individual product page.  
![add product form]()  


## Manual testing features
**Responsiveness**   
See [below](#testing-responsiveness) for responsive testing.  

**Register functionality**  
Expected:   
A user can register to the website by filling in the sign up form correctly.

Testing:
1. Go to the signup page by clicking 'my account' and then on 'signup' in the navbar.
2. Don't fill in the signup form and click 'Sign up'.
3. Confirm that a warning message appears.
4. Only fill in an email address and click 'Sign up'.
5. Confirm that a warning message appears.
6. Repeat steps 4 and 5 for username and password.
7. Fill in an email address, a unique username and a password.
8. Confirm that the message 'Verify your e-mail address' appears.
9. Confirm that a toast message appears with the text 'Confirmation e-mail sent to X.' (X = your email address).
10. Go to your email inbox and confirm an email was sent to confirm your email address.
11. Click the link in the email.
12. Confirm that you're redirected to a page to confirm your email address.
13. Click the 'Confirm' button.
14. Confirm you are redirected to the signin page.
15. Confirm a success toast message appears with the text 'You have confirmed X.'.
16. Log out by clicking the logout button in the navbar.
17. Repeat the sign up process with the same details you entered before.
18. Confirm that the message 'A user is already registered with this e-mail address.' appears.

Result:  
A user can register to the website by filling in the register form correctly.

**Login functionality**  
Expected:   
A user can log in to the website by filling in the login form correctly.

Testing:
1. Go to the sign in page by clicking 'my account' and then on 'signin' in the navbar.
2. Don't fill in the login form and click 'Sign in'.
3. Confirm that a warning message appears.
4. Only fill in the username and click 'Sign up'.
5. Confirm that a warning message appears.
6. Only fill in the password.
7. Confirm that a warning message appears.
8. Fill in a wrong username and password.
9. Confirm that the message 'The username and/or password you specified are not correct.' appears.
10. Fill in your username and password.
11. Confirm you are redirected to your home page.
12. Confirm a success toast appears with the text 'Successfully signed in as Y.' (Y is your username).

Result:  
A user can log in to the website by filling in the login form correctly.

**Logout functionality**  
Expected:   
A user is logged out when they click on the logout link in the navbar.

Testing:
1. Log in.
2. Click on 'my account' and then on 'signout' in the navbar..
3. Confirm that you are redirected to a new page with a warning message 'Are you sure you want to sign out?'.
4. Click 'Cancel'.
5. Confirm you are still logged in and are redirected to the home page.
6. Repeat steps 2 and 3.
7. Click 'Sign out'.
8. Confirm you are redirected to the login page.
9. Confirm you are logged out from the website and a success toast message 'You have signed out.' appears.

Result:  
A user is logged out when they click on the logout link in the navbar.  

**Search bar**  
Expected:  
A user can go to the search bar and search products by keyword (name or description).

Testing:
1. On any page, click the search icon at the top of the page.
2. Confirm a search bar pops up.  
3. Fill in the keyword 'lamp' in the search bar.
4. Confirm that you are redirected to the shop page and the product 'Levitating Moon Lamp' is shown.
5. Fill in the keyword 'paramount' in the search bar.
6. Confirm that you are redirected to the shop page and the product 'Wireless headphones' is shown.
7. Click on the image of the headphones to go to the product page.
8. Confirm the word 'paramount' is in the description for the headphones.
9. Fill in the keyword 'banana' in the search bar.
10. Confirm that you are redirected to the shop page the message '0 Products found for "banana"' is displayed and no products are shown.  

Result:  
A user can go to the search bar and search products by keyword (name or description).  

**Category buttons**  
Expected:  
A user can use the category buttons on the products page to display the products by category.

Testing:
1. Go to the products page and click on the 'Accessories' button if you're using a large screen or select 'Accessories' from the dropdown button if you're using a small screen.
2. Confirm that only products with category 'Accessories' are displayed.
3. Repeat steps 1 and 2 for the other categories.
4. Click on the 'All Products' button.
5. Confirm that all recipes are displayed.

Result:  
A user can use the category buttons on the products page to display the products by category.

**Sort select box**  
Expected:  
A user can use the sort button on the products page sort products by price, rating, name or category, both ascending and descending.

Testing:
1. Go to the products page and select 'Price (low to high)' from the 'sort by' dropdown button.
2. Confirm that all products are displayed lowest price first.
3. Select 'Price (high to low)' from the 'sort by' dropdown button.
4. Confirm the all products are displayed highest price first.
5. Repeat steps 1 to 4 for the rating, name and category.

Result:  
A user can use the sort button on the products page sort products by price, rating, name or category, both ascending and descending.

**Indication of special offers/deal**  
Expected:  
A user can see special offers and is reminded to get that offer during shopping.

Testing:  
1. Go to any page and confirm that at the top of the page a banner is shown with the text 'FREE DELIVERY ON ORDERS OVER $50!'.  
2. Go to the shop page, click the image of 'Manta Sleep Mask' to go to that product page.  
3. Click 'Add to bag'.
4. Confirm that the success toast message has the text 'Spend $10.01 more to get free delivery!' at the bottom.  
5. Click on 'Go to secure checkout'.
6. Confirm that the text 'You could get free delivery by spending just $10.01 more!' appears above the 'secure checkout' button.

Result:  
A user can see special offers and is reminded to get that offer during shopping.  

**Error handler pages**  
Expected:  
A user gets a error 404 page when a page can't be displayed and can get back by clicking a button.

Testing:
1. Go to any page.
2. In the browser's address bar, remove or add one or more characters at the end and press enter.
3. Confirm a message '404 page not found' is shown.
4. Confirm there is a button 'Go back home' at the bottom of the page.
5. Click the button and confirm you are redirected to the home page of the website.

Result:  
A user gets a error 404 page when a page can't be displayed and can get back by clickin a button.

**Stripe functionality**  
Expected:  
When a user buys a product, the Stripe payment process is secure and working.  

Testing:  
1. Go to the shop page and select a product and click 'add to bag'. 
2. Click the 'go to secure checkout' button and then the 'secure checkout' button.
3. Fill in the delivery information form.
4. For the credit card payment information use 4242 4242 4242 4242, any date in the future, any cvc number and any postcode and click 'complete order'.  
5. Confirm you are redirected to the checkout succes page with an overview of your order.
6. Confirm a success toast message appears with the text 'Order successfully processed! Your order number is #. A confirmation email will be sent to X. Where # = the ordernumber and X your email address. 
7. Check your email inbox and confirm you have received an email confirmation.
8. Log in to your stripe account, go to 'Payments' and confirm the payment was succesfull.
9. Log in to the django admin of the site, go to Orders and confirm the order was created.
10. Repeat steps 1 to 4 but use 4000 0000 0000 3220 for the credit card payment information.
11. Confirm a 3D Secure 2 authentication message pops up.
12. Click 'Fail' and confirm that you are redirected to the checkout page and a message appears with the text 'We cannot verify your payment method. Please select another payment method and try again.'.
13. Repeat steps 10 and 11 and click 'Confirm' after step 4.
14. Confirm you can repeat steps 5 to 9.
15. Repeat steps 1 to 4, but use 4000 0000 0000 9995 for the credit card payment information.
16. Confirm the payment has failed and a message appears stating that your card has insufficient funds. 

Result:  
When a user buys a product, the Stripe payment process is secure and working.
>Note: for extensive testing of Stripe see their guide on [testing](https://stripe.com/docs/testing)

**Confirmation modal**  
Expected:  
A modal asking the user to confirm their action pops up, when the user clicks a 'delete' button.

Testing:
1. Log in as admin.
2. Go to the shop page and select any product.
3. Click the 'Delete Product' button.
4. Confirm a modal pops up that asks 'Are you sure you want to delete this product?'.
5. Click 'no'.

Result:  
A modal asking the user to confirm their action pops up, when the user clicks a 'delete' button.

> For confirmation modal of delete review, see below CRUD - User - Delete review.

**Social icons**  
Expected:  
The user is redirected to the respective social media page, when they click on a social media icon.

Testing:
1. Go to the footer of any page.
2. Click on a social media icon.
3. Confirm you are redirected to that social media page.
4. Confirm that the page is opened in a new window.
5. Repeat steps 2, 3 and 4 for the other icons.

Result:  
The user is redirected to the respective social media page, when they click on a social media icon.

**Contact form**  
Expected:  
The user can send the site owner a message by filling in the contact form.

Testing:
1. Go to the contact page by clicking on 'About' and then on the 'contact' link in the navbar.
2. Confirm you are redirected to the contact page.
3. Don't fill in the contact form and click 'Send'.
4. Confirm that a warning message appears.
5. Fill in the contact form except for the full name and click the 'Send' button.
6. Confirm that a warning message appears.
7. Repeat steps 5 and 6 for the email address, subject and message inputs.
8. Fill in the complete contact form and click the 'Send' button.
9. Confirm that a success toast appears with the message 'Your message was sent successfully!'.
10. Go to your email inbox and confirm a confirmation email was sent to your email address.
11. Log in to the django admin of the site, go to Received contact forms and confirm the contact form was created.

Result:  
The user can send the site owner a message by filling in the contact form.

#### CRUD (Create, Read, Update, Delete) functionality.
> User:  
**Add Review**  
Expected:  
A new review is added when the user fills in the add review form.

Testing:
1. Log in and go to the shop page.
2. Select any product and scroll down to Reviews.
3. Click on the 'Write a review' button.
4. Confirm a add review form is shown.
5. Don't fill out the review form and click the 'Submit' button.
6. Confirm a warning message appears.
7. Fill in the review form, except the review title.
8. Confirm a warning message appears.
9. Repeat steps 6 and 7 for comment and rating.
10. Fill in the review form and the click the 'Submit' button.
11. Confirm that a succes toast message appears with the text 'Review succesfully added!'
12. Confirm you stay at the product page.
13. Scroll down and confirm that your review is added to the Reviews.

Result:  
A new recipe is added when the user fills in the add review form.

**Edit review**  
Expected:  
An existing review is edited when the user fills in the edit review form.

Testing:
1. Log in.
2. Go to your profile page, go to 'My Reviews' and click the 'Go to Product' button.
3. Confirm you are redirected to the product page and scroll down to Reviews.
4. Confirm that your review has an 'Edit Review' button.
5. Click the 'Edit Review' button and confirm you are redirected to the edit review page.
6. Confirm the form is prefilled with the data of the existing review.
7. Change any of the input fields.
8. Click the 'Edit Review' button.
9. Confirm that a succes toast message appears with the text 'Your review is edited successfully!'
10. Confirm you are redirected to the product page.
11. Scroll down to Reviews and confirm that your change is shown in the review.

Result:  
An existing review is edited when the user fills in the edit review form.

**Delete review**  
Expected:  
A review is deleted when the user clicks on the 'DELETE' icon of a review.

Testing:
1. Log in.
2. Go to your profile page, go to 'My Reviews' and click the 'Go to Product' button.
3. Confirm you are redirected to the product page and scroll down to Reviews.
4. Confirm that your review has a 'Delete' icon.
3. Click the 'delete' icon and confirm a modal pops up with the message 'Are you sure you want to delete this review?'
4. Click 'Delete'.
5. Confirm that a succes toast message appears with the text 'Your review has been deleted.'
6. Confirm you stay at the product page.
7. Scroll down to Reviews and confirm the review is deleted.

Result:  
A review is deleted when the user clicks on the 'DELETE' icon of a review.

> Admin  
**Add Product**  
Expected:  
A new product is added when the admin fills in the add product form.

Testing:
1. Log in as admin.
2. Click on 'my account' and then on the 'product management' link in the navbar.
3. Confirm you are redirected to the product management page.
4. Don't fill out the form and click the 'Add Product' button.
5. Confirm a warning message appears.
6. Fill in the form, except the name field.
7. Confirm a warning message appears.
8. Repeat steps 6 and 7 for the other fields that are required.
9. Fill in the review form and the click the 'Add Product' button.
10. Confirm that a succes toast message appears with the text 'Successfully added product!'
11. Confirm you are redirected to the product page and the product is added.

Result:  
A new product is added when the admin fills in the add product form.

**Edit product**  
Expected:  
An existing product is edited when the admin fills in the edit product form.

Testing:
1. Log in as admin.
2. Go to your shop page and select any product.
3. Confirm you are redirected to the product page.
4. Confirm there is an 'Edit Product' button.
5. Click the 'Edit Review' button and confirm you are redirected to the product management page.
6. Confirm the form is prefilled with the data of the existing product.
7. Change any of the input fields.
8. Click the 'Edit Product' button.
9. Confirm that a succes toast message appears with the text 'Successfully updated product!'
10. Confirm you are redirected to the product page.
11. Confirm that your change is shown on the product page. 

Result:  
An existing product is edited when the admin fills in the edit product form.

**Delete product**  
Expected:  
A product is deleted when the user clicks on the 'DELETE' button of a product.

Testing:
1. Log in as admin.
2. Go to your shop page and select any product.
3. Click the 'DELETE' button of one of your categories (tip: create a new test product first.).
4. Confirm a modal pops up with the message 'Are you sure you want to delete this category?'
5. Click 'YES'.
6. Confirm that a succes toast message appears with the text 'Product deleted!'
7. Confirm you are redirected to the products page.
8. Confirm the product is deleted.

Result:  
A product is deleted when the user clicks on the 'DELETE' button of a product.  

---
## Code validation
### HTML
[W3C Markup Validation Service](https://validator.w3.org/) is used to check for markup validity of the web document.  
Because Jinja template is used on all HTML pages, the source code is taken from the rendered pages to be tested.  
You can validate the rendered page by:  
- Use the source code of the rendered page
    - Right click on the page
    - Click 'show source code'
    - Copy all HTML
    - Paste it into the validator. 

Or  
- Enter the url of the Heroku live link.

However, when authentication is used, the live link can't be used to validate the page.
Furthermore, the live site of Heroku takes a while to update after committing.   
Therefore I've opted to use the source code to render the pages.

Running the code through the validator gives: 
#### For about.html:
- 3 errors and 1 warning three times are shown.  

1. *Element `<hr>` not allowed as child of element `<ul>` in this context.*  
Fix:  
You can't have header tags as children within a `<ul></ul>`, you can only have `<li>` elements as children.  
So wrap the `<hr>` in `<li></li>`.  
2. *No `<li>` element in scope but a `<li>` end tag seen.*  
Fix:  
Remove the extra `<li>` element.  
3. *The aria-labelledby attribute must point to an element in the same document.*  
The aria-labelledby doesn't point to a matching id. Add `id="offcanvasNavbarLabel"` to the `<h3>` in the offcanvas 
component.  
4. *The type attribute is unnecessary for JavaScript resources.*  
Fix:  
Up until html5 type was needed for the browser to distinguish between js and other text. With html5 it is no longer needed.
The default type for `<script>` tags is JavaScript, so you don’t need to include the type for JS resources.    
Remove the `type="text/javascript"`.  
This will be done for all the other scripts on other pages as well.  

#### For bag.html:  
- No errors or warnings to show.  
    > Note: I've added a product to the bag first.  

#### For checkout.html:  
- No errors or warnings to show.  

#### For checkout_success.html:
- No errors or warnings to show.  

#### For contact.html:  
- No errors or warnings to show.  

#### For index.html:
- No errors or warnings to show.  

#### For add_product.html:  
- 2 errors are shown.  
1. *Duplicate attribute id*  
Fix:  
The include of `include "django/forms/widgets/attrs.html"` already has an id attribute in there.  
`Select Image <input id="new-image" type="{{ widget.type }}" name="{{ widget.name }}"{% include "django/forms/widgets/attrs.html" %}>`  
So remove the `id="new-image"` from the select image.  
2. *Element p not allowed as child of element strong in this context.*  
Fix:  
remove `<strong>`.  

#### For edit_product.html:  
- 2 errors are shown.  

1. *Duplicate attribute class.*  
Fix:  
Remove the merge the 2 classes into 1 class.  
2. *An img element must have an alt attribute, except under certain conditions.*  
Fix:  
Add an alt to the img element in custom_clearable_file_input.html.   

#### For products.html:  
- 2 errors and 2 warnings are shown 5 times.  

1. *Duplicate ID confirmDelete.*  
Fix:  
Create unique id's by adding the product id to delete modals by use of Jinja notation:  
`id="confirmDelete{{ product.id }}"`  
2. *Duplicate ID exampleModalLabel.*  
Fix:  
Create unique id's by adding the product id to to `<h6>` by use of Jinja notation:  
`id="exampleModalLabel{{ product.id }}"`  
> This has been done on other pages with similar forms as well.  
#### For product_detail.html:  

1. *Attribute placeholder not allowed on element select at this point.*  
Fix:  
Remove the placeholder from the select element by deleting `self.fields['rating'].widget.attrs['placeholder'] = 'Add your rating'` from the review model.  

#### For products.html:  
- No errors or warnings to show.  

#### For product_detail.html:  

1. *Duplicate ID id_title*
Partial Fix:  
Crispy forms renders the title field with it's own id based on the input title.
According to the django crispy forms docs you can change the id of the fields (label and input/select) by changing the
attribute in the forms.py.  
So I decided to make a second class named EditReviewForm and change the id's in there:  
    ```
    class EditReviewForm(forms.ModelForm):
        """ Create a form fro users to add a review """
        class Meta:
            model = Review
            fields = ('title', 'comment', 'rating')
            widgets = {
                'title': forms.TextInput(attrs={'id': 'edit_title'}),
                'comment': forms.Textarea(attrs={'id': 'edit_comment'}),
                'rating': forms.Select(attrs={'id': 'edit_rating'}),
            }
        ...
    ```  
I changed the form rendering on reviews.html:  
    ```
    {% csrf_token %}
    <div class="div">
        {{ review_edit_form.title|as_crispy_field }}
    </div>
    <div class="div">
        {{ review_edit_form.comment|as_crispy_field }}
    </div>
    <div class="div">
        {{ review_edit_form.rating|as_crispy_field }}
    </div>
    ```  
This fixes the duplicate ID's for the input and select fields.  
However, the duplicate ID's for the `<div>`'s are still there.  
Add Picture
After a long session with Tutoring we still couldn't fix the error.  
To be on the safe side and to make the page pass the W3C validation, I've decided to put the edit review option on a different page.    
After creating a separate edit review page no more errors or warnings are shown.  

#### For profile.html:  
- 1 error is shown.  
Add picture
1. *Attribute placeholder not allowed on element select at this point*  
Fix:  
The form is rendering a placeholder for the country select element. So the select element for country shouldn't get a placeholder. 
Upon inspecting the forms.py in profile. I noticed that all elements get a placeholder with respective name due to:  
    ```
    for field in self.fields:
        if field != 'default_country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
    ```
So the to not give the country element a placeholder, the last line should be inside the `if field != 'default_country':` statement.  
    ```
    for field in self.fields:
        if field != 'default_country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
    ```
#### For edit_review.html:  
- No errors or warnings to show.  

#### For signup.html:  
- No errors or warnings to show.  

#### For signin.html:
- No errors or warnings to show. 

#### For 403.html:
- No errors or warnings to show. 

#### For 404.html:
- No errors or warnings to show. 

#### For 500.html:
- No errors or warnings to show. 

---
### CSS  
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) is used to check the CSS of the web document.
Running the code through the validator gives:
#### For base.css:
- No errors are found. 

#### For checkout.css:  
- No errors are found.  

#### For product.css:  
- No errors are found.  

#### For profile.css:  
- No errors are found.

---
### Javascript  
[JSHint](https://jshint.com/) is used to check the validity of the Javascript of the web document.  
It is recommended to add **`/* jshint esversion: 6 */`** at the top of the .js file to tell JSHint that your code uses ECMAScript 6 specific syntax.  

Running the code through the validator gives:
#### For stripe_elements.js:  
- No errors or warnings are shown.  

#### For countryfield.js:
- No errors or warnings are shown.  

---
### Python  
[PEP8 online](http://pep8online.com/) is used to check the python code for PEP8 requirements.
Due to the large amound of python files, I'll only mention the files with big errors or warnings, leaving out the 
whitespace or line to long errors.
Before checking the app.py file, I tried to remove as many mistakes beforehand, such as extra whitespaces, maximum
code line length of 72, correct line breaks, etc.  
- No large errors were found.

---
## Testing browser compatibility
I've tested the website on Safari, Chrome and Mozilla Firefox.  
The testing was done by:

- Visually checking the pages.
- Checking all links.
- Checking CRUD functionality.

No issues arose during testing.  

---
## Testing responsiveness
To test the responsiveness of the website, I've used Chrome Dev Tools by:
- right clicking on the page
- click inspect 
- click toggle device toolbar  
- select the different devices.  

The testing was done on widths down to a screen resolution of 280px.  
All the elements on each page were checked.  

No issues arrose.

## Bugs and problems
