from RobEngine import RobEngine, Sprite, QUIT


def main():
    renderer = RobEngine()
    renderer.initialize()

    test_sprite = Sprite("test_sprite.jpg", [10, 10])
    test_sprite.draw(renderer.screen)

    running = True
    while running:
        for event in renderer.event.get():
            if event.type == QUIT:
                running = False

        renderer.update()


if __name__ == "__main__":
    main()
