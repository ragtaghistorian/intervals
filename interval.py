import pyglet
from pyglet import font
import time

BELL_SOUND = 'OneBellRing.wav'
CLACK_SOUND = "clackClack.wav"
font.add_file('digital-7.ttf')
d7 = font.load('Digital-7', 16)

window = pyglet.window.Window(width=800, height=600,style=pyglet.window.Window.WINDOW_STYLE_DEFAULT)
window.set_caption('Interval')

icon1 = pyglet.image.load('play-btn-fill16.png')
icon2 = pyglet.image.load('play-btn32.png')
window.set_icon(icon1, icon2)

width = window.width
height = window.height
thetime = 0
running = False
gogogo = True
is_hovering = False

batch = pyglet.graphics.Batch()
pyglet.gl.glClearColor(0.8, 0.8, 0.8, 1.0)

rowB_x = 50
rowB_y = height - 50
rowC_x = 50
rowC_y = height - 90
rowD_x = 50
rowD_y = height - 140

html="<h1>set intervals and work/rest periods</h1>"
intervalInt = 1
workInt = 0
restInt = 0
currentInterval = 1
workSeconds = 60
restSeconds = 120

label = pyglet.text.HTMLLabel(html,
                              x=75,y=height-295,
                              width=window.width,
                              batch=batch,
                              multiline=True, anchor_y='center')


onebell = pyglet.resource.media(BELL_SOUND, streaming=False)
clack = pyglet.resource.media(CLACK_SOUND, streaming=False)
# Load button images
startUnpressed = pyglet.resource.image('play-btn.png')
startPressed = pyglet.resource.image('play-btn-fill.png')
startHover = pyglet.resource.image('play-btn-fill.png')

resetUnpressed = pyglet.resource.image('stop-btn.png')
resetPressed = pyglet.resource.image('stop-btn-fill.png')
resetHover = pyglet.resource.image('stop-btn-fill.png')

exitUnpressed = pyglet.resource.image('x-square.png')
exitPressed = pyglet.resource.image('x-square-fill.png')
exitHover = pyglet.resource.image('x-square-fill.png')

removeOne = pyglet.resource.image('arrow-down-square32.png')
removeOnePressed = pyglet.resource.image('arrow-down-square-fill32.png')
addOne = pyglet.resource.image('arrow-up-square32.png')
addOnePressed = pyglet.resource.image('arrow-up-square-fill32.png')

workDownUnpressed = pyglet.resource.image('arrow-down-square32.png')
workDownPressed = pyglet.resource.image('arrow-down-square-fill32.png')
workUpUnpressed = pyglet.resource.image('arrow-up-square32.png')
workUpPressed = pyglet.resource.image('arrow-up-square-fill32.png')

restDownUnpressed = pyglet.resource.image('arrow-down-square32.png')
restDownPressed = pyglet.resource.image('arrow-down-square-fill32.png')
restUpUnpressed = pyglet.resource.image('arrow-up-square32.png')
restUpPressed = pyglet.resource.image('arrow-up-square-fill32.png')


@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    global is_hovering
    if startbutton.x < x < startbutton.x + startbutton.width and startbutton.y < y < startbutton.y + startbutton.height:
        if not is_hovering:
            is_hovering = True
            push_label.text="press to start, press again to pause"
    else:
        if is_hovering:
            is_hovering = False
        if push_label.text=="press to start, press again to pause":
            push_label.text=""

    if resetButton.x < x < resetButton.x + resetButton.width and resetButton.y < y < resetButton.y + resetButton.height:
        if not is_hovering:
            is_hovering = True
            push_label.text="reset interval timer"
            # Change sprite image or trigger hover effect
    else:
        if is_hovering:
            is_hovering = False
        if push_label.text=="reset interval timer":
            push_label.text=""

    if exitButton.x < x < exitButton.x + exitButton.width and exitButton.y < y < exitButton.y + exitButton.height:
        if not is_hovering:
            is_hovering = True
            push_label.text="Exit"
            # Change sprite image or trigger hover effect
    else:
        if is_hovering:
            is_hovering = False
        if push_label.text=="Exit":
            push_label.text=""


