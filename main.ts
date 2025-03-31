namespace SpriteKind {
    export const left = SpriteKind.create()
    export const right = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Projectile, SpriteKind.left, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    ball.setVelocity(100, 100)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.right, function on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    ball.setVelocity(randint(0, -100), randint(0, -100))
})
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
`, SpriteKind.left)
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
`, SpriteKind.right)
plate_left.setPosition(10, 60)
plate_right.setPosition(150, 60)
plate_left.setStayInScreen(true)
plate_right.setStayInScreen(true)
let ball = sprites.create(img`
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
`, SpriteKind.Projectile)
ball.setScale(.3, ScaleAnchor.Middle)
ball.setVelocity(100, 100)
ball.setStayInScreen(true)
ball.setBounceOnWall(true)
controller.moveSprite(plate_right, 0, 195)
game.onUpdate(function move_left_paddle() {
    if (controller.B.isPressed()) {
        plate_left.y -= 4.1
    } else if (controller.A.isPressed()) {
        plate_left.y += 4.1
    }
    
})
