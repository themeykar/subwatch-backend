from django.contrib import admin

from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "cost", "billing_cycle", "next_renewal_date", "category")
    list_filter = ("billing_cycle", "category")
    search_fields = ("name", "user__email")
    date_hierarchy = "next_renewal_date"
