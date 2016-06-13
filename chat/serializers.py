from swampdragon.serializers.model_serializer import ModelSerializer


class ChatSerializer(ModelSerializer):

    class Meta:
        model = 'chat.Chat'
        publish_fields = ('title', 'users')
        update_fields = ()

    def serialize_users(self, obj):
        return [{'uid': user.id, 'username': user.username, 'userpic': str(user.userpic)} for user in obj.users.all()]


class MessageSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Message'
        publish_fields = ('text', 'created_at', 'author')
        update_fields = ()

    def serialize_author(self, obj):
        return {'uid': obj.author.id, 'username': obj.author.username, 'userpic': str(obj.author.userpic)}


class CustomUserSerializer(ModelSerializer):
    chat = ChatSerializer

    class Meta:
        model = 'conf_app.CustomUser'
        publish_fields = ('id', 'username', 'userpic')
        update_fields = ()
