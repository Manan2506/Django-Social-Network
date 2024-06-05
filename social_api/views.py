
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import FriendRequest
from .serializers import FriendRequestSerializer, UserSerializer

CustomUser = get_user_model()


class FriendRequestThrottle(UserRateThrottle):
    rate = '3/minute'


class SendFriendRequestView(generics.CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestThrottle]

    def perform_create(self, serializer):
        sender = self.request.user
        receiver = CustomUser.objects.get(id=self.request.data['receiver_id'])

        if FriendRequest.objects.filter(sender=sender, receiver=receiver, status='pending').exists():
            raise serializers.ValidationError("Friend request already sent.")

        serializer.save(sender=sender, receiver=receiver, status='pending')


class AcceptFriendRequestView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.receiver != request.user:
            return Response({"detail": "Not allowed."}, status=status.HTTP_403_FORBIDDEN)

        if instance.status == 'accepted':
            return Response({"detail": "Friend request already accepted."}, status=status.HTTP_400_BAD_REQUEST)

        if instance.status == 'rejected':
            return Response({"detail": "Friend request already rejected."}, status=status.HTTP_400_BAD_REQUEST)

        instance.status = 'accepted'
        instance.save(update_fields=['status'])

        return Response({"detail": "Friend request accepted."}, status=status.HTTP_200_OK)


class RejectFriendRequestView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.receiver != request.user:
            return Response({"detail": "Not allowed."}, status=status.HTTP_403_FORBIDDEN)

        if instance.status == 'accepted':
            return Response({"detail": "Friend request already accepted."}, status=status.HTTP_400_BAD_REQUEST)

        if instance.status == 'rejected':
            return Response({"detail": "Friend request already rejected."}, status=status.HTTP_400_BAD_REQUEST)

        instance.status = 'rejected'
        instance.save(update_fields=['status'])

        return Response({"detail": "Friend request rejected."}, status=status.HTTP_200_OK)


class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = CustomUser.objects.filter(
            Q(sent_requests__receiver=user, sent_requests__status='accepted') |
            Q(received_requests__sender=user, received_requests__status='accepted')
        ).distinct()
        return friends


class ListPendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(receiver=user, status='pending')
