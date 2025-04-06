@namespace
class SpriteKind:
    left = SpriteKind.create()
    right = SpriteKind.create()
    text = SpriteKind.create()
    collision1 = SpriteKind.create()
    collision2 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global score
    score += 1
    if score >= 10:
            game.set_game_over_message(True, "Left Side Wins!")
            game.game_over(True)
sprites.on_overlap(SpriteKind.collision1, SpriteKind.projectile, on_on_overlap)

def draw_text2(x: number, y: number, text2: str):
    global texty2
    texty2 = sprites.create(image.create(30, 10), SpriteKind.text)
    texty2.set_position(x, y)
    texty2.image.print(text2, 0, 0, 5)
    return texty2



def draw_text(x2: number, y2: number, text3: str):
    global texty
    texty = sprites.create(image.create(30, 10), SpriteKind.text)
    texty.set_position(x2, y2)
    texty.image.print(text3, 0, 0, 5)
    return texty

def on_on_overlap3(sprite3, otherSprite3):
    global score2
    score2 += 10
    if score2 >= 1:
        game.set_game_over_message(True, "Right Side Wins!")
        game.game_over(True)
sprites.on_overlap(SpriteKind.collision2, SpriteKind.projectile, on_on_overlap3)

def on_on_overlap2(paddle, ball):
    offset = ball.y - paddle.y
    normalized = offset / (paddle.height / 2)
    new_vy = normalized * 100
    new_vx = abs(ball.vx)
    ball.set_velocity(new_vx, new_vy)

def on_on_overlap4(paddle, ball):
    offset = ball.y - paddle.y
    normalized = offset / (paddle.height / 2)
    new_vy = normalized * 100
    new_vx = -abs(ball.vx)
    ball.set_velocity(new_vx, new_vy)

sprites.on_overlap(SpriteKind.left, SpriteKind.projectile, on_on_overlap2)
sprites.on_overlap(SpriteKind.right, SpriteKind.projectile, on_on_overlap4)



def do_something():
    global ball2
    ball2 = sprites.create(img("""
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
            """),
        SpriteKind.projectile)
    ball2.set_scale(0.3, ScaleAnchor.MIDDLE)
    ball2.set_velocity(100, 100)
    ball2.set_stay_in_screen(True)
    ball2.set_bounce_on_wall(True)
ball2: Sprite = None
score2 = 0
texty: Sprite = None
ball: Sprite = None
texty2: Sprite = None
score = 0

do_something()

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
"""),
    SpriteKind.left)

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
"""),
    SpriteKind.right)


collision_barr = sprites.create(img("""
        ....1111111.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1111111.....
        """),
    SpriteKind.collision1)
collision_barr.set_position(163, 70)


collision_barr2 = sprites.create(img("""
        ....1111111.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1fffff1.....
        ....1111111.....
        """),
    SpriteKind.collision2)


collision_barr2.set_position(-2, 70)
collision_barr.set_position(163, 70)
plate_left.set_position(10, 60)
plate_right.set_position(150, 60)

plate_left.set_stay_in_screen(True)
plate_right.set_stay_in_screen(True)

controller.move_sprite(plate_right, 0, 195)

score_label = draw_text(20, 10, "Left ")
score_amount = draw_text(20, 10, "" + str(score))
score_label2 = draw_text(125, 10, "Right: ")
score_amount2 = draw_text(163, 10, "" + str(score))

def on_on_update():
    if controller.B.is_pressed():
        plate_left.y -= 4.1
    elif controller.A.is_pressed():
        plate_left.y += 4.1
game.on_update(on_on_update)

def on_on_update2():
    global score_amount
    sprites.destroy(score_amount)
    score_amount = draw_text(50, 10, "" + str(score))
game.on_update(on_on_update2)

def on_on_update3():
    global score_amount2
    sprites.destroy(score_amount2)
    score_amount2 = draw_text(160, 10, "" + str(score2))
game.on_update(on_on_update3)
