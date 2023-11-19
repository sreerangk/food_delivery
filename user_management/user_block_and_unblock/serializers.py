from rest_framework import serializers


class UserBlockSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

class UserUnblockSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
