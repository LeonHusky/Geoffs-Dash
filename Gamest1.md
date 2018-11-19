```python
import pyxel
from airbrake import *

print("this is a test")
pyxel.init(255, 255)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)
```
#For github: dont copy over the backticks they are for the syntax highlighting in github (bc that will cause an error on run)
