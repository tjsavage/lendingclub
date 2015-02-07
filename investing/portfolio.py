import note

class Portfolio:
    def __init__(self, notes=[]):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    