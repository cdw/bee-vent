# Even bees gotta follow rules

## Stationary flappers
 - stand there
 - move left or right when nudged

## Wandering bees
 - walk towards the hive entrance
 - if there is an obstacle in the way, route goal to left or right (whichever is closer)
 - heading is subject to normal distributed fluctuation around the goal
 - move forward a bit (normal distributed) on each time-step

## Scale of the system
 - 1 pixel is 1 mm. The unit of movement described in bee.py or porch.py is a pixel/a mm.
