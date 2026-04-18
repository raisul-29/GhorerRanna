from django.contrib import admin
from .models import User, Coupon, Menu, Order, OrderDetails, Payment, Delivery, Feedback, Subscription

# Register your models here.
admin.site.register(User)
admin.site.register(Coupon)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Feedback)
admin.site.register(Subscription)