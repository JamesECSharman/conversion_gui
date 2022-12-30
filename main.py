import PySimpleGUI as Gui

themes = Gui.theme("DarkTeal10")

label_feet = Gui.Text("Enter your feet:", size=(15, 1), key="feet", expand_y=True, expand_x=True)
input_feet = Gui.Input(size=(20, 0), expand_x=True, expand_y=True, justification='center')
label_inches = Gui.Text("Enter your inches:", size=(15, 1), key="inches", expand_y=True, expand_x=True)
input_inches = Gui.Input(size=(20, 0), expand_x=True, expand_y=True, justification='center')
conversion_rate = Gui.Combo(values=['Meters', 'Centimeters', 'Yards'], size=(15, 4), font=("Helvetica", 18))

convert_button = Gui.Button("Convert", expand_y=False, expand_x=False, auto_size_button=False)
output_label = Gui.Text(key="output", expand_y=True, expand_x=True, justification='center', font=("Helvetica", 18))

window_column_1 = [[label_feet, input_feet], [label_inches, input_inches], [convert_button]]
window_column_2 = [[conversion_rate], [output_label]]

layout = [[Gui.Column(window_column_1, element_justification='l', expand_y=True, expand_x=True, vertical_alignment='center'),
           Gui.Column(window_column_2, element_justification='l', vertical_alignment='bottom', expand_y=True,
                      expand_x=True)]]

window = Gui.Window("Convertor", layout=layout, resizable=True,
                    auto_size_buttons=False, default_element_size=(12, 1), font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event, values)
    feet = int(values[0])
    inches = int(values[1])

    if values[2] == 'Meters':
        if event == 'Convert':
            meters = feet * 0.3048 + inches * 0.0254
            window["output"].update(value=f"You are {meters} m")
    elif values[2] == 'Centimeters':
        if event == 'Convert':
            meters = feet * 0.3048 + inches * 0.0254
            centimeters = meters * 100
            window["output"].update(value=f"You are {centimeters} cm")
    elif values[3] == 'Yards':
        if event == 'Convert':
            yards = feet * 0.333 + inches * 0.027
            window["output"].update(value=f"You are {yards} yards")
    elif event == Gui.WIN_CLOSED:
        break

window.close()