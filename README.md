# Django example project (mysite)

This project demonstrates:
- Product model with ImageField
- Class-based views (ListView, DetailView)
- Pagination and simple search (query param `q`)
- Templates using `{% url %}` and template comments
- Admin registration with prepopulated slug
- Serving media in development

## Requirements

- Python 3.8+
- Install dependencies:
```
pip install -r requirements.txt
```

## Setup (local dev)

1. Create & activate virtualenv
2. Install dependencies
3. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```
4. Create admin user:
```
python manage.py createsuperuser
```
5. Collect static (optional)
6. Run dev server:
```
python manage.py runserver
```
- Admin: http://127.0.0.1:8000/admin/
- Products list: http://127.0.0.1:8000/products/

## Notes

- Media files uploaded via admin will be saved to `media/`.
- Install Pillow to support ImageField.
