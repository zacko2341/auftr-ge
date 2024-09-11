from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.overview_screen import OverviewScreen
from screens.order_screen import OrderScreen
from screens.details_screen import DetailsScreen
from screens.storage_manager import save_orders, load_orders

class AuftragApp(App):
    def build(self):
        self.title = "Auftrags-App"
        
        # Aufträge laden
        self.orders = load_orders()
        self.current_order_index = None
        
        # Screen Manager
        sm = ScreenManager()
        
        # Overview Screen
        self.overview_screen = OverviewScreen(name='overview')
        sm.add_widget(self.overview_screen)
        
        # Order Screen (Neueingabe)
        self.order_screen = OrderScreen(name='order')
        sm.add_widget(self.order_screen)
        
        # Details Screen
        self.details_screen = DetailsScreen(name='details')
        sm.add_widget(self.details_screen)
        
        # Lade gespeicherte Aufträge beim Start
        self.overview_screen.load_orders()
        
        return sm
    
    def on_stop(self):
        """Beim Beenden der App Aufträge speichern."""
        save_orders(self.orders)

if __name__ == "__main__":
    AuftragApp().run()
