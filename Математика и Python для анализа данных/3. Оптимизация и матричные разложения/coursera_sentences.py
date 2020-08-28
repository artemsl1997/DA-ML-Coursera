import re
import numpy as np

with open('sentences.txt', 'r') as file:
	lines = []
	for line in file.readlines():
		lines.append(line.lower().strip())
#print(lines)

new_lines = []
for line in lines:
	new_line = re.split('[^a-z]', line)
	new_lines.append(new_line)
#print(new_lines)

new_lines = [[value for value in line if value != ''] for line in new_lines]
final_lines = []
for line in new_lines:
	for value in line:
		if value in final_lines:
			continue
		final_lines.append(value)
#print(final_lines)

import collections
res_dict = {}
counter = 0
for i in final_lines:
	res_dict[(counter, i)] = []
	for line in new_lines:
		if i in line:
			l = line.count(i)
			res_dict[(counter, i)] += [l]
		else:
			res_dict[(counter, i)] += [0]
	counter += 1
print(res_dict)

l = []
for value in res_dict.values():
	l.append(value)
arr = np.array(l)
print(arr.shape)


from scipy.spatial import distance
result = []
for i in range(len(arr[0])):
	result.append((i, distance.cosine(arr[:, 0], arr[:, i])))
result.sort(key=lambda x: x[1])
print(result)

final_line = str(result[1][1]) + ' ' + str(result[2][1])
with open('submission-1.txt', 'w') as final:
	final.write(final_line)