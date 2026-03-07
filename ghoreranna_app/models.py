from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Bachelor Employee', 'Bachelor Employee'),
        ('Home Cook', 'Home Cook'),
        ('Delivery Staff', 'Delivery Staff'),
        ('Admin', 'Admin'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.TextField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.role})"



class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    homecook = models.ForeignKey(User, on_delete=models.CASCADE, related_name='menus', limit_choices_to={'role': 'Home Cook'})
    meal_type = models.CharField(max_length=100)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    availability_status = models.BooleanField(default=True)

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return f"{self.item_name} - {self.homecook.name}"

