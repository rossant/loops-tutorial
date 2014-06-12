import numpy as np
from vispy import app
from vispy import gloo

vertex = """
attribute float x;
attribute float y;
uniform float d;
void main (void)
{
    gl_Position = vec4(d*x, y, 0.0, 1.0);
}
"""

fragment = """
void main()
{
    gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
}
"""

class Window(app.Canvas):
    def __init__(self, n=50):
        app.Canvas.__init__(self)
        self.program = gloo.Program(vertex, fragment, n)
        self.program['x'] = np.linspace(-1.0, +1.0, n)
        self.program['y'] = np.random.uniform(-0.5, +0.5, n)
        self.d = 1.
        self.program['d'] = self.d

    def on_resize(self, event):
        gloo.set_viewport(0, 0, event.size[0], event.size[1])

    def on_mouse_wheel(self, event):
        self.d += event.delta[1]*.25
        self.program['d'] = self.d
        self.update()
        
    def on_draw(self, event):
        gloo.clear((1,1,1,1))
        self.program.draw('line_strip')

window = Window(n=1000)
window.show()
app.run()
