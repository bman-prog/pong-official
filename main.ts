let plate_left = sprites.create(img`
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
`, SpriteKind.Player)
let plate_right = sprites.create(img`
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
`, SpriteKind.Player)
plate_left.setPosition(10, 60)
plate_right.setPosition(150, 60)
plate_left.setStayInScreen(true)
plate_right.setStayInScreen(true)
controller.moveSprite(plate_right, 0, 195)
game.onUpdate(function move_left_paddle() {
    if (controller.B.isPressed()) {
        plate_left.y -= 4.1
    } else if (controller.A.isPressed()) {
        plate_left.y += 4.1
    }
    
})
