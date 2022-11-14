
class StringMapper(object):

    # zu Aufgabe 3
    # angefangen bei 1, für jedes neue feature um eins erhöhen,
    # bei wiederholung von features gleichen index behalten
    def __init__(self):
        self.map = {}
        self.inverse_map = {}
        self.counter = 1

    def lookup(self, s: str) -> int:
        if s in self.map:
            return self.map[s]
        else:
            self.map[s] = self.counter
            self.inverse_map[self.counter] = s
            self.counter += 1

    def inverseLookup(self, featureIndex: int)-> str:
        return self.inverse_map[featureIndex]
    # hilfreich um im nachhinein interpretieren zu können, welche features
    # besonders gut sind