# Installation

Web application for user registration made in Python. Install using:

```
git clone https://github.com/mpedziwiatr02/JPWP-User-Registration
cd JPWP-User-Registration
pip install -r requirements.txt
python3 manage.py runserver
```
# Task 1

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

Learn more [here](https://docs.djangoproject.com/en/5.0/topics/db/models/).

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

Send a screenshot containing your code.

# Task 2

Unless you’re planning to build websites and applications that do nothing but publish content, and don’t accept input from your visitors, you’re going to need to understand and use forms.

Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input.

Learn more [here](https://docs.djangoproject.com/en/5.0/topics/forms/).

Modify file `users/forms.py`. Add previously created fields to a form of your choice. Verify that the fields are correctly displayed, modifiable and saved to the database after submitting changes.

Send a screenshot containing your code and newly added fields in your browser.

# Task 3

Django has support for writing asynchronous views, along with an entirely async-enabled request stack if you are running under ASGI. Async views will still work under WSGI, but with performance penalties, and without the ability to have efficient long-running requests.

Learn more [here](https://docs.djangoproject.com/en/5.0/topics/auth/default/) about the authentication system and [here](https://docs.djangoproject.com/en/5.0/topics/async/) about asynchronous operations support.

Modify file `users/views.py`. Try changing the login / logout flows for asynchronous operation. Use functions `alogin(request, user, backend=None)` and `alogout(request)` (added in Django 5.0).

Send a screenshot containing your code and successful user login message in your browser.
