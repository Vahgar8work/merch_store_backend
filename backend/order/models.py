from django.db import models
from products.models import Product
from login.models import CustomUser as User
from discounts.models import DiscountCode

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    mail_added = models.BooleanField(default=False)
    discount_code = models.ForeignKey(DiscountCode, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)

    @property
    def total_amount(self):
        total = sum(item.product.price for item in self.order_items.all())
        if self.discount_code and self.discount_code.is_valid():
            discount = total * (self.discount_code.discount_percentage / 100)
            total -= discount
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='order_items')
    printing_name = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=5, null=True, blank=True)
    image_url = models.URLField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.order.id}_{self.product.name}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_intent_id = models.CharField(max_length=100)  # Store Stripe Payment Intent ID

    def __str__(self):
        return f"Payment for Order {self.order.id}"
