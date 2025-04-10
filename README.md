interval training tool
# pygletInterval

Pyglet's frame coordinate system aligns with the OpenGL standard, where the origin (0, 0) is located at the bottom-left corner of the window. The X-axis extends horizontally to the right, and the Y-axis extends vertically upwards. Coordinates are measured in pixels. When drawing elements, their positions are specified relative to this coordinate system. For example, drawing an image at coordinates (100, 150) will position the image's anchor point (by default, the bottom-left corner) 100 pixels to the right and 150 pixels up from the bottom-left corner of the window.
