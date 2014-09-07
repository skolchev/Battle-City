from Config import GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT, TERRAIN_WIDTH, TERRAIN_HEIGHT


def main():
    for row in range(0, int(GAME_FIELD_WIDTH / TERRAIN_WIDTH)):
        for col in range(0, int(GAME_FIELD_HEIGHT / TERRAIN_HEIGHT)):
            print('0', end='')
        print()


if __name__ == '__main__':
    main()