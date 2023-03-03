chords = {
    "eMajor": ["E", "G#", "B"],
    "eMinor": ["E", "G", "B"],
    "fMajor": ["F", "A", "C"],
    "fMinor": ["F", "Ab", "C"],
    "gMajor": ["G", "B", "D"],
    "gMinor": ["G", "Bb", "D"],
    "aMajor": ["A", "C#", "E"],
    "aMinor": ["A", "C", "E"],
    "cMajor": ["C", "E", "G"],
    "cMinor": ["C", "Eb", "G"],
}


def findChord(chordNote):
    for el in chords:
        if chordNote.upper() in chords[el] and chords[el][0] == chordNote.upper():
            print(
                f"Akordi koji započinju s tom notom su: {el}, a njegovi tonovi su {chords[el]}"
            )


chordNote = str(input("Unesi notu: "))
findChord(chordNote)
