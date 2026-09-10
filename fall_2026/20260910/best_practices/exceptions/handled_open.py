def append_to_file(file_name):
    f = None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
    except PermissionError:
        print('Could not open ' + file_name)
    finally:
        return f

f = append_to_file('no_file.txt')
f = append_to_file('no_read_permission.txt')
