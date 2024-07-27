from RobEngine import RobEngine, Sprite, Input, locals
from RobEngine import SpriteGroup


def main():
    renderer = RobEngine()
    renderer.initialize()

    input_handler = Input()

    test_sprite = Sprite("test_sprite.jpg", [10, 10])
    test_sprite.draw(renderer.screen)

    sprite_group = SpriteGroup()

    sprite_group.add_sprite(test_sprite)

    running = True
    while running:
        for event in renderer.event.get():
            if input_handler.was_pressed(locals.K_a, event):
                print("Hi there!")
            if event.type == locals.QUIT:
                running = False

        if input_handler.is_pressed(locals.K_LEFT):
            test_sprite.rect.x -= 1
        if input_handler.is_pressed(locals.K_RIGHT):
            test_sprite.rect.x += 1
        if input_handler.is_pressed(locals.K_UP):
            test_sprite.rect.y -= 1
        if input_handler.is_pressed(locals.K_DOWN):
            test_sprite.rect.y += 1

        sprite_group.update()
        sprite_group.SpriteGroup.draw(renderer.screen)
        renderer.update()


if __name__ == "__main__":
    main()
