class Paziente:
    def __init__(self, CodiceFiscale, DataDiNascita, Nome, Cognome, Username, Password, Medico):
        self.CodiceFiscale = CodiceFiscale
        self.DataDiNascita = DataDiNascita
        self.Nome = Nome
        self.Cognome = Cognome
        self.Username = Username
        self.Password = Password
        self.Medico = Medico

    
    @property
    def Nome(self):
        return self._Nome

    @Nome.setter
    def Nome(self, value):
        self._Nome = value

    @property
    def Cognome(self):
        return self._Cognome

    @Cognome.setter
    def Cognome(self, value):
        self._Cognome = value

    @property
    def CodiceFiscale(self):
        return self._CodiceFiscale

    @CodiceFiscale.setter
    def CodiceFiscale(self, value):
        self._CodiceFiscale = value

    @property
    def DataDiNascita(self):
        return self._DataDiNascita

    @DataDiNascita.setter
    def DataDiNascita(self, value):
        self._DataDiNascita = value

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, value):
        self._Username = value

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, value):
        self._Password = value

    @property
    def Medico(self):
        return self._Medico

    @Medico.setter
    def Medico(self, value):
        self._Medico = value

    def prenota_appuntamento(self, data, motivo):
        print(f"{self.Nome} {self.Cognome} ha prenotato un appuntamento con il Medico {self.Medico} per il {data}. Motivo: {motivo}")
    
    def visualizza_anagrafica(self):
        print(f"Anagrafica di {self.Nome} {self.Cognome}:")
        print(f"Codice Fiscale: {self.CodiceFiscale}")
        print(f"Data di Nascita: {self.DataDiNascita}")
        print(f"Medico di Riferimento: {self.Medico}")
    
    def __str__(self):
        return f"Paziente(Nome={self.Nome}, Cognome={self.Cognome},CodiceFiscale={self.CodiceFiscale}, DataDiNascita={self.DataDiNascita}, Username={self.Username}, Medico={self.Medico})"