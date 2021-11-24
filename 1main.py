from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line,Triangle
from kivy.uix.button import Button
from random import uniform

class MyPaintWidget(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            Color(uniform(.3,1),uniform(.3,1),uniform(.3,1))
            #d=30
            #touch.ud['Ellipse']=Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
            #Triangle(pos=(touch.x,touch.y,touch.x+touch.width/4,touch.y,touch.x+touch.width/4,touch.y+touch.height/4))
            touch.ud['line']=Line(points=(touch.x,touch.y),width=3)
    def on_touch_move(self,touch):
        #d=30
        touch.ud['line'].points +=[touch.x,touch.y]
        
        #touch.ud['Ellipse'].pos +=[touch.x-d/2,touch.y-d/2]

class MyPaintApp(App):
    def build(self):
        parent_class=Widget()
        self.painter = MyPaintWidget()
        clear=Button(text="clear")

        clear.bind(on_release=self.clear_canvas)

        parent_class.add_widget(self.painter)
        parent_class.add_widget(clear)

        return parent_class

    def clear_canvas(self,obj):
        self.painter.canvas.clear()

if __name__=='__main__':
    MyPaintApp().run()