@namespace
class SpriteKind:
    left = SpriteKind.create()
    right = SpriteKind.create()

def on_overlap(sprite, otherSprite):
    ball.set_velocity(100, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.left, on_overlap)

def on_overlap2(sprite, otherSprite):
    ball.set_velocity(randint(0, -100), randint(0, -100),)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.right, on_overlap2)

plate_left = sprites.create(img("""
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
"""), SpriteKind.left)

plate_right = sprites.create(img("""
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
"""), SpriteKind.right)

plate_left.set_position(10, 60)
plate_right.set_position(150, 60)
plate_left.set_stay_in_screen(True)
plate_right.set_stay_in_screen(True)

ball = sprites.create(img("""
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
    11111111111111111111
"""), SpriteKind.projectile)
ball.set_scale(.3, ScaleAnchor.MIDDLE)
ball.set_velocity(100, 100)
ball.set_stay_in_screen(True)
ball.set_bounce_on_wall(True)

controller.move_sprite(plate_right, 0, 195)


def move_left_paddle():
    if controller.B.is_pressed():
        plate_left.y -= 4.1
    elif controller.A.is_pressed():
        plate_left.y += 4.1

game.on_update(move_left_paddle)
