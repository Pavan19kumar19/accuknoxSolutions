# AccuknoxSolutions
# Django Solution Project

## Topic : Django Signals

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
    print("Signal handler completed")
```
**Output:**
![1](https://github.com/user-attachments/assets/1b8d6234-322b-48c8-b828-ef4182dd3ce6)


### 2. Do django signals run in the same thread as the caller?

Yes, Django signals run in the same thread as the caller. The handlers for the signal are executed in the same thread that triggered the signal. This behavior ensures that any thread-specific context or state is preserved when the signal is processed.

**Example Code:**

In the Django `signals.py` file:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rectangular

@receiver(post_save,sender=Rectangular)
def rectangular_saved_handler(sender,instance,**kwargs):
    print(f"Signal received for Rectangular with length={instance.length} and width={instance.width}")
    print(f"Signal handler thread: {threading.current_thread().name}")
```
**Output:**
![2](https://github.com/user-attachments/assets/f5bd11d0-0caa-47cc-92c9-de124dbfe644)

### 3. Do Django signals run in the same database transaction as the caller?

By default, Django signals run **within the same database transaction** as the caller. This means that if a signal is triggered as part of a database transaction, the signal handlers execute within that same transaction. This ensures that any changes made by the signal handlers are part of the same transaction, maintaining transactional integrity.

**Example Code:**

In the Django `signals.py` file:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rectangular

@receiver(post_save,sender=Rectangular)
def rectangular_saved_handler(sender,instance,**kwargs):
    print(f"Signal received for Rectangular with length={instance.length} and width={instance.width}")
    raise Exception("Forcing a rollback to test transaction handling")
```
**Output:**
![3](https://github.com/user-attachments/assets/029e9580-fdbf-43cc-8de5-cefd67587d85)

## Topic : Custom Classes in Python
### 1 Initialize the class with length and width attributes
```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
```
### 2 Implement an iterator so that instances of the Rectangle class can be iterated over.
```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define an iterator method to make the instance iterable
    def __iter__(self):
        # Yield length first
        yield {'length': self.length}
        # Yield width second
        yield {'width': self.width}
```
### 3 Define the iteration behavior to return a dictionary with the length first and then the width.
```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield length first
        yield {'length': self.length}
        # Yield width second
        yield {'width': self.width}

# Example usage
rect = Rectangle(10, 5)

# Iterating over the Rectangle instance
for dim in rect:
    print(dim)
```
![Screenshot 2024-09-13 163527](https://github.com/user-attachments/assets/1bebf550-cc9a-498a-982c-ce47bc63102b)


# Key Highlights of My Approach

This solution demonstrates a deep understanding of Django's behavior in key areas such as signal handling, threading, and transaction management. By addressing how Django signals work synchronously, in the same thread, and within the same database transaction, I provide clear and practical solutions to common framework challenges. This approach highlights my ability to analyze, break down complex topics, and offer precise, reliable solutions, all essential skills for developing robust applications.

---

<h2 align="center">Thank You!</h2>
