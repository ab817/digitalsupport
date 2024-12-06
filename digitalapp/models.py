# blog/models.py
from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
import  datetime
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

class PortalSetting(models.Model):
    show_popup = models.BooleanField(default=True)
    popup_image = models.ImageField(upload_to='popup_images/', blank=True, null=True)
    #show_image = models.BooleanField(default=True)

    def __str__(self):
        return "Portal Settings"

class Feedback(models.Model):
    feedback_text = models.TextField()
    questioned_by = models.CharField(max_length=100)
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.questioned_by} on {self.submitted_on}'

class DigitalProduct(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/')
    pdf = models.FileField(upload_to='product_pdfs/', blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.name

class Notice(models.Model):
    NOTICE_FORMATS = [
        ('PDF', 'PDF'),
        ('JPG', 'JPG'),
        ('PNG', 'PNG'),
    ]

    notice_number = models.CharField(max_length=20, unique=True, blank=True)
    notice_name = models.CharField(max_length=255)
    link_to_download = models.FileField(upload_to='notices/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png'])
    ])
    notice_date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.notice_name


@receiver(pre_save, sender=Notice)
def generate_notice_number(sender, instance, **kwargs):
    if not instance.notice_number:
        last_notice = Notice.objects.order_by('id').last()
        if last_notice:
            last_number = int(last_notice.notice_number[1:])
            instance.notice_number = f"N{last_number + 1:04d}"
        else:
            instance.notice_number = "N0001"