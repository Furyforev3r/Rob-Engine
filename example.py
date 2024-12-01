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
    renderer = RobEngine(display_size=[640, 480])
    renderer.initialize()

    clock = renderer.clock

    input_handler = Input()
    physics = Physics()

    python_sprite = Sprite("python_icon.webp", [10, 10])
    python_sprite.resize((30, 30))

    sprite_group = SpriteGroup()
    solid_group = SolidGroup()

    character_moviment = EightDirections(
        character=python_sprite,
        input_handler=input_handler,
        physics=physics,
        solid_group=solid_group,
        speed=0.4
    )

    sprite_group.add_sprite(python_sprite)
    
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
        renderer.update(background_color=(0, 168, 26))


if __name__ == "__main__":
    main()
