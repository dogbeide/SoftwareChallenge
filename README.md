# Software Developer Challenge

## Challenge 1:
Read through the rest of the assignment, decide which technologies to use and explain why you chose what you chose. As a reminder we at Paytm are dealing with millions of concurrent users, just sayin’ :)
---------------------------------------------------
### Core Backend Framework: Django
 - Fast initial implementation.
 - Scalable (compared to Flask).
 - Python is more optimized for speed (compared to R.o.R for syntactic sugar).

### REST interfacing: Django REST framework
 - Supports Django's authentication system.
 - Built-ins for fast development, open source implies consistent improvement.
 - Supports Django's ORM.
 - Supports bandwidth throttling for all clients (anonymous & authenticated) as well as in-memory storage which can throttle disk bandwidth too. Will be useful in big data web applications.

### Database: postgreSQL
 - Open source, continuous development & support
 - Built to work with Django's JSONField ORM class, can store tweet JSON.
 - Can be scaled to big data


## Challenge 2:
Create a deployable “Hello World” Server exposing simple REST “Hello World” API. It is going to be a base for your application for this assignment.

## Challenge 3:
Pick one of the available online API’s such as Twitter (https://dev.twitter.com/overview/api), LCBO (https://lcboapi.com/) or Weather (https://openweathermap.org/api), create and implement a flow involving that API and user of your application. For example, your application might have following UI:

![Sample UI](./sample-ui.png?raw=true "Sample UI")


User will insert text and click the button `Search` and your application will search tweets that contain submitted string. Note: it is only an example, go wilder than that :)

## Challenge 4:
Make your application secure and personalized by making people to have to sign-up / login. Bonus points, if users will be able to reset their passwords.

##Challenge 5:
Make your application persistent. Whatever functionality your application has, after restart, make it possible to view a history of user activity or anything else you deem necessary.

## Challenge 6:
Test your application.

## Challenge 7:
Let us know how we can use it. You could either provide us with a zipped file containing your solution or a link to your Github repository containing one.
### How to use:
1. git clone <thisrepo.git>
2. pip install -r requirements.txt
3. python manage.py runserver

## Bonus (optional):
Add an “I’m feeling lucky button” that does a random search, but make sure that same result is not returned twice or that you don’t return a page that the user already viewed. Use the user stored history to do so. Since going through the history can potentially be costly, suggest and optionally implement optimization mechanism to avoid hitting the storage every time.
