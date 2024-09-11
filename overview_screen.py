from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.app import App

class OverviewScreen(Screen):
    def __init__(self, **kwargs):
        super(OverviewScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Neu Button
        self.new_button = Button(text="Neu", size_hint_y=None, height=50)
        self.new_button.bind(on_press=self.go_to_new_order)
        layout.add_widget(self.new_button)
        
        # Auftrag Liste
        self.order_list = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.order_list.bind(minimum_height=self.order_list.setter('height'))
        
        scroll_view = ScrollView(size_hint=(1, None), size=(self.width, 400))
        scroll_view.add_widget(self.order_list)
        
        layout.add_widget(scroll_view)
        self.add_widget(layout)
    
    def go_to_new_order(self, instance):
        self.manager.current = 'order'
    
    def load_orders(self):
        self.order_list.clear_widgets()
        app = App.get_running_app()  # Aktuelle App-Instanz abrufen
        for i, order in enumerate(app.orders):  # Beispiel für gespeicherte Aufträge
            btn = Button(text=f"Auftrag {i+1}: {order['auftragsnummer']}", size_hint_y=None, height=40)
            btn.bind(on_press=self.go_to_order_details)
            btn.order_index = i
            self.order_list.add_widget(btn)
    
    def go_to_order_details(self, instance):
        app = App.get_running_app()  # Aktuelle App-Instanz abrufen
        app.current_order_index = instance.order_index
        self.manager.current = 'details'
        self.manager.get_screen('details').display_order_details(instance.order_index)
