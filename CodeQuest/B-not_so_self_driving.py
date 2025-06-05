import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    speed, obs_dist = sys.stdin.readline().rstrip().split(":")
    speed = float(speed)
    obs_dist = float(obs_dist)

    if speed == 0:
        print("SAFE")
        continue

    if obs_dist / speed <= 1:
        print("SWERVE")
    elif obs_dist / speed <= 5:
        print("BRAKE")
    else:
        print("SAFE")
