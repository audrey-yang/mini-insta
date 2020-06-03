# Mini-Instagram
For the PennApps Dev Team Technical Challenge

## Instructions
From [this Django tutorial](https://docs.djangoproject.com/en/3.0/intro/reusable-apps/).
1. Add "instagram" to your INSTALLED_APPS setting, i.e.
    ```
    INSTALLED_APPS = [
        ...
        'instagram',
    ]
    ```

2. Include the polls URLconf in your project urls.py, i.e.
    ```
    path('instagram/', include('instagram.urls')),
    ```

3. Run ``python manage.py migrate`` to create the instagram models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ 
    (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to use the app.

## Known Bugs
A user that is not logged in can still access the pages to post and view the user's posts by entering the url. However, this path will always lead to some error, so they can't actually use the app that way.

## Functionality
My site has all the functionalities of the example site–users can create text posts and delete them, as well as view all the posts from different users. To create and authenticate users, I used Django's own authentication system. I also added in styling with CSS and a like button with a tally of likes. 

## General Thoughts on the Assignment
This was my first time using Django, so I think that this assignment was a really effective way of learning the framework. I think if I had no experience, though, this would have been extremely tough.

## Credits
Thanks to my friend [Sahana Sundar](https://www.instagram.com/bortlesandotherstuff/) for the artwork displayed on the login page! 