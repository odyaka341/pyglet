#!/usr/bin/env python

'''Testing flat map allow_oob enforcement.

Press arrow keys to move view focal point (red dot) around map.
Press "o" to turn allow_oob on and off.

You should see no black border with allow_oob=False.

Press escape or close the window to finish the test.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import unittest
from render_base import RenderBase
import pyglet.scene2d
from pyglet.scene2d.debug import gen_rect_map

class OOBTest(RenderBase):
    def test_main(self):
        m = gen_rect_map(['a'*10]*10, 32, 32)

        self.init_window(256, 256)
        self.set_map(m)

        def on_text(text):
            if text == 'o':
                self.view.allow_oob = not self.view.allow_oob
                print 'NOTE: allow_oob =', self.view.allow_oob
                return
            return pyglet.window.event.EVENT_UNHANDLED
        print 'NOTE: allow_oob =', self.view.allow_oob

        self.w.push_handlers(on_text)
        self.show_focus()

        self.run_test()
if __name__ == '__main__':
    unittest.main()
