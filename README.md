# Installation

Web application for user registration made in Python. Install and run using:

```
git clone https://github.com/mpedziwiatr02/JPWP-User-Registration
cd JPWP-User-Registration
pip install -r requirements.txt
python3 manage.py runserver
```

# Task 1

AsyncIO is a library to write concurrent code using the async/await syntax. It's used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

Learn more about asyncIO [here](https://docs.python.org/3/library/asyncio.html).

Modify file `task1.py`. Make functions `main()` and `mecz(value)` act as coroutines. Use `asyncio.run()`, `asyncio.gather()` and `asyncio.sleep()`.

Send a screenshot containing your code in `task1.py`.

# Task 2

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

Learn more about Models [here](https://docs.djangoproject.com/en/5.0/topics/db/models/).

Modify file `users/models.py`. Add two different fields to the `Profile` model. Remember to apply database migrations after your modifications. Create migrations using:

```
python3 manage.py makemigrations
python3 manage.py makemigrations <app>
```

Then apply them using:

```
python3 manage.py migrate
python3 manage.py migrate <app>
```

If you encounter any problems, try flushing the database (use with caution in production environments):

```
python3 manage.py flush
```

Send a screenshot containing your code in `models.py`.

# Task 3

Unless you’re planning to build websites and applications that do nothing but publish content, and don’t accept input from your visitors, you’re going to need to understand and use forms.

Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input.

Learn more about Forms [here](https://docs.djangoproject.com/en/5.0/topics/forms/).

Modify file `users/forms.py`. Add previously created fields to a form of your choice. Verify that the fields are correctly displayed, modifiable and saved to the database after submitting changes.

Send a screenshot containing your code in `forms.py` and newly added fields in your browser.

# Task 4

Django’s template language is designed to strike a balance between power and ease. It’s designed to feel comfortable to those used to working with HTML. If you have any exposure to other text-based template languages, such as Smarty or Jinja2, you should feel right at home with Django’s templates.

Learn more about Templates [here](https://docs.djangoproject.com/en/5.0/ref/templates/language/).

Modify `users/models.py` and `users/forms.py`. Create a completely new form with new fields using the `Profile` model. Add form validation and saving in `users/views.py`. Then modify the `users/templates/users/profile.html` template to display your form. Don't forget about database migrations.

Send a screenshot containing your code in `forms.py`, `profile.html` and a newly added form in your browser.

# Task 5

Django has support for writing asynchronous views, along with an entirely async-enabled request stack if you are running under ASGI. Async views will still work under WSGI, but with performance penalties, and without the ability to have efficient long-running requests.

Learn more about the authentication system [here](https://docs.djangoproject.com/en/5.0/topics/auth/default/) and asynchronous operations support [here](https://docs.djangoproject.com/en/5.0/topics/async/).

Modify file `users/views.py`. Try changing the login / logout flows for asynchronous operation. Use functions `alogin(request, user, backend=None)` and `alogout(request)` (added in Django 5.0).

Send a screenshot containing your code in `views.py` and a successful user login message in your browser.
