import os
ls = os.listdir('data')
ls.remove('.gitkeep')
for i in ls:
	os.remove(str('./data/' + i))
