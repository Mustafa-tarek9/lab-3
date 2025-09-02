# Simple script to create sample products using Django ORM.
# Run from project root after migrations:
# python manage.py shell < sample_data/create_sample.py

from products.models import Product
Product.objects.all().delete()
for i in range(1, 13):
    Product.objects.create(
        name=f"Sample Product {i}",
        slug=f"sample-product-{i}",
        description="This is a sample product created for demo purposes.",
        price=9.99 + i,
        is_available=True
    )
print("Created sample products.")