def start_button_handler(widget, value):
    #print("hi")
    global running
    running = not running
    if running:
        pyglet.clock.schedule_interval(myupdate, 1)
    else:
        pyglet.clock.unschedule(myupdate)

    #label.text="<h1>pow pow pow</h1>"
    #label.font_name="Digital-7"
    #label.color=(255,255,0,255)
    #width = window.width
    #height = window.height
    #push_label.text = f"boom! {value}, width {width} height {height}"

def start_tip(widget):
    print("bam")
    #push_label.text = "Push Button: False"

def reset_button_handler(widget):
    thetime = 0
    running = False
    gogogo = True
    label.text="<h1>set intervals and work/rest periods</h1>"
    intervalInt = 1
    workInt = 0
    restInt = 0
    currentInterval = 1
    workSeconds = 60
    restSeconds = 120

def exit_button_handler(widget):
    pyglet.app.exit()


def release_button_handler(widget):
    pass
    #push_label.text = "Push Button: False"

def intervalUp_handler(widget):
    global intervalInt
    intervalInt+=1
    intervals_Count.text=str(intervalInt)

def intervalDown_handler(widget):
    global intervalInt
    if intervalInt >0:
        intervalInt-=1
    intervals_Count.text=str(intervalInt)

def workUp_handler(widget):
    global workInt
    workInt+=30
    m, s = divmod(workInt, 60)
    timeTemp = f'{round(m):02}:{round(s):02}'
    workTime.text=timeTemp

def workDown_handler(widget):
    global workInt
    if workInt > 0:
        workInt-=30
    m, s = divmod(workInt, 60)
    timeTemp = f'{round(m):02}:{round(s):02}'
    workTime.text=timeTemp

def restUp_handler(widget):
    global restInt
    restInt+=30
    m, s = divmod(restInt, 60)
    timeTemp = f'{round(m):02}:{round(s):02}'
    restTime.text=timeTemp

def restDown_handler(widget):
    global restInt
    if restInt > 0:
        restInt-=30
    m, s = divmod(restInt, 60)
    timeTemp = f'{round(m):02}:{round(s):02}'
    restTime.text=timeTemp


def myupdate(dt):
    #print(dt)
    global thetime
    global intervalInt
    global workInt
    global restInt
    global currentInterval
    global running
    global gogogo

    if running:
        global workSeconds
        workSeconds = workInt
        thetime += dt
        if gogogo:
            workSeconds = workInt
        else:
            workSeconds = restInt

        if currentInterval <= intervalInt:
            if gogogo:
                m, s = divmod(workSeconds-thetime, 60)
                #print(f'{round(m):02}:{round(s):02}')
                timeTemp = f'{round(m):02}:{round(s):02}'
                pyglet.gl.glClearColor(1, 1, 1, 1.0)
                label.text="<center><h1>Work Work Work:</h1></center><center><p>"+str(currentInterval)+" of "+str(intervalInt)+"</center></p></center><center><p> "+timeTemp+"</p></center>"
                label.font_name="Digital-7"
                label.color=(0,255,0,255)
                label.background_color=None
                label.font_size=56
                if int(s) == 10 and int(m)== 0:
                    clack.play()
                if workSeconds-thetime <1:
                    onebell.play()
                    thetime = 0
                    gogogo = not gogogo
            else:
                m, s = divmod(restInt-thetime, 60)
                #print(f'{round(m):02}:{round(s):02}')
                timeTemp = f'{round(m):02}:{round(s):02}'
                pyglet.gl.glClearColor(0.8, 0.8, 0.8, 1.0)
                label.text="<center><h1>Active Rest:</h1></center><center><p>"+str(currentInterval)+" of "+str(intervalInt)+"</center><br><center>"+timeTemp+"</p></center>"
                label.font_name="Digital-7"
                label.color=(255,255,0,255)
                label.background_color=0,0,255,255
                label.font_size=56
                if restInt-thetime < 1:
                    onebell.play()
                    thetime=0
                    currentInterval += 1
                    gogogo = not gogogo
        elif currentInterval > intervalInt:
            onebell.play()
            time.sleep(.25)
            onebell.play()
            label.text='<h1>Done</h1>'
            startbutton.value = not startbutton.value
            thetime = 0
            currentInterval = 1
            pyglet.clock.unschedule(myupdate)



