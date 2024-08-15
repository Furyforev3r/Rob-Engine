from RobEngine import RobEngine, Sprite, Input, locals, SpriteGroup, Physics


def main():
    renderer = RobEngine()
    renderer.initialize()

    input_handler = Input()

    test_sprite = Sprite("test_sprite.jpg", [10, 10])
    test_sprite.resize((300, 300))

    test_sprite_2 = Sprite("test_sprite.jpg", [1100, 600])
    test_sprite_2.resize((100, 100))

    sprite_group = SpriteGroup()
    sprite_group.add_sprite(test_sprite)
    sprite_group.add_sprite(test_sprite_2)

    physics = Physics()

    velocity_x = 0
    velocity_y = 0
    speed = 1

    running = True

    while running:
        for event in renderer.event.get():
            if input_handler.was_pressed(locals.K_a, event):
                print("Hi there!")
            if event.type == locals.QUIT:
                running = False

        velocity_x = 0
        velocity_y = 0

        if input_handler.is_pressed(locals.K_LEFT):
            velocity_x = -speed
        if input_handler.is_pressed(locals.K_RIGHT):
            velocity_x = speed
        if input_handler.is_pressed(locals.K_UP):
            velocity_y = -speed
        if input_handler.is_pressed(locals.K_DOWN):
            velocity_y = speed

        test_sprite.rect.x += velocity_x
        test_sprite.rect.y += velocity_y

        if physics.check_collisions(test_sprite, test_sprite_2):
            print("Collision detected!")
            test_sprite.rect.x -= velocity_x
            test_sprite.rect.y -= velocity_y

        sprite_group.update()
        sprite_group.SpriteGroup.draw(renderer.screen)
        renderer.update()


if __name__ == "__main__":
    main()
