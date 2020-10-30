from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.filechooser import FileChooserListView
from kivy.core.audio import SoundLoader


def callback(instance):
   print('The button <%s> is being pressed' % instance.text)


red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class myLayout(BoxLayout):

    color = [red, green, blue, purple]
    path = '/home/edward/Music'


    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)
        self.sound = None

        layout = BoxLayout(pos=self.pos, size=self.size,spacing=10)

        self.add_widget(layout)

        flc = FileChooserListView(path='/home/edward/Music',filters=['*.mp3'],size=(7, 3))
        flc.bind(selection=self.load_sound)  # bind to the property `selection`

        layout.add_widget(flc)

        # creating the play button

        play = Button(text="PLAY",valign='center', halign='center',background_color=blue,size_hint=(0.3, 0.5))

        play.bind(on_press=self.play_pressed)
        layout.add_widget(play)

        # creating the stop button

        stop = Button(text="STOP", valign='center',halign='center',size_hint=(0.3, 0.6),background_color=red)
        layout.add_widget(stop)
        stop.bind(on_press=self.stop_pressed)

        #creating a Label

        display=Label(text="kiwiAudioPlayer",halign='right', size=(3,5))

        layout.add_widget(display)

        #displaying an animated image

        animate = AsyncImage(source='https://i.gifer.com/KNGq.gif',                              allow_stretch=False, anim_delay=0.10)

        layout.add_widget(animate)

    #trying to define a load song function

    def load_sound(self, filechooser, selection):

        if self.sound is not None:
            self.sound.stop()
        self.sound = SoundLoader.load(selection[0])

    #play button function

    def play_pressed(self, button):

        if self.sound is not None:
            self.sound.play()

    #stop button function

    def stop_pressed(self, button):

        if self.sound is not None:
            self.sound.stop()

#main function

class musicApp(App):

   def build(self):

      return myLayout()

if __name__ == "__main__":
       app = musicApp()
       app.run()
