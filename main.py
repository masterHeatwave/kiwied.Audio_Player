import kivy
import random
import os
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.uix.image import AsyncImage
from kivy.uix.filechooser import FileChooserListView
from kivy.resources import resource_find
from kivy.properties import StringProperty, ObjectProperty, ListProperty, \
    AliasProperty, BooleanProperty, NumericProperty
from kivy.loader import Loader


# delayed imports
Loader.num_workers = 4


def callback(instance):
        print('The button <%s> is being pressed' % instance.text)


red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]



class myLayout(BoxLayout):

    color = [red, green, blue, purple]


    def __init__(self, **kwargs):
            super(myLayout, self).__init__(**kwargs)

            layout = BoxLayout(pos=self.pos, size=self.size,spacing=10)

            self.add_widget(layout)

            flc = FileChooserListView(path='/home/edward/Music/', filters=['*.3gp'], size_hint=(3, 1))
            flc.bind(on_selection=self.play_pressed)
            layout.add_widget(flc)

        # creating the play button

            play = Button(text="PLAY", valign='center', halign='center', size_hint=(0.6, 0.5),
                       background_color=blue)
            layout.add_widget(play)
            play.bind(on_press=self.play_pressed)

        # creating the stop button

            stop = Button(text="STOP", valign='center', halign='center',
                      size_hint=(0.6, 0.6), background_color=red)
            layout.add_widget(stop)
            stop.bind(on_press=self.stop_pressed)

            display = Label(text="kiwiAudioPlayer", halign='right',
                        size=(7, 5))

            self.add_widget(display)

            animate = AsyncImage(source='https://i.gifer.com/KNGq.gif', allow_stretch=False, anim_delay=0.10)

            layout.add_widget(animate)



    def play_pressed(self, play):

            sound = SoundLoader.load('/home/edward/Music/massive attack/Mezzanine/02 Risingson.mp3')
            if sound:
                print("Sound found at %s" % sound.source)
                print("Sound is %.3f seconds" % sound.length)
            sound.play()

    def stop_pressed(self, stop):

            sound = SoundLoader.unload('/home/edward/Music/massive attack/Mezzanine/02 Risingson.mp3')
            sound.stop()

    def pressed(self, filename):

            with open(os.path.join(path, filename[0])):

                if self.soundf is None:
                    self.soundf = SoundLoader.load(self.path)
                if self.soundf.status != 'stop':
                    self.soundf.stop()
                    self.soundf.loop = False
                    self.soundf.play()

class FullImage(Image):

    pass


class musicApp(App):

    pass

    def build(self):

        return myLayout()

if __name__ == "__main__":
        app = musicApp()
        app.run()