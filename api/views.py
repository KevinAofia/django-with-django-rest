from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from djangorestapp.models import User

@api_view(['GET'])
def get_users(request):
    users = serializers.UserSerializer(User.objects.all(), many=True)
    return Response(users.data)

@api_view(['POST'])
def post_user(request):
    user = serializers.UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
    return Response(user.data)

@api_view(['PUT'])
def update_user(request,id):
    user = User.objects.get(id=id)
    updated_user = serializers.UserSerializer(user, data=request.data)
    if updated_user.is_valid():
        updated_user.save()
    return Response(updated_user.data)

@api_view(['DELETE'])
def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return Response() # DEFAULTS TO 200


