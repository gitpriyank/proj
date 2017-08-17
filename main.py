from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import time
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras import backend as K
K.set_image_dim_ordering('th')
import numpy as np
from PIL import Image

m, n = 100, 50
classes = ['Apple-black-spot', 'Apple-broad-leaf-spot', 'Apple-needle-leaf-spot1', 'Apple-normal', 'Bell-pepper-blight', 'Bell-pepper-normal', 'Blueberry-normal', 'Cherry-Normal', 'Cherry-powdery-mildew', 'Corn-blight', 'Corn-blight1', 'Corn-normal', 'Corn-rust', 'Grape-black-spot', 'Grape-blight', 'Grape-normal', 'Grape-rust', 'Orange-normal', 'Peach-blight', 'Peach-normal', 'Potato-black-spot', 'Potato-black-spot,-powdery-mildew', 'Potato-normal', 'Rasberry-normal', 'Soybean-normal', 'Squash-powdery-mildew', 'Strawberry-normal', 'Strawberry-rust', 'Tomato-bacterial-spot', 'Tomato-early-blight', 'Tomato-late-blight', 'Tomato-powdery-mildew', 'Tomato-septorial-leaf-spot', 'Tomato-spider-mite', 'Tomato-target-spot', 'Tomato-yellow-leaf-curl']
model = load_model('cnnmodel0.h5')

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        Button:
            text: 'Plant Disease Information'
            on_press: root.manager.current = 'Plants'
        Button:
            text: 'Open Camera'
            on_press: root.manager.current = 'camera'
        Button:
            text: 'Quit'
            on_press: root.quit()
            
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    
<Plants>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Apple'
            on_press: root.manager.current = 'diseaseApple'
        Button:
            text: 'Bell-pepper'
            on_press: root.manager.current = 'diseaseBellpepper'
        Button:
            text: 'Cherry'
            on_press: root.manager.current = 'diseaseCherry'
        Button:
            text: 'Corn'
            on_press: root.manager.current = 'diseaseCorn'
        Button:
            text: 'Grape'
            on_press: root.manager.current = 'diseaseGrape'
        
        Button:
            text: 'Peach'
            on_press: root.manager.current = 'diseasePeach'
        Button:
            text: 'Potato'
            on_press: root.manager.current = 'diseasePotato'
        
        Button:
            text: 'Squash'
            on_press: root.manager.current = 'diseaseSquash'
        Button:
            text: 'Strawberry'
            on_press: root.manager.current = 'diseaseStrawberry'
        Button:
            text: 'Tomato'
            on_press: root.manager.current = 'diseaseTomato'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'main'
<Apple>:
    BoxLayout:
        orientation: 'vertical'
        Button: 
            text: 'BlackSpot'
            on_press: root.manager.current = 'blackspot'
        Button:
            text: 'LeafSpot'
            on_press: root.manager.current = 'leafspot'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Bellpepper>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Blight'
            on_press: root.manager.current = 'blight'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'       
<Cherry>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Powdery Mildew'
            on_press: root.manager.current = 'powderymildew'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Corn>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Blight'
            on_press: root.manager.current = 'blight'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Grape>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Black spot'
            on_press: root.manager.current = 'blackspot'
        Button:
            text: 'Blight'
            on_press: root.manager.current = 'blight'
        Button:
            text: 'Rust'
            on_press: root.manager.current = 'rust'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Peach>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Blight'
            on_press: root.manager.current = 'blight'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Potato>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Black-Spot'
            on_press: root.manager.current = 'blackspot'
        Button:
            text: 'Powdery-mildew'
            on_press: root.manager.current = 'powderymildew'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Squash>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Powdery-Mildew'
            on_press: root.manager.current = 'powderymildew'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Strawberry>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Rust'
            on_press: root.manager.current = 'rust'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Tomato>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Bacterial-Spot'
            on_press: root.manager.current = 'bacterialspot'
        Button:
            text: 'Blight'
            on_press: root.manager.current = 'blight'
        Button:
            text: 'Powdery-Mildew'
            on_press: root.manager.current = 'powderymildew'
        Button:
            text: 'Spectoria-Spot'
            on_press: root.manager.current = 'spectoriaspot'
        Button:
            text: 'Spider-Mite'
            on_press: root.manager.current = 'spidermite'
        Button:
            text: 'Target-Spot'
            on_press: root.manager.current = 'targetleafspot'
        Button:
            text: 'Yellow-leaf-curl'
            on_press: root.manager.current = 'yellowleafcurl'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'

