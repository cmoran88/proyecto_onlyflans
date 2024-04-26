import uuid
from django.db import models

class ContactForm(models.Model):

    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length = 64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name

