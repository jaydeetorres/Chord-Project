import PySimpleGUI as sg
import process_csv
import microservice_request as rng

chords = process_csv.process_csv('chords.csv')

progressions = {
    "Happy": ["i", "iv", "v", "i"],
    "Sad": ["vi", "iv", "i", "v"],
    "Hopeful": ["iv", "v", "vi", "i"]
}

sg.theme('DarkBlue')

def createExit():
    exit_layout = [[sg.Text("Are you sure you would like to exit?")],
            [sg.Button("Yes"), sg.Button("No")]]
    exit_window = sg.Window('Exit?', exit_layout)
    return exit_window

def createError():
    error_layout = [[sg.Text("Please select a key and mood from the options menu")],
                    [sg.Button("OK")]]
    error_window = sg.Window('Invalid reponse', error_layout)
    return error_window

def createMain():
    layout = [[sg.OptionMenu(["Guitar", "Piano", "Help"])],
            [sg.Button("Randomize Options")],
            [sg.Text("Key: "), sg.Combo(list(chords.keys()), key = "chord", enable_events = True), sg.Text("Mood: "), sg.Combo(list(progressions.keys()), key = "mood")],
            [sg.Button('Generate Chord Progression'), sg.Button('Exit')],
            [sg.Text('Scale: '), sg.Text(key = '-CHORD-'), sg.Text('Mood: '), sg.Text(key = '-MOOD-')],
            [sg.Text('Your chord progression here:'), sg.Text(size=(15,1), key='-OUTPUT-')]]
    window = sg.Window('Chord Buddy', layout)
    return window

def updateProgression(chord, mood, window):
    prog = chords.get(chord).make_progression(progressions[mood])
    window['-CHORD-'].update(chord)
    window['-MOOD-'].update(mood)
    window['-OUTPUT-'].update(prog)

exit = False

window = createMain()

while not exit: 
    event, values = window.read()
    
    if event == 'Generate Chord Progression':
        if values['mood'] == '' or values['chord'] == '':
            error_window = createError()
            while True:
                error_event, error_values = error_window.read()
                if error_event == "OK":
                    error_window.close()
                    break
        else:
            updateProgression(values['chord'], values['mood'], window)

    if event == 'Randomize Options':
        try:
            chord_rand = rng.rng(len(chords)-1)
            prog_rand = rng.rng(len(progressions)-1)
            values['chord'] = list(chords)[chord_rand]
            values['mood'] = list(progressions)[prog_rand]
            updateProgression(values['chord'], values['mood'], window)

        except:
            print("Error: Microservice server not found")
    
    if event == sg.WIN_CLOSED:
        break

    if event == 'Exit':
        exit_window = createExit()
        while True:
            exit_event, exit_values = exit_window.read()
            if exit_event == "Yes":
                exit_window.close()
                exit = True
                break
            elif exit_event == "No":
                exit_window.close()
                break

window.close()