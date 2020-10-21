"""Vehicles Routing Problem (VRP) with Time Windows."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['time_matrix'] = [
        [0, 5, 9, 3, 10, 6, 8, 7, 5, 1, 10, 6, 2, 6, 2, 5, 5, 6, 8, 3, 7, 6, 7, 9, 8, 8],
        [5, 0, 2, 2, 4, 8, 7, 8, 5, 9, 2, 4, 1, 7, 3, 4, 6, 2, 6, 9, 3, 8, 6, 9, 6, 3],
        [9, 2, 0, 2, 6, 7, 9, 8, 9, 1, 4, 6, 5, 3, 1, 9, 4, 4, 2, 10, 9, 3, 4, 4, 5, 10],
        [3, 2, 2, 0, 5, 1, 6, 7, 2, 5, 4, 8, 10, 1, 9, 8, 2, 10, 2, 9, 4, 8, 8, 6, 8, 9],
        [10, 4, 6, 5, 0, 7, 6, 1, 1, 6, 7, 7, 5, 1, 3, 9, 5, 6, 4, 10, 2, 7, 5, 3, 6, 3],
        [6, 8, 7, 1, 7, 0, 2, 1, 9, 2, 5, 5, 10, 10, 4, 5, 5, 7, 2, 5, 1, 7, 3, 8, 1, 7],
        [8, 7, 9, 6, 6, 2, 0, 9, 10, 9, 1, 4, 9, 9, 10, 8, 4, 2, 8, 2, 4, 5, 5, 3, 2, 10],
        [7, 8, 8, 7, 1, 1, 9, 0, 5, 2, 3, 9, 1, 1, 6, 6, 6, 1, 4, 8, 7, 5, 7, 5, 2, 5],
        [5, 5, 9, 2, 1, 9, 10, 5, 0, 9, 3, 9, 9, 9, 3, 9, 5, 8, 10, 5, 4, 8, 8, 10, 10],
        [1, 9, 1, 5, 6, 2, 9, 2, 9, 0, 2, 1, 9, 7, 8, 7, 8, 7, 7, 5, 5, 9, 5, 5, 8, 3],
        [10, 2, 4, 4, 7, 5, 1, 3, 3, 2, 0, 9, 1, 9, 1, 1, 10, 2, 4, 2, 8, 6, 7, 9, 3, 6],
        [6, 4, 6, 8, 7, 5, 4, 9, 9, 1, 9, 0, 2, 5, 7, 4, 10, 9, 4, 2, 10, 7, 9, 2, 5, 4],
        [2, 1, 5, 10, 5, 10, 9, 1, 9, 9, 1, 2, 0, 7, 7, 8, 5, 4, 9, 4, 9, 5, 1, 1, 8, 2],
        [6, 7, 3, 1, 1, 10, 9, 1, 9, 7, 9, 5, 7, 0, 3, 6, 7, 6, 6, 5, 5, 2, 8, 6, 3, 9],
        [2, 3, 1, 9, 3, 4, 10, 6, 3, 8, 1, 7, 7, 3, 0, 6, 1, 8, 9, 4, 3, 5, 10, 1, 8, 1],
        [5, 4, 9, 8, 9, 5, 8, 6, 9, 7, 1, 4, 8, 6, 6, 0, 8, 8, 2, 3, 1, 3, 5, 8, 2, 8],
        [5, 6, 4, 2, 5, 5, 4, 6, 5, 8, 10, 10, 5, 7, 1, 8, 0, 6, 10, 10, 7, 6, 3, 9, 3, 1],
        [6, 2, 4, 10, 6, 7, 2, 1, 8, 7, 2, 9, 4, 6, 8, 8, 6, 0, 2, 5, 7, 9, 7, 8, 9, 1],
        [8, 6, 2, 2, 4, 2, 8, 4, 10, 7, 4, 4, 9, 6, 9, 2, 10, 2, 0, 9, 7, 8, 7, 2, 8, 6],
        [3, 9, 10, 9, 10, 5, 2, 8, 5, 5, 2, 2, 4, 5, 4, 3, 10, 5, 9, 0, 3, 5, 5, 8, 7, 4],
        [7, 3, 9, 4, 2, 1, 4, 7, 4, 5, 8, 10, 9, 5, 3, 1, 7, 7, 7, 3, 0, 7, 8, 9, 1, 1],
        [6, 8, 3, 8, 7, 7, 5, 5, 8, 9, 6, 7, 5, 2, 5, 3, 6, 9, 8, 5, 7, 0, 1, 1, 9, 9],
        [7, 6, 4, 8, 5, 3, 5, 7, 8, 5, 7, 9, 1, 8, 10, 5, 3, 7, 7, 5, 8, 1, 0, 8, 7, 9],
        [9, 9, 4, 6, 3, 8, 3, 5, 10, 5, 9, 2, 1, 6, 1, 8, 9, 8, 2, 8, 9, 1, 8, 0, 7, 2],
        [8, 6, 5, 8, 6, 1, 2, 2, 10, 8, 3, 5, 8, 3, 8, 2, 3, 9, 8, 7, 1, 9, 7, 7, 0, 3],
        [8, 3, 10, 9, 3, 7, 10, 5, 2, 3, 6, 4, 2, 9, 1, 8, 1, 1, 6, 4, 1, 9, 9, 2, 3, 0],
    ]
    data['time_windows'] = [
        (5, 12),  # depot
        (8, 19),  # 1
        (3, 12),  # 2
        (11, 19),  # 3
        (16, 18),  # 4
        (8, 20),  # 5
        (5, 9),  # 6
        (6, 16),  # 7
        (2, 4),  # 8
        (17, 20),  # 9
        (2, 17),  # 10
        (4, 17),  # 11
        (5, 19),  # 12
        (15, 17),  # 13
        (14, 18),  # 14
        (1, 8),  # 15
        (5, 12),  # 16
        (2, 13),  # 17
        (0, 2),  # 18
        (9, 12),  # 19
        (8, 18),  # 20
        (12, 19),   #21
        (6, 8),  # 22
        (17, 20),  # 23
        (10, 12), #24        
    ]
    data['num_vehicles'] = 3
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            plan_output += '{0} Time({1},{2}) -> '.format(
                manager.IndexToNode(index), solution.Min(time_var),
                solution.Max(time_var))
            index = solution.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        plan_output += '{0} Time({1},{2})\n'.format(manager.IndexToNode(index),
                                                    solution.Min(time_var),
                                                    solution.Max(time_var))
        plan_output += 'Time of the route: {}min\n'.format(
            solution.Min(time_var))
        print(plan_output)
        total_time += solution.Min(time_var)
    print('Total time of all routes: {}min'.format(total_time))


def main():
    """Solve the VRP with time windows."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['time_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def time_callback(from_index, to_index):
        """Returns the travel time between the two nodes."""
        # Convert from routing variable Index to time matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['time_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Time Windows constraint.
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        30,  # allow waiting time
        30,  # maximum time per vehicle
        False,  # Don't force start cumul to zero.
        time)
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot.
    for location_idx, time_window in enumerate(data['time_windows']):
        if location_idx == 0:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
    # Add time window constraints for each vehicle start node.
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(data['time_windows'][0][0],
                                                data['time_windows'][0][1])

    # Instantiate route start and end times to produce feasible times.
    for i in range(data['num_vehicles']):
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.End(i)))

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)


if __name__ == '__main__':
    main()
