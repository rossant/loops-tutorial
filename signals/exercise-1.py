import numpy as np
from vispy import app
from vispy import gloo

vertex = """
attribute float x;
attribute float y;
void main (void)
{
    gl_Position = vec4(x, y, 0.0, 1.0);
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

    def on_resize(self, event):
        gloo.set_viewport(0, 0, event.size[0], event.size[1])

    def on_draw(self, event):
        gloo.clear((1,1,1,1))
        self.program.draw('line_strip')

window = Window(n=1000)
window.show()
app.run()
