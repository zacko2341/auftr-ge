from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.app import App

class DetailsScreen(Screen):
    def __init__(self, **kwargs):
        super(DetailsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Beispiel Label für Details
        self.details_label = Label(text="Details hier anzeigen")
        layout.add_widget(self.details_label)
        
        # Speichern Button
        self.save_button = Button(text="Speichern")
        self.save_button.bind(on_press=self.save_current_order)
        layout.add_widget(self.save_button)
        
        # Löschen Button
        self.delete_button = Button(text="Löschen", background_color=(1, 0, 0, 1))  # Rot hinterlegt für den Löschen-Button
        self.delete_button.bind(on_press=self.delete_current_order)
        layout.add_widget(self.delete_button)
        
        # Zurück Button
        self.back_button = Button(text="Zurück")
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)
    
    def display_order_details(self, order_index):
        app = App.get_running_app()  # Aktuelle App-Instanz abrufen
        order = app.orders[order_index]
        self.details_label.text = (
            f"Auftragsnummer: {order['auftragsnummer']}\n"
            f"Adresse: {order['strasse']} {order['hausnummer']}, "
            f"{order['adresszusatz']}, {order['ort']}\n"
            f"Beschreibung: {order['beschreibung']}\n"
            f"E-Mail: {order['email']}\n"
            f"Foto: {order['photo_path']}"
        )
    
    def save_current_order(self, instance):
        # Hier könnte man die Änderungen am aktuellen Auftrag speichern
        print("Auftrag wurde aktualisiert.")
    
    def delete_current_order(self, instance):
        app = App.get_running_app()  # Aktuelle App-Instanz abrufen
        if app.current_order_index is not None:
            # Löschen des aktuellen Auftrags
            del app.orders[app.current_order_index]
            app.current_order_index = None
            print("Auftrag wurde gelöscht.")
            # Aktualisiere die Übersichtsliste
            self.manager.get_screen('overview').load_orders()
            # Zurück zur Übersicht
            self.manager.current = 'overview'
    
    def go_back(self, instance):
        self.manager.current = 'overview'
