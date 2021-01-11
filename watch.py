from subprocess import Popen

import time


N_LOOP = 100

handles = []
for i in range(N_LOOP):
	
	print(i)

	h = Popen(["pipenv", "run", "python", "a.py"])

	handles.append(h)

	time.sleep(4.1)


print("wait for fin")
while len(handles) > 0:
	for proc in handles:
		
		retcode = proc.poll()

		if retcode is not None:
			handles.remove(proc)

		else:
			time.sleep(0.1)


print("fin")