# AccuknoxSolutions
# Django Solution Project

## Overview

This project demonstrates the use of Django signals, custom Django models, and Python class iteration. The project contains a Django app named `solution` with a model called `Rectangular`. It also includes explanations and code examples related to Django signals.

## Django Signals

### 1. Are Django signals executed synchronously or asynchronously by default?

By default, Django signals are executed **synchronously**. This means that when a signal is sent, the signal handlers are executed in the same thread and process as the sender. 

**Example Code:**

In the Django `signals.py` file:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rectangular

@receiver(post_save,sender = Rectangular)
def rectangular_saved_handler(sender,instance,**kwargs):
    print(f"Signal received for Rectangular with length={instance.length} and width={instance.width}")
    print(f"Signal handler thread: {threading.current_thread().name}")
    time.sleep(5)  # Simulate synchronous behavior
    print("Delay 5 seconds")
    print("Signal handler completed")```

### 2. Do django signals run in the same thread as the caller?
