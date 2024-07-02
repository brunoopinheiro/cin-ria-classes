def read_file() -> list[str]:
    try:
        filelines = []
        with open('input.txt', 'r') as file:
            lines = file.readlines()
            filelines = [line.strip('\n') for line in lines]
        return filelines
    except IOError as err:
        print('Error: ', err)


def main():
    elfs_catalog = read_file()
    most_c = 0
    elf = 0
    for cal in elfs_catalog:
        if cal == '':
            if most_c < elf:
                most_c = elf
            elf = 0
        else:
            elf += int(cal)

    print('Most Cal: ', most_c)


if __name__ == '__main__':
    main()
