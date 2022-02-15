import PySimpleGUI as sg
import chord_backend as chord

chords = {
    "A": chord.Chord("A", "B", "C#", "D", "E", "F#", "G#"),
    "B": chord.Chord("B", "C#", "D#", "E", "F#", "G#", "A#")
}

progression = ["i", "iv", "v", "i"]

sg.theme('DarkBlue')

layout = [[sg.OptionMenu(["Guitar", "Piano", "Help"])],
        [sg.Text('Your chord progression here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Button("Randomize Options")],
        [sg.Text("Key: "), sg.Combo(["A", "B", "C", "D", "E", "F", "G"], key = "chord", enable_events = True), sg.Text("Genre: "), sg.Combo(["Pop", "Jazz"])],
        [sg.Button('Generate Chord Progression'), sg.Button('Exit')]]

window = sg.Window('Chord Buddy', layout)

while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Generate Chord Progression':
        prog = chords.get(values['chord']).make_progression(progression)
        window['-OUTPUT-'].update(prog)

window.close()