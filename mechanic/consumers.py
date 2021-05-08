import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import need_help
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from channels.generic.websocket import WebsocketConsumer

instances = []

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        global instances

        instances.append(self)

        self.send(json.dumps({'message': need_help.get_all_objects(need_help)}, sort_keys=True, indent=1, cls=DjangoJSONEncoder))

    def disconnect(self, close_code):

        global instances

        instances.remove(self)

        self.close()


@receiver(post_save, sender=need_help)
@receiver(post_delete, sender=need_help)
def get_model_objects(sender, **kwargs):
    print(need_help.get_all_objects(need_help))

    for instance in instances:
        instance.send(json.dumps({'message': need_help.get_all_objects(need_help)}))