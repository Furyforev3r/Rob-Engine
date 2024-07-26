from RobEngine import RobEngine, Sprite, Input, locals


def main():
    renderer = RobEngine()
    renderer.initialize()

    input_handler = Input()

    test_sprite = Sprite("test_sprite.jpg", [10, 10])
    test_sprite.draw(renderer.screen)

    running = True
    while running:
        for event in renderer.event.get():
            if input_handler.is_pressed(locals.K_SPACE):
                print("Hi there!")
            if input_handler.was_pressed(locals.K_a, event):
                print("Hru?")
                print(type(event))
            if event.type == locals.QUIT:
                running = False

        renderer.update()


if __name__ == "__main__":
    main()
