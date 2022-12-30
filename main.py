import PySimpleGUI as Gui

label_feet = Gui.Text("Enter your feet:", key="feet")
input_feet = Gui.Input()
label_inches = Gui.Text("Enter your inches:", key="inches")
input_inches = Gui.Input()
conversion_rate = Gui.Combo(values=['Meters', 'Centimeters', 'Yards'])

convert_button = Gui.Button("Convert")
output_label = Gui.Text(key="output")

window = Gui.Window("Convertor", layout=[[label_feet, input_feet],
                                         [label_inches, input_inches],
                                         [conversion_rate],
                                         [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = int(values[0])
    inches = int(values[1])

    if values[2] == 'Meters':
        if event == 'Convert':
            meters = feet * 0.3048 + inches * 0.0254
            window["output"].update(value=f"{meters} m")
    elif values[2] == 'Centimeters':
        if event == 'Convert':
            meters = feet * 0.3048 + inches * 0.0254
            centimeters = meters * 100
            window["output"].update(value=f"{centimeters} cm")
    elif values[2] == 'Yards':
        if event == 'Convert':
            yards = feet * 0.333 + inches * 0.027
            window["output"].update(value=f"{yards} yards")

window.close()