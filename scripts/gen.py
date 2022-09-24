import array
import os
import sys

try:
    binary_path, template_path, show_original = sys.argv[1:]
except ValueError:
    print(f"Usage: {sys.argv[0]} binary_path template_path show_original", file=sys.stderr)
    sys.exit(1)

code = bytearray((os.path.getsize(binary_path) + 7) // 8 * 8)
with open(binary_path, "rb") as f:
    f.readinto(code)

arr = array.array('Q')
arr.frombytes(code)
r = ",".join(min(str(i), hex(i), key=len) for i in arr)

source_path = "src/solution.rs"
show_original = int(show_original)

with open(template_path) as f:
    template = f.read().rstrip()
if show_original:
    sys.stdout.write("// Generated with basm-rs: https://github.com/kiwiyou/basm-rs")
    with open(source_path, 'r') as g:
        for line in g.readlines():
            sys.stdout.write("//" , line)
    sys.stdout.write("\n//\n" )
    
print(template % {"len": len(arr), "text": r})
