from rest_framework import viewsets

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    """Full CRUD for the authenticated user's subscriptions.

    • The queryset is always filtered to ``request.user``, so a user can
      never see, modify, or delete another user's subscriptions.
    • On create, the user is auto-assigned from the JWT — the client
      never sends a ``user`` field.
    • Attempting to access another user's subscription by id returns 404
      (not 403), so existence of other users' data is never leaked.
    """

    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
