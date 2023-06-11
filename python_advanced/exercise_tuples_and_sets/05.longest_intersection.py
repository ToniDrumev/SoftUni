longest_intersection_length = 0
longest_intersection_numbers = set()


for _ in range(int(input())):
    range_edges = input().split("-")
    first_range_edges = [int(x) for x in range_edges[0].split(",")]
    second_range_edges = [int(x) for x in range_edges[1].split(",")]

    first_range = set(range(first_range_edges[0], first_range_edges[1] + 1))
    second_range = set(range(second_range_edges[0], second_range_edges[1] + 1))

    current_intersection_length = len(first_range & second_range)

    if current_intersection_length > longest_intersection_length:
        longest_intersection_length = current_intersection_length
        longest_intersection_numbers = sorted(first_range & second_range)

print(f'Longest intersection is {longest_intersection_numbers} with length {longest_intersection_length}')
