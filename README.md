# garden-manager


## Event-Driven System

### Principle: 
Producers emit events; consumers subscribe and react.

### Data 
**Plant** = producer (emits “wilting” events)
**Garden** = consumer (reacts by watering)
Events decouple the two: Garden doesn’t poll; it reacts.


