def make_readable(seconds):
    SS = seconds % 60
    MM = (seconds // 60) % 60
    HH = seconds // (60 * 60)

    HHMMSS = f'{HH:02d}:{MM:02d}:{SS:02d}'

    return HHMMSS


if __name__ == '__main__':
    pass