frame = pyglet.gui.Frame(window, order=4)


startbutton = pyglet.gui.ToggleButton((width-210) // 2, 50, pressed=startPressed, unpressed=startUnpressed, hover=startHover,batch=batch)
startbutton.set_handler('on_toggle', start_button_handler)
startbutton.set_handler('on_mouse_motion',start_tip)
#pushbutton.set_handler('on_release', release_button_handler)
frame.add_widget(startbutton)
push_label = pyglet.text.Label(" ", x=(width-210) // 2, y=150, batch=batch, color=(255, 0, 0, 255))

resetButton = pyglet.gui.PushButton(((width-210) // 2)+70, 50, pressed=resetPressed, unpressed=resetUnpressed, hover=resetHover,batch=batch)
resetButton.set_handler('on_press', reset_button_handler)
#pushbutton.set_handler('on_release', release_button_handler)
frame.add_widget(resetButton)

exitButton = pyglet.gui.PushButton(((width-210) // 2)+175, 50, pressed=exitPressed, unpressed=exitUnpressed, hover=exitHover,batch=batch)
exitButton.set_handler('on_press', exit_button_handler)
#pushbutton.set_handler('on_release', release_button_handler)
frame.add_widget(exitButton)

intervals_label = pyglet.text.Label("Intervals", x=rowB_x, y=rowB_y, batch=batch, color=(0, 0, 0, 255))
intervals_Count = pyglet.text.Label("1", font_name="Digital-7",font_size=36,x=rowC_x, y=rowC_y, batch=batch, color=(0, 0, 0, 255))

intervalButtonUp = pyglet.gui.PushButton(rowD_x, rowD_y, pressed=addOnePressed, unpressed=addOne, batch=batch)
intervalButtonUp.set_handler('on_press', intervalUp_handler)
frame.add_widget(intervalButtonUp)

intervalButtonDown = pyglet.gui.PushButton(rowD_x+35, rowD_y, pressed=removeOnePressed, unpressed=removeOne, batch=batch)
intervalButtonDown.set_handler('on_press', intervalDown_handler)
frame.add_widget(intervalButtonDown)

work_label = pyglet.text.Label("Work", x=rowB_x+250, y=rowB_y, batch=batch, color=(0, 0, 0, 255))
workTime = pyglet.text.Label("00:00", font_name="Digital-7",font_size=36,x=rowC_x+250, y=rowC_y, batch=batch, color=(0, 0, 0, 255))
workButtonUp = pyglet.gui.PushButton(rowD_x+250, rowD_y, pressed=workUpPressed, unpressed=workUpUnpressed, batch=batch)
workButtonUp.set_handler('on_press', workUp_handler)
frame.add_widget(workButtonUp)

workButtonDown = pyglet.gui.PushButton(rowD_x+250+35, rowD_y, pressed=workDownPressed, unpressed=workDownUnpressed, batch=batch)
workButtonDown.set_handler('on_press', workDown_handler)
frame.add_widget(workButtonDown)

rest_label = pyglet.text.Label("Active Rest", x=rowB_x+450, y=rowB_y, batch=batch, color=(0, 0, 0, 255))
restTime = pyglet.text.Label("00:00", font_name="Digital-7",font_size=36,x=rowC_x+450, y=rowC_y, batch=batch, color=(0, 0, 0, 255))
restButtonUp = pyglet.gui.PushButton(rowD_x+450, rowD_y, pressed=restUpPressed, unpressed=restUpUnpressed, batch=batch)
restButtonUp.set_handler('on_press', restUp_handler)
frame.add_widget(restButtonUp)

restButtonDown = pyglet.gui.PushButton(rowD_x+450+35, rowD_y, pressed=restDownPressed, unpressed=restDownUnpressed, batch=batch)
restButtonDown.set_handler('on_press', restDown_handler)
frame.add_widget(restButtonDown)



#pyglet.clock.schedule_interval(myupdate, 1/30)

pyglet.app.run()
