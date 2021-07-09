import re
import sys
import io
import zipfile 

with io.BytesIO(bytes.fromhex(sys.stdin.read())) as f:
	f = zipfile.ZipFile(f)
	s = f.infolist()

cur, vol = 0,0
find = re.compile(r"\sfile_size=(\d+)")
for i in s:
    tmp = str(i)
    tmp = find.search(tmp)
    if tmp:
        cur += 1
        vol += int(tmp.group(1))

print(cur, vol)