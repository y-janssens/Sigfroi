from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from .models import Snapshot
# import os
# from django.db.models.signals import post_delete


# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     # if instance.file:
#     snap = instance
#     if os.path.isfile(snap.file.path):
#         os.remove(snap.file.path)


# post_delete.connect(auto_delete_file_on_delete, sender=Snapshot)

# Receive the pre_delete signal and delete the file associated with the model instance.


# @receiver(pre_delete, sender=Snapshot)
# def mymodel_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     print(instance.file.path)
#     instance.file.delete(False)
