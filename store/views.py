import os

import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.views.generic import TemplateView
from dotenv import load_dotenv

from .models import Item, Order, OrderItem

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
DOMAIN = os.getenv("DOMAIN")


class ItemDetailView(DetailView):
    model = Item
    template_name = "index.html"


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class GetStripeSessionId(View):
    def get(self, request, *args, **kwargs):
        target = request.GET.get('target')
        line_items = select_target(target, self)
        if not line_items:
            raise Exception('Target not found')
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=DOMAIN + "/success/",
            cancel_url=DOMAIN + "/cancel/",
        )
        return JsonResponse({
            'id': checkout_session.id
        })


def get_order(request, pk):
    order = Order.objects.get(id=pk)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'index.html', context)


def select_target(target, self):
    if target == 'order':
        order = get_object_or_404(Order, pk=self.kwargs["pk"])
        line_items = [
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(order_item.items_price) * 100,
                    "product_data": {
                        "name": order_item.item.name,
                        "description": order_item.item.description,
                    },
                },
                "quantity": 1,
            } for order_item in order.order_items.all()
        ]
    elif target == 'item':
        item = Item.objects.get(id=self.kwargs["pk"])
        line_items = [
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(item.price) * 100,
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                },
                "quantity": 1,
            }
        ]
    else:
        line_items = []
    return line_items
