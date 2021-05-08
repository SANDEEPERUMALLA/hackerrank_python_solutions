from collections import deque

n = int(input())

while n > 0:
    size = int(input())
    cube_lengths = deque(list(map(int, input().split())))
    n -= 1
    max_l = 0
    if cube_lengths[0] > cube_lengths[-1]:
        max_l = cube_lengths[0]
        max = cube_lengths.popleft()
    else:
        max_l = cube_lengths[-1]
        max = cube_lengths.pop()

    isPossible = 'Yes'
    for i in range(0, len(cube_lengths)):
        if cube_lengths[0] <= max_l and cube_lengths[-1] <= max_l:
            if cube_lengths[0] >= cube_lengths[-1]:
                max_l = cube_lengths[0]
                cube_lengths.popleft()
            else:
                max_l = cube_lengths[-1]
                cube_lengths.pop()
        elif cube_lengths[0] <= max_l:
            max_l = cube_lengths[0]
            cube_lengths.popleft()
        elif cube_lengths[-1] <= max_l:
            max_l = cube_lengths[-1]
            cube_lengths.pop()
        else:
            isPossible = 'No'
            break

    print(isPossible)
