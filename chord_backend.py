# This class stores the chords based on key
class Chord:
    def __init__(self, key, ii, iii, iv, v, vi, vii):
        self.chords = {
            "i": key,
            "ii": ii,
            "iii": iii,
            "iv": iv,
            "v": v,
            "vi": vi,
            "vii": vii
        }
    
    #Generates a progression based on a given list of chords (e.g. i -> iv -> vi)
    def make_progression(self, progression):
        prog = []
        for x in range(0, len(progression)):
            prog.append(self.chords.get(progression[x]))
        return prog
    
if __name__ == "__main__":
    test = Chord("A", "B", "C", "D", "E", "F", "G")
    prog = ["key", "iv", "v"]
    print(test.make_progression(prog))
