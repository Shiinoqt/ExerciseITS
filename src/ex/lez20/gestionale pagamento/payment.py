class Pagamento:
    def __init__(self):
        self.__amount = 0.0

    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount

    def dettagli_pagamento(self):
        print(f"Importo del pagamento: €{self.__amount:.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self, amount=0.0):
        super().__init__()
        self.set_amount(amount)

    def dettagli_pagamento(self):
        print(f"Pagamento in contanti: €{self.get_amount():.2f}")

    def in_pezzi_da(self):
        """Calcola e stampa la suddivisione dell'importo in banconote e monete"""
        importo = self.get_amount()
        
        if importo <= 0:
            print("Importo non valido per il calcolo delle banconote e monete.")
            return
        
        print(f"Suddivisione di €{importo:.2f} in banconote e monete:")
        
        # Valori delle banconote e monete in ordine decrescente
        tagli = [
            (500, "banconote da €500"),
            (200, "banconote da €200"), 
            (100, "banconote da €100"),
            (50, "banconote da €50"),
            (20, "banconote da €20"),
            (10, "banconote da €10"),
            (5, "banconote da €5"),
            (2, "monete da €2"),
            (1, "monete da €1"),
            (0.50, "monete da €0,50"),
            (0.20, "monete da €0,20"),
            (0.10, "monete da €0,10"),
            (0.05, "monete da €0,05"),
            (0.01, "monete da €0,01")
        ]
        
        # Conversione a centesimi per evitare problemi di precisione floating point
        resto_centesimi = round(importo * 100)
        
        for valore, descrizione in tagli:
            valore_centesimi = round(valore * 100)
            quantita = resto_centesimi // valore_centesimi
            
            if quantita > 0:
                if valore >= 1:
                    print(f"{quantita:2d} {descrizione}")
                else:
                    print(f"{quantita:2d} {descrizione}")
                resto_centesimi = resto_centesimi % valore_centesimi

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo=0.0, nome_titolare="", data_scadenza="", numero_carta=""):
        """Costruttore che definisce l'importo e le informazioni della carta di credito"""
        super().__init__()  # Chiama il costruttore della classe padre
        self.set_amount(importo)  # Imposta l'importo usando il metodo set()
        self.__nome_titolare = nome_titolare
        self.__data_scadenza = data_scadenza
        self.__numero_carta = numero_carta
    
    # Metodi get per gli attributi della carta
    def get_nome_titolare(self):
        """Restituisce il nome del titolare della carta"""
        return self.__nome_titolare
    
    def get_data_scadenza(self):
        """Restituisce la data di scadenza della carta"""
        return self.__data_scadenza
    
    def get_numero_carta(self):
        """Restituisce il numero della carta di credito"""
        return self.__numero_carta
    
    # Metodi set per gli attributi della carta
    def set_nome_titolare(self, nome):
        """Imposta il nome del titolare della carta"""
        self.__nome_titolare = nome
    
    def set_data_scadenza(self, data):
        """Imposta la data di scadenza della carta"""
        self.__data_scadenza = data
    
    def set_numero_carta(self, numero):
        """Imposta il numero della carta di credito"""
        self.__numero_carta = numero
    
    def dettagli_pagamento(self):
        """Ridefinisce il metodo per includere tutte le informazioni della carta di credito"""
        print(f"Pagamento con carta di credito: €{self.get_amount():.2f}")
        print(f"Titolare: {self.__nome_titolare}")
        print(f"Numero carta: {self._maschera_numero_carta()}")
        print(f"Data scadenza: {self.__data_scadenza}")
    
    def _maschera_numero_carta(self):
        """Metodo privato per mascherare il numero della carta (mostra solo le ultime 4 cifre)"""
        if len(self.__numero_carta) >= 4:
            return "**** **** **** " + self.__numero_carta[-4:]
        return self.__numero_carta


# Esempio di utilizzo
if __name__ == "__main__":
    print("="*70)
    print("           SISTEMA DI GESTIONE PAGAMENTI")
    print("="*70)
    
    # Test con due oggetti PagamentoContanti
    print("\n🟢 TEST PAGAMENTI IN CONTANTI")
    print("─" * 40)
    
    # PagamentoContanti 1
    print("\n💰 PAGAMENTO CONTANTI #1:")
    contanti1 = PagamentoContanti(245.67)
    contanti1.dettagli_pagamento()
    contanti1.in_pezzi_da()
    
    # PagamentoContanti 2
    print("\n💰 PAGAMENTO CONTANTI #2:")
    contanti2 = PagamentoContanti(89.23)
    contanti2.dettagli_pagamento()
    contanti2.in_pezzi_da()
    
    # Test con due oggetti PagamentoCartaDiCredito
    print("\n\n🔵 TEST PAGAMENTI CON CARTA DI CREDITO")
    print("─" * 40)
    
    # PagamentoCartaDiCredito 1
    print("\n💳 PAGAMENTO CARTA DI CREDITO #1:")
    carta1 = PagamentoCartaDiCredito(
        importo=156.50,
        nome_titolare="Mario Rossi",
        data_scadenza="12/2027",
        numero_carta="1234567812345678"
    )
    carta1.dettagli_pagamento()
    
    # PagamentoCartaDiCredito 2
    print("\n💳 PAGAMENTO CARTA DI CREDITO #2:")
    carta2 = PagamentoCartaDiCredito(
        importo=99.99,
        nome_titolare="Anna Verdi",
        data_scadenza="08/2026",
        numero_carta="9876543210987654"
    )
    carta2.dettagli_pagamento()
    
 