# Animal shelter
implementing animal shelter using queue, that could contain cats or dogs , and should implement enqueue and dequeue methods to animal shelter class

## Whiteboard Process
**enqueue :**
![algo (16)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/9423fa44-1cfa-4ecb-ba8f-2670a961b350)


**dequeue :**
![algo (17)](https://github.com/11mones/data-structures-and-algorithms/assets/72322641/e63e4059-a212-43f0-8483-ff2a78dc9f4e)


## Approach & Efficiency
my functions works correctly and do what is meant to do and restore the original queue to its state

## Solution
algorithm : first initialize the AnimalShelter class:
Create an empty queue called shelter,implement the enqueue method and no problem with it same as normal enqueue implement the dequeue method that takes a preference
pref as an argument (either "dog" or "cat") and create an empty temporary queue called temp_queue. then we iterate while the shelter queue is not empty: dequeue an
item from the shelter queue and enqueue it to temp_queue and if the species of the back element in temp_queue matches the preference pref return the data (animal)
of the back element in temp_queue.
and to restore the original shelter queue we iterate while temp_queue is not empty dequeue an item from temp_queue and enqueue it back to the shelter queue.