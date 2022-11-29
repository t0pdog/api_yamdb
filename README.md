# The YaMDb project
The YaMDb project collects reviews (Review) of users on works (Title). There are 3 categories: "Books", "Movies", and "Music". The list of categories (Category) can be expanded.
The works themselves are not in YaMDb; you cannot watch a movie or listen to music here.
In each category, there are works: books, films, or music. For example, in the category "Books" there may be works "Winnie the Pooh and All-All-All" and "The Martian Chronicles", and in the category "Music" - the song "Davecha" by the group "Insects" and the second suite of Bach. The output can be assigned to a genre from the preset list (for example, "Fairy Tale", "Rock" or "Arthouse"). New genres can only be created by the administrator.
Users leave text reviews (Review) for the works and issue a rating.

# The technology stack is available in requirements.txt

# Resources API YaMDb
**AUTH**: authentication.

**USERS**: users.

**TITLES**: Titles that are being reviewed (a specific movie, book, or song).

**CATEGORIES**: categories (types) of works ("Movies", "Books", "Music").

**GENRES**: genres of works. One work can be tied to several genres.

**REVIEWS**: reviews of works. The review is tied to a specific product.

**COMMENTS**: Comments on reviews. The comment is tied to a specific review.

# User registration algorithm
User sends a POST request with an email parameter to `/api/v1/auth/email/`.
YaMDB sends an email with a confirmation code (confirmation_code) to the email address (feature under development).
The user sends a POST request with the email and confirmation_code parameters to `/api/v1/auth/token/`, in response to the request, he receives a token (JWT token).
These operations are performed once, when the user registers. As a result, the user receives a token and can work with the API by sending this token with each request.

# User Roles
**Anonymous** - can view descriptions of works, read reviews and comments.

**Authenticated user (user)** - can read everything, like Anonymous, can additionally publish reviews and rate works (films / books / songs), can comment on other people's reviews and rate them; can edit and delete their reviews and comments.

**Moderator** - the same rights as an Authenticated User plus the right to delete and edit any reviews and comments.

**Administrator (admin)** - full rights to manage the project and all its contents. Can create and delete works, categories and genres. Can assign roles to users.

**Django Administrator** - Same rights as the Administrator role.


### How to start a project:

Clone a repository and change to it on the command line:
```
git clone https://github.com/t0pdog/api_yamdb.git
```
cd api_yamdb
```
```
Create and activate virtual environment:
```
python -m venv venv
```
source venv/Scripts/activate
```
```
Install dependencies from a file requirements.txt:
```
pip install -r requirements.txt
```
```
To start the development server, while in the project directory, run the commands:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
```
Run the project:
```
python manage.py runserver
```
```
The project is launched and available at [localhost:8000](http://127.0.0.1:8000/).

Documentation is available at the address:

http://127.0.0.1:8000/redoc/
```

### Here is an example of endpoint request and its response:

Getting a list of all works
Get a list of all objects.

Access rights: Available without a token ( GET request):

```
http://127.0.0.1:8000/api/v1/titles/
```

# Server response:
```
[{
"count": 0,
"next": "string",
"previous": "string",
"results": [
{
"id": 0,
"name": "string",
"year": 0,
"rating": 0,
"description": "string",
"genre": [
{
"name": "string",
"slug": "string"
}],
"category": {
"name": "string",
"slug": "string"
}}]}]
```