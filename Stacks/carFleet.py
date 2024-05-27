def carFleet(target: int, position: list[int], speed: list[int]) -> int: 
    """
    There are n cars going to the same destination along a one-lane road. The destination is target miles away.

    You are given two integer array position and speed, both of length n, where position[i] is the position of 
    the ith car and speed[i] is the speed of the ith car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the 
    same speed. The faster car will slow down to match the slower car's speed. The distance between these two 
    cars is ignored (i.e., they are assumed to have the same position).

    A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single 
    car is also a car fleet.

    If a car catches up to a car fleet right at the destination point, it will still be considered as one car 
    fleet.

    Return the number of car fleets that will arrive at the destination.      
    """
    # Create a list of tuples that contains the position and speed of each car
    cars = [(position[i], speed[i]) for i in range(len(position))]

    # Create a variable that will hold the amount of time it takes to reach the destination
    totalTime = 0
    fleets = 0

    for pos, speed in sorted(cars, reverse=True): 
        # Compute the time it takes for the curr car to reach the destination
        currTime = (target - pos) / speed 

        # If the time is less than the total time, the number of fleets can be incremented
        if currTime > totalTime: 
            fleets += 1
            totalTime = currTime
    
    return fleets

print("Result:", carFleet(100, [4, 0, 2], [1, 4, 2]))