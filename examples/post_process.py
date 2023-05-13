# Require: Avg Apogee (ft), Min Stability, Avg Stability at Apogee, Max Stability, Max Velocity
# Input: Timestamp, Altitude, Total Acceleration, Total Velocity, Stability, Pressure
import math

apogees = []
apogee_stability = []
max_velocities = []
init_stabilities = []

min_stability = 10
max_stability = 0

with open('raw_output1a_4', 'r') as dataFile:
    lines = dataFile.readlines()
    for line in lines:
        if "Number" in line:
            offset = 0
            velocity = []
            stability = []
            altitude = []
            continue
        if "INFO" in line or "DEBUG" in line or "Cond" in line:
            continue
        if "End" in line:
            apogees.append(max(altitude))
            apogee_index = altitude.index(max(altitude))
            apogee_stability.append(stability[apogee_index - offset])
            max_velocities.append(max(velocity))

            if max(stability) > max_stability:
                max_stability = max(stability)
            #print(sorted(stability[0:apogee_index - 40 - offset])[0:10])
            init_stabilities.append(stability[0])
            if min(stability[0:apogee_index - offset - 200]) < min_stability: # 2 seconds ~= 40 timesteps
                min_stability = min(stability[0:apogee_index - 200 - offset])
            continue
        else:
            lineVal = line.strip().split(",")
            altitude.append(float(lineVal[1]))
            velocity.append(float(lineVal[3]))
            if lineVal[4] == " NC":
                offset += 1
            elif lineVal[4] != " NA":
                stability.append(float(lineVal[4]))

print(sum(apogees)/len(apogees))
print(min_stability)
print(sum(apogee_stability)/len(apogee_stability))
print(max_stability)
print(sum(max_velocities)/len(max_velocities))
init_stabilities = sorted(init_stabilities)
case_lessThan = 0
for i in init_stabilities:
    if i < 1.5:
        case_lessThan += 1
    else:
        break
print(case_lessThan / len(init_stabilities))
print(sum(init_stabilities) / len(init_stabilities))
#print(sorted(init_stabilities))
