class paziente:
    def __init__(self, nome, cognome, codicefiscale, data_nascita, username, password, medico):
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
        self.data_nascita = data_nascita
        self.username = username
        self.password = password
        self.medico = medico

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, value):
        self._cognome = value

    @property
    def codicefiscale(self):
        return self._codicefiscale

    @codicefiscale.setter
    def codicefiscale(self, value):
        self._codicefiscale = value

    @property
    def data_nascita(self):
        return self._data_nascita

    @data_nascita.setter
    def data_nascita(self, value):
        self._data_nascita = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, value):
        self._medico = value

    def prenota_appuntamento(self, data, motivo):
        print(f"{self.nome} {self.cognome} ha prenotato un appuntamento con il medico {self.medico} per il {data}. Motivo: {motivo}")
    
    def visualizza_anagrafica(self):
        print(f"Anagrafica di {self.nome} {self.cognome}:")
        print(f"Codice Fiscale: {self.codicefiscale}")
        print(f"Data di Nascita: {self.data_nascita}")
        print(f"Medico di Riferimento: {self.medico}")
    
    def __str__(self):
        return f"Paziente(nome={self.nome}, cognome={self.cognome},codicefiscale={self.codicefiscale}, data_nascita={self.data_nascita}, username={self.username}, medico={self.medico})"