<PowderyMildew>:
    orientation: 'vertical'
    BoxLayout:
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Blight>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<BlackSpot>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<LeafSpot>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Yellowleafcurl>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<Rust>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<SpiderMite>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
<SpectoriaSpot>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'

<Targetleafspot>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter text here'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'Plants'
""")

# Declare both screens
class MainScreen(Screen):
    pass

class Plants(Screen):
    pass

class Apple(Screen):
    pass

class Bellpepper(Screen):
    pass
class Blueberry(Screen):
    pass
class Cherry(Screen):
    pass
class Corn(Screen):
    pass
class Grape(Screen):
    pass

class Peach(Screen):
    pass
class Potato(Screen):
    pass

class Squash(Screen):
    pass
class Strawberry(Screen):
    pass
class Tomato(Screen):
    pass

class PowderyMildew(Screen):
    pass

class Blight(Screen):
    pass

class BlackSpot(Screen):
    pass

class LeafSpot(Screen):
    pass

class YellowLeafCurl(Screen):
    pass

class Rust(Screen):
    pass

class SpiderMite(Screen):
    pass

class SpectoriaSpot(Screen):
    pass

class TargetLeafSpot(Screen):
    pass

class CameraClick(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        img = camera.export_to_png("IMG_{}.png".format(timestr))
        # img = Image.open('0a4fd67d786615190d63a0fe47d70646.jpg')
        # img = img.convert(mode='RGB')
        img = img.resize((m, n))
        img = img_to_array(img)/255
        img = img.transpose(2, 0, 1)
        img = img.reshape(3, m, n)
        x = []
        x.append(img)
        x = np.array(x)
        predictions = model.predict(x)
        c = np.amax(predictions)
        ind = np.argmax(predictions)


        co = np.delete(predictions, ind)
        classes.pop(ind)
        d = np.amax(co)
        inde = np.argmax(co)
        content = Label(text=classes[ind])
        popup = Popup(title='Test popup', content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

        # print("Captured")


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(Plants(name='Plants'))
sm.add_widget(CameraClick(name='camera'))
sm.add_widget(Apple(name='diseaseApple'))
sm.add_widget(Bellpepper(name='diseaseBellpepper'))
sm.add_widget(Blueberry(name='diseaseBlueberry'))
sm.add_widget(Cherry(name='diseasecherry'))
sm.add_widget(Corn(name='diseaseCorn'))
sm.add_widget(Grape(name='diseaseGrape'))

sm.add_widget(Peach(name='diseasePeach'))
sm.add_widget(Potato(name='diseasePotato'))


sm.add_widget(Squash(name='diseaseSquash'))
sm.add_widget(Strawberry(name='diseaseStrawberry'))
sm.add_widget(Tomato(name='diseaseTomato'))

sm.add_widget(PowderyMildew(name='powderymildew'))
sm.add_widget(Blight(name='blight'))
sm.add_widget(Rust(name='rust'))
sm.add_widget(BlackSpot(name='blackspot'))
sm.add_widget(LeafSpot(name='leafspot'))
sm.add_widget(YellowLeafCurl(name='yellowleafcurl'))
sm.add_widget(SpectoriaSpot(name='spectoriaspot'))
sm.add_widget(SpiderMite(name='spidermite'))
sm.add_widget(TargetLeafSpot(name='targetleafspot'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
