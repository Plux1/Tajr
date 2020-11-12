from django.test import TestCase
from main import models
from django.core.files.images import ImageFile
from decimal import decimal

class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        product = models.Product(name='The cathedral and the bazaar', price=Decimal('10.00'))
        product.save()
        with open("C:\Users\Target\Desktop\issa.jpg", 'rb') as f:
            image = models.ProductImage(product=product, image=ImageFile(f, name='tctb.jpg'))
        
        image.refresh_from_db()
        with open("C:\Users\Target\Desktop\issa.jpg", 'rb') as f:
            expected_content = f.read()
            assert image.thumbnail.read() == expected_content
        
        image.thumbnail.delete(save=False)
        image.image.delete(save=False)