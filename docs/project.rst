Project Summary
===============

From this project I learned how to further use the Python Django framework
to develop web applications. I learned how to implement user authentication
and how to implement a contact form.

Goals Achieved
--------------
Goal 1 - Home page of application created.

Completed the home page of application which includes a navigation bar.
On the home page there is a "values" section, a pricing section, a
testimonial section and a contact section.
Note: Contact section not working yet

Goal 2 - User authentication added to application.

Added ability for users to register for an account, then they can log in
and view and edit their specific account details. Once logged in,
the user has extra options on the navbar where there can view their
workout program and their meal plan provided by their trainer.

Goal 3 - Ability to contact trainer added

User can now successfully use the contact section and their message will be
received in the terminal. Was not able to set it up so that when a user sends
a message, it will go to the trainers email. (This option required money, and
since this is a fictional application, I chose to not add this)

Goal 4 - User Profile created 

User can look at their profile page and make changes to any of their information. 
There are a variety of different fields they can fill out including height and weight
since this is a personal trainer application. In the profile page they can also change
their membership plan and change their profile picture. 

Goal 4 - Ability to reset password (partially working)

The reset password function is partly working and there are no errors that come up in 
the console but it does not properly send a link to reset the password. Ideally, 
a link should show up in the console that can be clicked on to reset the password. 
Was not able to set it up so that when a user does "forgot password", it will email them 
a link to the email they used at sign up. (This option required money, and since this is 
a fictional application, I chose to not add this feature)


Known Issues
------------
1. Reset Password function only partially working
2. Lack of comments, need to add comments
3. Form fields span across the entire width of page

   * I would like the width of each field to be smaller 

4. Unit testing not working for all models, forms, and views. 

   * So far, unit testing is only working for some forms, and some views. 

5. Having isses using the "Sphinx automodule" to automatically add code to documentation. 


Features To Be Added V2
-----------------------
1. Enhance the design of the application

   * Make application more interactive
   * Possibly use different font
   * Include more JavaScript and Bootstrap

2. Create a "Meet our team" page
3. Create a seperated "Testimonials" page
4. Create fictional workout program and meal plan to be added to app 
5. Add statistics page where user can add pictures, their measurements, weight. 

   * Previous statistics would remain on the page so that the user can keep track of their progress


