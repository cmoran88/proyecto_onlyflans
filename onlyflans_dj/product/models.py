import uuid
from django.db import models

class Flan(models.Model):

    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 64)
    description = models.TextField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

    def formatted_price(self):
        formatted = f"${self.price:,.0f}".replace(',', 'x').replace('.', ',').replace('x', '.')
        return formatted

'''
● flan_uuid del tipo UUIDField
● name del tipo CharField (largo máximo 64 caracteres)
● description del tipo TextField
● image_url del tipo URLField
● slug del tipo SlugField
● is_private del tipo BooleanField
'''