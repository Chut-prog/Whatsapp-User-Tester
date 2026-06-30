import pyautogui
import time
import itertools
import string
import pyperclip
import sys

class WhatsAppScanner:
    def __init__(self):
        print(">>> 5s pour bouton 'Enregistrer'...")
        time.sleep(5)
        self.btn_pos = pyautogui.position()
        print(">>> 5s pour zone erreur...")
        time.sleep(5)
        self.error_pos = pyautogui.position()
        print(">>> 5s pour champ saisie...")
        time.sleep(5)
        self.input_pos = pyautogui.position()
        
        self.total_tests = 0
        self.disponibles = []
        print("\n--- CONFIGURATION OK ---")

    def get_status(self):
        btn = pyautogui.pixel(*self.btn_pos)
        err = pyautogui.pixel(*self.error_pos)
        if btn[1] > 120 and btn[0] < 100: return True
        if err[0] > 150 and err[1] < 100: return False
        return None

    def run_test(self, pseudo):
        pyautogui.click(*self.input_pos)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyperclip.copy(pseudo)
        pyautogui.hotkey('ctrl', 'v')
        
        for _ in range(30):
            status = self.get_status()
            if status is not None: return status
            time.sleep(0.01)
        return False

    def start(self):
        print("\n--- TEST TÉMOIN ---")
        if self.run_test("adrien.gf"): print("Témoin : LIBRE")
        else: print("Témoin : PRIS/ERREUR")
        
        time.sleep(2)
        print("\n--- DÉBUT TESTS (Liste des trouvés en temps réel) ---")
        print("-" * 50)
        
        chars = string.ascii_lowercase + "0123456789"
        try:
            for p in itertools.product(chars, repeat=3):
                pseudo = "".join(p)
                self.total_tests += 1
                
                if self.run_test(pseudo):
                    print(f"\n[!!!] DISPONIBLE : {pseudo}")
                    self.disponibles.append(pseudo)
                
                # Mise à jour du compteur sur la même ligne
                sys.stdout.write(f"\rTests effectués: {self.total_tests} | Trouvés: {len(self.disponibles)}")
                sys.stdout.flush()
        
        except KeyboardInterrupt:
            print("\n\nArrêt utilisateur.")
        finally:
            print("\n\n" + "="*30)
            print("RÉSUMÉ FINAL")
            print(f"Total testés : {self.total_tests}")
            print(f"Disponibles  : {', '.join(self.disponibles) if self.disponibles else 'Aucun'}")
            print("="*30)

if __name__ == "__main__":
    scanner = WhatsAppScanner()
    scanner.start()