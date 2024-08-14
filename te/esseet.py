# Define the range boundaries
start = 0
end = 10

# Iterate over the range, excluding the first and last indices
for i in range(start + 1, end - 1):
    print(f'Index: {i}, Left Neighbor: {i - 1}, Right Neighbor: {i + 1}')
