import json
from .models import helps_received
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from channels.generic.websocket import WebsocketConsumer

instances = []

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        global instances

        instances.append(self)

        self.send(json.dumps({'message': helps_received.get_all_objects(helps_received)}))

    def disconnect(self, close_code):

        global instances

        instances.remove(self)

        self.close()


@receiver(post_save, sender=helps_received)
@receiver(post_delete, sender=helps_received)
def get_model_objects(sender, **kwargs):
    print(helps_received.get_all_objects(helps_received))

    for instance in instances:
        instance.send(json.dumps({'message': helps_received.get_all_objects(helps_received)}))
