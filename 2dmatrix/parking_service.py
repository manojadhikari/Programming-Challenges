'''
/**
 * I own a parking garage that provides valet parking service.
 * When a customer pulls up to the entrance they are either rejected
 * because the garage is full, or they are given a ticket they can
 * use to collect their car, and the car is parked for them.
 *
 * Given a set of different parking bays (Small, Medium, Large),
 * write a control program to accept/reject cars (also small, medium or large)
 * as they arrive, and issue/redeem tickets.
 *
 * Garage layout is 1 small bay, 1 medium bay, and 2 large bays: [1,1,2]
 *
 * First sequence Actions:
 * [(arrival, small),
 * (arrival, large),
 * (arrival, medium),
 * (arrival, large),
 * (arrival, medium)]
 *
 * Expected output: [1, 2, 3, 4, reject]
 *
 * Second sequence Actions:
 * [(arrival, small),
 * (arrival, large),
 * (arrival, medium),
 * (arrival, large),
 * (depart, 3),
 * (arrival, medium)]
 *
 * Expected output: [1, 2, 3, 4, 5]

 count = 5
 result: [1,2,3,4,5]
 my_map: {1: small, 2: large, 4:large, 5:medium}
 layout:{small: 0, medium: 0, large: 0}

Algorithm:
count = 1
layout = {small: 1, medium: 1, large: 2}
result = []
my_map = {}
traverse through the instruction array and for each instruction:
    if arrival:
        check if limit == 0 in layout
        if 0:
            append reject to result
            continue
        else:
            append count to result
            decrease limit on layout
            add count: cartype to dictionary

    if depart:
        check if depart index in range <= len(result):
        if yes,
            check that result[index-1] is not reject:

            if not reject:
                if my_map has the value at index, my_map.get(index)
                if still in dictionary:
                    remove it from dictionary
                    increase the limit in layout for value at index

    increase count
 '''
def parking_service_status(instructions):
    count = 1
    layout = {'small': 1, 'medium': 1, 'large': 2}
    result = []
    my_map = {}

    for instruction in instructions:
        action, car = instruction
        if action == 'arrival':
            if layout[car] == 0:
                result.append('reject')
            else:
                result.append(count)
                layout[car] -= 1
                my_map[count] = car
                count += 1

        elif action == 'depart':
            index = car
            if index <= len(result):
                if result[index - 1] != 'reject':

                    if my_map.get(index):
                        layout[my_map[index]] += 1
                        del(my_map[index])

    return result

arrival = 'arrival'
depart = 'depart'
small = 'small'
large = 'large'
medium = 'medium'
print(parking_service_status([(arrival, small),(arrival, large),(arrival, medium),(arrival, large),(arrival, medium)]))
print(parking_service_status([(arrival, small),(arrival, large),(arrival, medium),(arrival, large),(depart, 3),(arrival, medium)]))
