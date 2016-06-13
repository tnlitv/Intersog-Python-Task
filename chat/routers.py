from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter, BaseRouter
from swampdragon_notifications.notifier import notify_users
from conf_app.models import CustomUser
from .models import Chat, Message, Notification
from .serializers import ChatSerializer, MessageSerializer, CustomUserSerializer


class ChatRouter(ModelRouter):
    route_name = 'chat'
    valid_verbs = ['chat', 'subscribe', 'get_single', 'get_list']
    serializer_class = ChatSerializer
    model = Chat

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def chat(self, *args, **kwargs):
        errors = {}
        user = self.connection.user
        if 'message' not in kwargs or len(kwargs['message']) is 0:
            errors['message'] = 'Enter a chat message'

        if errors:
            self.send_error(errors)
        else:
            m = Message(
                text=kwargs['message'],
                author=CustomUser.objects.get(id=user.id),
                chat=self.get_object(id=kwargs['chat_id'])
            )
            m.save()
            self.send({'status': 'ok'})
            self.publish(['chat'], {'name': m.author.username, 'message': m.text})


class MessageRouter(ModelRouter):
    route_name = 'message'
    serializer_class = MessageSerializer
    model = Message

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(chat__id=kwargs['chat_id'])


class NotifyRouter(BaseRouter):
    valid_verbs = ['subscribe', 'notify_everyone_but_me']
    route_name = 'notifier'

    def notify_everyone_but_me(self, name):
        users = CustomUser.objects.all()
        # users = CustomUser.objects.exclude(pk=self.connection.user.pk)
        foo = Notification.objects.create(name=name)
        notify_users(users, subject=foo, notification_type='foo')


route_handler.register(NotifyRouter)
route_handler.register(ChatRouter)
route_handler.register(MessageRouter)
