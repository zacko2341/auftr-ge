from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.app import App
from plyer import camera
import os
from screens.storage_manager import save_orders

class OrderScreen(Screen):
    def __init__(self, **kwargs):
        super(OrderScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Auftragsnummer
        self.auftragsnummer_input = TextInput(hint_text="Auftragsnummer")
        layout.add_widget(self.auftragsnummer_input)
        
        # Adresseingabe
        self.strasse_input = TextInput(hint_text="Straße")
        self.hausnummer_input = TextInput(hint_text="Hausnummer")
        self.adresszusatz_input = TextInput(hint_text="Adresszusatz")
        self.ort_input = TextInput(hint_text="Ort")
        layout.add_widget(self.strasse_input)
        layout.add_widget(self.hausnummer_input)
        layout.add_widget(self.adresszusatz_input)
        layout.add_widget(self.ort_input)
        
        # Kamera Button
        self.photo_button = Button(text="Foto aufnehmen")
        self.photo_button.bind(on_press=self.take_photo)
        layout.add_widget(self.photo_button)
        
        # Längere Beschreibung
        self.beschreibung_input = TextInput(hint_text="Beschreibung", multiline=True)
        layout.add_widget(self.beschreibung_input)
        
        # E-Mail Adresse
        self.email_input = TextInput(hint_text="E-Mail-Adresse")
        layout.add_widget(self.email_input)
        
        # Senden Button
        self.send_button = Button(text="Senden")
        self.send_button.bind(on_press=self.send_email)
        layout.add_widget(self.send_button)
        
        # Speichern Button
        self.save_button = Button(text="Speichern")
        self.save_button.bind(on_press=self.save_order)
        layout.add_widget(self.save_button)
        
        # Zurück Button
        self.back_button = Button(text="Zurück")
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)
        
        # Variable zum Speichern des Foto-Pfads
        self.photo_path = None
    
    def take_photo(self, instance):
        # Dateiname für das Foto basierend auf der Auftragsnummer
        filename = f"{self.auftragsnummer_input.text}_photo.jpg"
        photo_dir = os.path.join(os.getcwd(), "photos")
        if not os.path.exists(photo_dir):
            os.makedirs(photo_dir)
        self.photo_path = os.path.join(photo_dir, filename)
        
        # Foto aufnehmen und speichern
        try:
            camera.take_picture(filename=self.photo_path, on_complete=self.photo_taken)
        except NotImplementedError:
            print("Kamera nicht verfügbar auf diesem Gerät.")
    
    def photo_taken(self, path):
        if path:
            print(f"Foto gespeichert unter: {path}")
        else:
            print("Fotoaufnahme fehlgeschlagen.")
    
    def send_email(self, instance):
        # Hier kommt der Code für das Senden der E-Mail
        print("E-Mail senden")
    
    def save_order(self, instance):
        app = App.get_running_app()  # Aktuelle App-Instanz abrufen
        # Speichern der Eingaben in einer Liste (oder später in einer Datei/Datenbank)
        order_data = {
            'auftragsnummer': self.auftragsnummer_input.text,
            'strasse': self.strasse_input.text,
            'hausnummer': self.hausnummer_input.text,
            'adresszusatz': self.adresszusatz_input.text,
            'ort': self.ort_input.text,
            'beschreibung': self.beschreibung_input.text,
            'email': self.email_input.text,
            'photo_path': self.photo_path,  # Pfad zum Foto speichern
        }
        app.orders.append(order_data)
        save_orders(app.orders)  # Speichern in die Datei
        self.manager.get_screen('overview').load_orders()
        print("Auftrag gespeichert:", order_data)
    
    def go_back(self, instance):
        self.manager.current = 'overview'
