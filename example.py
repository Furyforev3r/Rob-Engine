from RobEngine import (
    RobEngine,
    Sprite,
    Input,
    locals,
    SpriteGroup,
    Physics,
    Text,
    SolidGroup,
    EightDirections,
)


def main():
    renderer = RobEngine()
    renderer.initialize()

    clock = renderer.clock

    input_handler = Input()
    physics = Physics()

    test_sprite = Sprite("test_sprite.jpg", [10, 10])
    test_sprite.resize((300, 300))

    test_sprite_2 = Sprite("test_sprite.jpg", [1100, 600])
    test_sprite_2.resize((100, 100))

    sprite_group = SpriteGroup()
    solid_group = SolidGroup()

    character_moviment = EightDirections(
        character=test_sprite,
        input_handler=input_handler,
        physics=physics,
        solid_group=solid_group,
        speed=1.0,
        enabled=True,
    )

    sprite_group.add_sprite(test_sprite)
    sprite_group.add_sprite(test_sprite_2)
    solid_group.add_sprite(test_sprite_2)

    fps_text = Text(text="FPS: ...", font_size=30, color=(255, 255, 255))

    running = True
    max_fps = 1000

    while running:
        for event in renderer.event.get():
            if input_handler.was_pressed(locals.K_a, event):
                print("Hi there!")
            if event.type == locals.QUIT:
                running = False

        character_moviment.setup_moviment()

        fps = clock.get_fps()
        fps_text.update_text(f"FPS: {int(fps)}")

        clock.tick(max_fps)

        sprite_group.update()
        sprite_group.SpriteGroup.draw(renderer.screen)
        fps_text.draw(renderer.screen, (10, 10))
        renderer.update()


if __name__ == "__main__":
    main()
