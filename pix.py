import sys
from PIL import Image

grays = '@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,"^.`    '
gs = len(grays)

print(sys.argv[1])
img = Image.open(sys.argv[1]).convert("L")
px = img.load()

w = img.width
h = img.height

for y in range(0, h, 2):
    for x in range(w):
        idx = px[x, y] * gs // 255
        if idx == gs:
            idx = gs - 1
        sys.stdout.write(grays[idx])
    sys.stdout.write("\n")
    sys.stdout.flush()
