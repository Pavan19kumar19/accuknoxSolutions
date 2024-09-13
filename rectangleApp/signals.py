import threading
import time

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rectangular


##Question 1 
# @receiver(post_save,sender = Rectangular)
# def rectangular_saved_handler(sender,instance,**kwargs):
#     print(f"Signal received for Rectangular with length={instance.length} and width={instance.width}")
#     print(f"Signal handler thread: {threading.current_thread().name}")
#     time.sleep(5)  # Simulate synchronous behavior
#     print("Delay 5 seconds")
#     print("Signal handler completed")
    
##Question 2
# @receiver(post_save,sender=Rectangular)
# def rectangular_saved_handler(sender,instance,**kwargs):
#     print(f"Signal received for Rectangular with length={instance.length} and width={instance.width}")
#     print(f"Signal handler thread: {threading.current_thread().name}")


#Question 3
@receiver(post_save,sender=Rectangular)
def rectangular_saved_handler(sender,instance,**kwargs):
    print(f"Signal received for Rectangular with length={instance.length} and width={instance.width}")
    raise Exception("Forcing a rollback to test transaction handling")