import PySimpleGUI as sg


def make_win():
    layout = [[sg.Text('Enter something')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(40, 10), key='-OUTPUT-')]]
    return sg.Window('Window Title', layout, finalize=True)


def split_layout(layout):
    res = layout.split('\n')
    res = [list(x) for x in res]
    return res


def trans_string(layout, origin_map, input_str):
    res = ''
    for s in input_str:
        if s in origin_map.keys():
            xy = origin_map[s]
            res += layout[xy[0]][xy[1]]
        else:
            res += s
    return res


def trans_map(layout):
    res = {}
    i = 0
    for raw in layout:
        j = 0
        for val in raw:
            res[val] = [i, j]
            j += 1
        i += 1
    return res


def main():
    file_input_col = [sg.Text('変換用テキスト'),
                      sg.Input(key='INPUT_FILE', enable_events=True, size=(45, 1)),
                      sg.FileBrowse('参照', file_types=(('text', '*.txt')))]
    layout = [file_input_col]

    window_main = sg.Window('keyboard simulater', layout, finalize=True)
    window_sub = make_win()
    key_layout = split_layout('qwertyuiop\nasdfghjkl\nzxcvbnm,.')
    key_layout_origin = split_layout('qwertyuiop\nasdfghjkl\nzxcvbnm,.')
    key_layout_origin_map = trans_map(key_layout_origin)

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        if event == 'INPUT_FILE':
            if '.txt' in values['INPUT_FILE']:
                txt = open(values['INPUT_FILE'])
                key_layout = split_layout(txt.read())
        elif event == '-IN-':
            input_trans = trans_string(key_layout, key_layout_origin_map, values['-IN-'])
            window_sub['-OUTPUT-'].update(input_trans)
    window.close()


if __name__ == '__main__':
    main()
