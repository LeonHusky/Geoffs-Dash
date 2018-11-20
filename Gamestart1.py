#top
import pyxel
class App:
    pyxel.init(255, 255)
    
    
    def update():
        if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw():
        pyxel.cls(0)
        pyxel.rect(10, 10, 20, 20, 11)

App()
