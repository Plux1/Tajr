from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProductImage

THUMBNAIL_SIZE = (300, 300)


@receiver(pre_save, sender=ProductImage)
def generate_thumbnail(sender, instance, **kwargs):
    image = Image.open(instance.image)
    image = Image.convert('RGB')
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIS)
    
    temp_thumb = BytesIO()
    image.save(temp_thumb, 'JPEG')
    temp_thumb.seek(0)

    instance.thumbanil.save(instance.image.name, ContentFile(temp_thumb.read()), save=False)
    temp_thumb.close()