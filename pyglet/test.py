import pyglet
from pyglet import gl
 
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200  # v pixelech za sekundu
RYCHLOST_PALKY = RYCHLOST * 1.5  # taky v pixelech za sekundu

DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 30

def nakresli_obdelnik(x1, y1, x2, y2):
 gl.glBegin(gl.GL_TRIANGLE_FAN) # zacni kreslit spojene trojuhelniky
 gl.glVertex2f(int(x1), int(y1)) # vrchol A
 gl.glVertex2f(int(x1), int(y2)) # vrchol B
 gl.glVertex2f(int(x2), int(y2)) # vrchol C, nakresli trojuhelnik ABC
 gl.glVertex2f(int(x2), int(y1)) # vrchol D, nakresli trojuhelnik BCD
 # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
 gl.glEnd() # ukonci kresleni trojuhelniku
 
def vykresli():
 gl.glClear(gl.GL_COLOR_BUFFER_BIT) # smaz obsah okna (vybarvi na cerno)
 nakresli_obdelnik(1,2,56,152)
 
window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
 on_draw=vykresli, # na vykresleni okna pouzij funkci `vykresli`
)
pyglet.app.run()