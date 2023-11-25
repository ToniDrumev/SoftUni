import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Profile, Product, Order


def get_profiles(search_string: str = None) -> str:
	if search_string is None:
		return ""

	profiles = Profile.objects.filter(
		Q(full_name__icontains=search_string) |
		Q(email__icontains=search_string) |
		Q(phone_number__icontains=search_string)
	).order_by(
		'full_name',
	)

	result = []

	for profile in profiles:
		result.append(f"Profile: {profile.full_name}, email: {profile.email}, phone number: {profile.phone_number}"
					  f", orders: {profile.orders.count()}")

	return "\n".join(result)


def get_loyal_profiles() -> str:
	profiles = Profile.objects.get_regular_customers()

	if not profiles:
		return ""

	return "\n".join(f"Profile: {profile.full_name}, orders: {profile.orders_count}"
		for profile in profiles
	)


def get_last_sold_products() -> str:
	order = Order.objects.prefetch_related('products').last()

	if order is None or not order.products.exists():
		return ""

	products = [p.name for p in order.products.all()]

	return f"Last sold products: {', '.join(products)}"


def get_top_products() -> str:
	top_products = Product.objects.annotate(
		num_orders=Count('order')
	).filter(
		num_orders__gt=0
	).order_by('-num_orders', 'name')[:5]

	if not top_products:
		return ""

	result = ["Top products:"]

	for p in top_products:
		result.append(f"{p.name}, sold {p.num_orders} times")

	return "\n".join(result)


def apply_discounts() -> str:
	orders_to_discount = Order.objects.annotate(
		products_count=Count('products')
	).filter(
		products_count__gt=2, is_completed=False
	).update(
		total_price=F('total_price') * 0.9
	)

	return f"Discount applied to {orders_to_discount} orders."


def complete_order() -> str:
	order = Order.objects.filter(
		is_completed=False,
	).order_by(
		'creation_date'
	).first()

	if not order:
		return ""

	order.is_completed = True
	order.save()

	for p in order.products.all():
		p.in_stock -= 1

		if p.in_stock == 0:
			p.is_available = False

		p.save()

	return "Order has been completed!"

