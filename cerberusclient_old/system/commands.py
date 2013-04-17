from system.models import Message
from django.utils import timezone
def sendSystemMessage(content=None, timestamp=timezone.now(), seen=False):
	m = Message(content=content, timestamp=timestamp, seen=seen)
	m.save()
