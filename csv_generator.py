import user_interface as ui

def create():
    path = 'file.csv'
    name = ui.get_name()
    fam = ui.get_last_name()
    tel = ui.get_phone()
    comm = ui.get_comment()
    with open(path, 'a') as data:
        data.write(f'{name};{fam};{tel};{comm}\n')
        data.write('')
    return path

#data = create()

#a = create() # костыль для самопроверки