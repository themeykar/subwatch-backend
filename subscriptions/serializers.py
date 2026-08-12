from rest_framework import serializers

from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for the Subscription model.

    • ``user`` is read-only and auto-assigned from the JWT in the view,
      so it never appears in request input.
    • ``cost`` is validated to be a positive number.
    """

    class Meta:
        model = Subscription
        fields = (
            "id",
            "name",
            "cost",
            "billing_cycle",
            "next_renewal_date",
            "category",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Cost must be a positive number."
            )
        return value
