'''
INSERT YOUR CODE HERE
'''

with open('input.txt') as input_file:
    number_vertexes = int(input_file.readline())
    adjacency = []

    for vertex in range(number_vertexes):
        line = input_file.readline().split()
        adjacency.append([int(edge) for edge in line])

    vertexes = input_file.readline().split()
    first = int(vertexes[0]) - 1
    second = int(vertexes[1]) - 1

distances = [-1 for i in range(number_vertexes)

'''
INSERT YOUR CODE HERE
'''

output_file = open('output.txt', 'w')
output_file.write(str(distance[second]) + '\n')
output_file.close()
