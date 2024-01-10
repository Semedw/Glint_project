from django.db import models

from core.utils.slug_title import generate_slug

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Service(BaseModel):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    price = models.FloatField(default=10.99)
    slug = models.SlugField(null = True, blank = True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Service, self).save(*args, **kwargs)

class About(BaseModel):
    content = models.TextField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Team(BaseModel):
    name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length = 500, null = True, blank = True)
    facebook = models.CharField(max_length = 500, null = True, blank = True)
    github = models.CharField(max_length = 500, null = True, blank = True)
    linkedin = models.CharField(max_length = 500, null = True, blank = True)
    instagram = models.CharField(max_length = 500, null = True, blank = True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name


class Project(BaseModel):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField()
    developer = models.CharField(max_length = 255)
    developer_quote = models.TextField()
    developer_position = models.CharField(max_length = 255)
    developers_img = models.ImageField(null=True, blank=True,)
    slug = models.SlugField(null = True, blank = True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Project, self).save(*args, **kwargs)


class Testimonials(BaseModel):
    name = models.CharField(max_length = 255)
    job = models.CharField(max_length = 255)
    quote = models.TextField()

    class Meta:
        verbose_name = 'Testiomonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class Gallery(BaseModel):
    image = models.ImageField()

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'


class Contact(BaseModel):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.first_name
    

class Subscriber(BaseModel):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.full_name    

class Banner(BaseModel):
    title = models.CharField(max_length = 500)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
