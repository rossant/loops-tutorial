import numpy as np
from vispy import app
from vispy import gloo

vertex = """
attribute float x;
attribute float y;
attribute float i;
void main (void)
{
    gl_Position = vec4(x, 1.0 - 1.0/10.0- i/5.0 +y, 0.0, 1.0);
}
"""

fragment = """
void main()
{
    gl_FragColor = vec4(0.0,0.0,0.0,1.0);
}
"""

class Window(app.Canvas):
    def __init__(self, n=50):
        app.Canvas.__init__(self)
        self.program = gloo.Program(vertex, fragment)
        self.data = np.zeros((10,n), [('x', np.float32, 1),
                                      ('y', np.float32, 1),
                                      ('i', np.float32, 1)])

        self.data['x'] = np.linspace(-1.0, +1.0, n)
        self.data['y'] = np.random.uniform(-0.1, +0.1, (10,n))
        self.data['i'] = np.repeat(np.arange(10),n).reshape(10,n)

        self.vdata = gloo.VertexBuffer(self.data)
        self.program.bind(self.vdata)


    def on_resize(self, event):
        gloo.set_viewport(0, 0, event.size[0], event.size[1])

    def on_draw(self, event):
        gloo.clear((1,1,1,1))
        self.program.draw('line_strip')



window = Window(n=256)
window.show()
app.run()
