from DSEngine import *
from pygame import Vector2

window = Window(fps=120, size=(1280, 720), title="Animation Tool", bg=(100, 100, 100))
editor_button = Button("Editor", position=Vector2(500, 0))
preview_button = Button("Preview", position=Vector2(editor_button.rect.right+25, 0))
preview_text = Text2D("Preview", position=Vector2(150, 350))
editor_text = Text2D("Editor", position=Vector2(150, 350))
editor_button.init(window)
preview_button.init(window)
preview_text.init(window)
editor_text.init(window)
editor = True
preview = False
while window.running:
    keys = window.frame()
    editor_text.visible = editor
    preview_text.visible = False
    if editor_button.pressed:
        editor = True
        preview = False
    if preview_button.pressed:
        preview = True
        editor = False