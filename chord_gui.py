import PySimpleGUI as sg
import process_csv
import microservice_request as rng
from help import help_text

chords = process_csv.process_csv('chords.csv')

progressions = {
    "Happy": ["i", "iv", "v", "i"],
    "Sad": ["vi", "iv", "i", "v"],
    "Hopeful": ["iv", "v", "vi", "i"]
}

last_progression = ()

sg.theme('DarkBlue')

# The create functions are the functions to create each window
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
    layout = [[sg.Button("Randomize Options"), sg.Button("Need help?")],
            [sg.Text("Key: "), sg.Combo(list(chords.keys()), key = "chord", enable_events = True), sg.Text("Mood: "), sg.Combo(list(progressions.keys()), key = "mood")],
            [sg.Button('Generate Chord Progression'), sg.Button('Exit')],
            [sg.Button('See last progression')]]
    window = sg.Window('Chord Buddy', layout)
    return window

def createHelp():
    layout = [[sg.Text(help_text)]]
    window = sg.Window("Help?", layout)
    return window

def createProgressionWindow(chords, key, mood):
    c1 = 'C:/Users/torrjond\OneDrive - Oregon State University/CS361/Chord Project/Chord Images/' + chords[0] + '.PNG'
    c2 = 'C:/Users/torrjond\OneDrive - Oregon State University/CS361/Chord Project/Chord Images/' + chords[1] + '.PNG'
    c3 = 'C:/Users/torrjond\OneDrive - Oregon State University/CS361/Chord Project/Chord Images/' + chords[2] + '.PNG'
    c4 = 'C:/Users/torrjond\OneDrive - Oregon State University/CS361/Chord Project/Chord Images/' + chords[3] + '.PNG'
    layout = [[sg.Text("Key: " + key), sg.Text("Mood: " + mood)],
            [sg.Image(c1)], [sg.Image(c2)], [sg.Image(c3)], [sg.Image(c4)]]
    window = sg.Window('CHORDS', layout)
    return window

exit = False

window = createMain()

while not exit: 
    event, values = window.read()
    
    # Event triggers on the different buttons - Titles are pretty self explanatory
    if event == 'Generate Chord Progression':
        if values['mood'] == '' or values['chord'] == '':
            error_window = createError()
            while True:
                error_event, error_values = error_window.read()
                if error_event == "OK":
                    error_window.close()
                    break
        else:
            chord_list = chords.get(values['chord']).make_progression(progressions[values['mood']])
            last_progression = (chord_list, values['chord'], values['mood'])
            chord_window = createProgressionWindow(chord_list, values['chord'], values['mood'])
            chord_event, chord_values = chord_window.read()

    if event == 'Randomize Options':
        try:
            values['chord'] = list(chords)[rng.rng(len(chords)-1)]
            values['mood'] = list(progressions)[rng.rng(len(progressions)-1)]
            chord_list = chords.get(values['chord']).make_progression(progressions[values['mood']])
            last_progression = (chord_list, values['chord'], values['mood'])
            chord_window = createProgressionWindow(chord_list, values['chord'], values['mood'])
            chord_event, chord_values = chord_window.read()

        except:
            print("Error: Microservice server not found")
    
    if event == 'Need help?':
        help_window = createHelp()
        help_event, help_values = help_window.read()

    if event == 'See last progression':
        chord_window = createProgressionWindow(last_progression[0], last_progression[1], last_progression[2])
        chord_event, chord_values = chord_window.read()
    
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