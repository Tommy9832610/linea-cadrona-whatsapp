# linea_cadoma_simulator.py

import time

class LineaCadornaWhatsApp:
    def __init__(self, chat_name):
        self.chat_name = chat_name
        self.bunker_active = False

    def ricevi_notifica(self, tipo_minaccia):
        print(f"\n[!] Allarme in corso sulla chat: '{self.chat_name}'")
        if tipo_minaccia == "VERDE":
            print(">>> Rilevato meme o auguri. Protocollo: Pollicino fantasma.")
        elif tipo_minaccia == "GIALLO":
            print(">>> Rilevato invito vago. Protocollo: 'Appena mi stabilizzo'.")
        elif tipo_minaccia == "ROSSO":
            print(">>> ATTENZIONE: Sondaggio per cena di classe con menù fisso!")
            self.attiva_protocollo_ortler()

    def attiva_protocollo_ortler(self):
        print("❄️ Attivazione scavo igloo di ghiaccio in corso...")
        time.sleep(1)
        print("🔇 Chat impostata su 'Silenzioso per sempre'.")
        print("🗄️ Chat archiviata in fondo alla rubrica. Permafrost raggiunto.")
        self.bunker_active = True
        print("☕ Versamento tisana calda completato. Sei al sicuro.")

# Esecuzione del test di sopravvivenza
if __name__ == "__main__":
    chat_liceo = LineaCadornaWhatsApp("Liceo Scientifico '5ªB' - Rimpatriata 20 anni")
    chat_liceo.ricevi_notifica("ROSSO")
