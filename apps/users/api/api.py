from rest_framework.views import APIView
from apps.users.api.serializers import UserProfileSerializer
from apps.users.models import UserProfile
from rest_framework.response import Response

class UserAPIView(APIView):

    def get(self, request):
        users = UserProfile.objects.all()
        users_serializer = UserProfileSerializer(users, many=True)
        return Response(users_serializer.data)