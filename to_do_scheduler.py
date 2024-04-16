import PySimpleGUI as sg

sg.theme('DarkGrey10')   # Add a little color for fun


def item_row(item_num):
    """
    A "Row" in this case is a Button with an "X", an Input element and a Text element showing the current counter
    :param item_num: The number to use in the tuple for each element
    :type:           int
    :return:         List
    """
    row =  [sg.pin(sg.Col([[sg.T(f'{item_num+1}.', k=('-STATUS-', item_num)),
                            sg.B("x",size=2, border_width=1, button_color=(sg.theme_text_color(), sg.theme_background_color()), k=('-DEL-', item_num), tooltip='Delete this item'),
                            sg.In(size=(20,1), k=('-DESC-'))]], k=('-ROW-', item_num)))]
    return row


def make_window():
    
    layout = [  [sg.Text('Add tasks to complete during the day', font='_ 15')],
                [sg.Col([item_row(0)], k='-TRACKING SECTION-')],
                [sg.pin(sg.Text(size=(35,1), font='_ 8', k='-REFRESHED-',))],
                [sg.T("X", enable_events=True, k='Exit', tooltip='Exit Application'), sg.T('Refresh', enable_events=True, k='Refresh',  tooltip='Save Changes & Refresh'), sg.T('+', enable_events=True, k='Add Item', tooltip='Add Another Item')]]

    right_click_menu = [[''], ['Add Item',  'Edit Me', 'Version']]


    window = sg.Window('Window Title', layout,return_keyboard_events=True,finalize=True,  right_click_menu=right_click_menu, use_default_focus=False, font='_ 15', metadata=0,margins=(0,0), no_titlebar=True, grab_anywhere=True, alpha_channel=.75, use_ttk_buttons=True, location=(1185,655))
    window.bind("<Return>","_Enter")
    return window


def main():
    window = make_window()
    last_desc_event = '-DESC-'
    while True:
        event, values = window.read()     # wake every hour
        print(event)
        print(type(event))

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Add Item' or event=="_Enter":
            window.metadata += 1
            window.extend_layout(window['-TRACKING SECTION-'], [item_row(window.metadata)])
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)
        elif event[0] == '-DEL-':
                window[('-ROW-', event[1])].update(visible=False)
    window.close()
    
    
if __name__ == "__main__":
    #sg.theme_previewer()
    main()
    

    
