scene.onHitTile(SpriteKind.Player, 5, function (sprite) {
    game.over(true)
})
// Goes to the next level of our maps
function nextLevel () {
    scene.setTileMap(maps[currentLevel])
    scene.placeOnRandomTile(hero, 7)

    for (let index = 0; index < 3; index++) {
    
        let enemy = sprites.create(enemyImgs[currentLevel], SpriteKind.Enemy)
    }
    // increase the level to prepare for next time when we
    // call next level
    currentLevel = currentLevel + 1
}
scene.onHitTile(SpriteKind.Player, 2, function (sprite) {
    nextLevel()
})
let currentLevel = 0
let maps: Image[] = []
let hero: Sprite = null
hero = sprites.create(img`
    . . . . f f f f . . . .
    . . f f e e e e f f . .
    . f f e e e e e e f f .
    f f f f 4 e e e f f f f
    f f f 4 4 4 e e f f f f
    f f f 4 4 4 4 e e f f f
    f 4 e 4 4 4 4 4 4 e 4 f
    f 4 4 f f 4 4 f f 4 4 f
    f e 4 d d d d d d 4 e f
    . f e d d b b d d e f .
    . f f e 4 4 4 4 e f f .
    e 4 f b 1 1 1 1 b f 4 e
    4 d f 1 1 1 1 1 1 f d 4
    4 4 f 6 6 6 6 6 6 f 4 4
    . . . f f f f f f . . .
    . . . f f . . f f . . .
`, SpriteKind.Player)
controller.moveSprite(hero)
scene.cameraFollowSprite(hero)
scene.setTile(15, img`
    . . . . . c c b b b . . . . . .
    . . . . c b d d d d b . . . . .
    . . . . c d d d d d d b b . . .
    . . . . c d d d d d d d d b . .
    . . . c b b d d d d d d d b . .
    . . . c b b d d d d d d d b . .
    . c c c c b b b b d d d b b b .
    . c d d b c b b b b b b b b d b
    c b b d d d b b b b b d d b d b
    c c b b d d d d d d d b b b d c
    c b c c c b b b b b b b d d c c
    c c b b c c c c b d d d b c c b
    . c c c c c c c c c c c b b b b
    . . c c c c c b b b b b b b c .
    . . . . . . c c b b b b c c . .
    . . . . . . . . c c c c . . . .
`, true)
scene.setTile(14, img`
    . . b d b . . . . . b b b b . .
    . c b d d b . . . b b d d d b .
    . b c c b . . . b c d d d d b .
    . . . . . . b b c c b d b b b .
    . . . . . b d d b c c b b b c .
    . . b b b c d d b b c c c c . .
    . b d d d b c b b c . . . . . .
    c b d d d d c c c c . b b b . .
    c c b b b b c c c . b d d d b .
    . c c c b b . . b c b b d d b b
    . b b . . . . . b c c b b b b .
    b d d b b . . . . . c c c b . .
    b b d d b c . . b b b b b b b .
    . b c c c b . b d d d b b c b .
    . . . . . . b d d d b c c b . .
    . . . . . . b b b c c c b . . .
`, true)
scene.setTile(1, img`
    7 7 7 7 5 7 7 7 7 7 7 7 7 7 7 7
    7 7 5 7 5 5 7 7 7 7 7 7 7 7 7 7
    7 6 5 5 7 5 7 5 5 7 7 7 7 7 7 7
    7 7 6 5 7 7 5 5 6 7 7 7 7 7 7 7
    7 7 7 6 7 7 5 6 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 5 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 5 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 6 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 5 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 5 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 6 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 5 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
`, false)
scene.setTile(2, img`
    c c c c c c c c c c c c c c c c
    c c c c c c c c c c c b b b b c
    c c c c c c c c c c c b b b b c
    c c c c c c c c c c c b b b b c
    c c c c c c b b b b c b b b b c
    c c c c c c b b b b c b b b b c
    c c c c c c b b b b c b b b b c
    c c c c c c b b b b c b b b b c
    c b b b b c b b b b c b b b b c
    c b b b b c b b b b c d d d d c
    c b b b b c b b b b b b b b b c
    c b b b b c d d d d b b b b b c
    c b b b b c b b b b b b b b b c
    c b b b b b b b b b b b b b b c
    c d d d d b b b b b b b b b b c
    c b b b b b b b b b b b b b b c
`, true)
scene.setTile(7, img`
    7 6 7 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 6 6 6 6 7 6 6 6 6 6 6 6 6 6 6
    6 6 6 7 6 7 7 6 6 6 6 6 7 6 6 6
    6 6 8 7 7 6 7 6 7 7 6 6 6 6 6 6
    6 6 6 8 7 6 6 7 7 8 6 6 6 6 6 6
    6 6 6 6 8 6 6 7 8 6 6 6 6 6 6 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 6 7 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 6 6 6 6 6 6 6 6 6 6 7 7 6 6 6
    6 6 6 6 6 6 6 6 6 6 7 7 8 6 6 6
    6 6 6 6 6 6 6 6 7 7 6 8 6 6 6 6
    6 6 6 6 6 6 6 6 6 7 7 6 6 6 6 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7
    6 6 7 6 6 6 6 6 6 6 6 6 6 6 6 7
`, false)
scene.setTile(5, img`
    . . b b b b b b b b b b b b . .
    . b e 4 4 4 4 4 4 4 4 4 4 e b .
    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b
    b e e 4 4 4 4 4 4 4 4 4 4 e e b
    b e e e e e e e e e e e e e e b
    b e e e e e e e e e e e e e e b
    b b b b b b b d d b b b b b b b
    c b b b b b b c c b b b b b b c
    c c c c c c b c c b c c c c c c
    b e e e e e c b b c e e e e e b
    b e e e e e e e e e e e e e e b
    b c e e e e e e e e e e e e c b
    b b b b b b b b b b b b b b b b
    . b b . . . . . . . . . . b b .
`, true)
// Define all my maps
maps = [img`
    7 f f f f f f 1 1 1 1 e 1 1 1 1
    1 1 1 1 1 1 1 f f f f e f 1 1 1
    1 1 1 1 1 1 1 1 1 1 1 e 1 1 1 1
    f f 1 e 1 1 1 1 1 1 1 1 1 1 1 e
    1 1 e 1 1 1 1 1 1 1 1 1 f f e 1
    1 e f f f 1 1 1 1 1 f f 1 e 1 1
    1 e 1 1 1 f f 1 1 f 1 1 e 1 1 1
    e 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    1 1 1 f f 1 1 1 1 1 1 1 f f 1 1
    1 f f 1 1 1 1 1 e e e e e 1 1 1
    f 1 1 1 1 e 1 1 1 1 1 1 1 1 1 1
    1 1 1 e 1 1 1 1 f f 1 1 1 1 1 1
    1 1 e 1 1 1 e f 1 1 1 e f 1 1 1
    1 e f 1 1 1 1 e e e 1 e 1 f 1 1
    1 1 f f f 1 1 1 1 1 e e e 1 f 1
    1 1 1 1 1 f f 1 1 1 1 1 1 1 1 2
`, img`
    7 1 1 f 1 1 1 1 1 1 1 1 f 1 1 1
    1 1 1 f 1 1 1 1 1 1 1 1 f 1 1 1
    1 1 1 f 1 1 1 1 1 e e e f 1 1 1
    1 1 1 f 1 1 1 1 1 1 1 1 f 1 1 1
    1 1 1 f 1 1 1 1 f 1 1 1 f 1 1 1
    1 1 1 e 1 1 1 1 f 1 1 1 e 1 f 1
    1 1 1 f 1 1 1 f f 1 1 1 f 1 f 1
    1 1 1 e 1 1 1 f f 1 1 1 f 1 f 1
    1 1 1 f 1 1 1 1 f 1 1 1 1 1 f 1
    1 1 1 e 1 1 1 1 f e 1 1 1 1 e 1
    1 1 1 e 1 1 1 1 f 1 1 1 1 1 e 1
    1 1 1 e 1 1 1 1 f 1 1 f f f f 1
    1 1 f 1 1 1 1 1 f 1 1 f 1 1 f 1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 f 1
    1 1 1 1 1 1 1 1 1 e 1 1 1 1 f 1
    1 1 1 e e e 1 1 1 1 1 1 1 1 f 2
`, img`
    7 1 1 1 1 1 1 1 1 1 1 1 1 f f f
    1 1 1 1 1 1 1 1 1 1 1 1 1 f 1 f
    1 1 1 1 1 1 1 1 1 1 1 1 1 e 1 f
    1 1 1 1 1 1 1 1 1 1 1 1 1 f 1 f
    1 1 1 1 1 f f f f f e f 1 f e f
    1 1 1 1 1 f 5 1 1 1 1 f 1 1 1 1
    1 1 1 1 1 f 1 1 1 1 1 f 1 1 1 1
    e e e 1 1 f 1 1 1 1 1 f 1 1 1 1
    1 1 1 e 1 e 1 1 1 1 1 f 1 1 1 1
    1 1 1 e 1 f 1 1 1 1 1 1 1 1 1 1
    1 1 1 e 1 f f f f f f 1 1 1 1 1
    1 1 1 e 1 1 1 1 1 1 1 1 1 1 1 1
    e e e 1 1 1 1 1 1 1 1 e e e e f
    1 1 1 1 1 1 1 1 1 1 1 e 1 1 1 e
    1 1 1 1 1 1 1 1 1 1 1 f 1 1 1 e
    1 1 1 1 1 1 1 1 1 1 1 e e e f e
`]
nextLevel()
// There are 3 levels, and we need 3 enemies
let enemyImgs = [
    img`
        . . . . . f f f f f . . . . . .
        . . . . f e e e e e f . . . . .
        . . . f d d d d d d e f . . . .
        . . f d f f d d f f d f f . . .
        . c d d d e e d d d d e d f . .
        . c d c d d d d c d d e f f . .
        . c d d c c c c d d d e f f f f
        . . c d d d d d d d e f f b d f
        . . . c d d d d e e f f f d d f
        . . . . f f f e e f e e e f f f
        . . . . f e e e e e e e f f f .
        . . . f e e e e e e f f f e f .
        . . f f e e e e f f f f f e f .
        . f b d f e e f b b f f f e f .
        . f d d f f f f d d b f f f f .
        . f f f f f f f f f f f f f . .
    `,
    img`
        . . . . . c c c c c c c . . . .
        . . . . c 6 7 7 7 7 7 6 c . . .
        . . . c 7 c 6 6 6 6 c 7 6 c . .
        . . c 6 7 6 f 6 6 f 6 7 7 c . .
        . . c 7 7 7 7 7 7 7 7 7 7 c . .
        . . f 7 8 1 f f 1 6 7 7 7 f . .
        . . f 6 f 1 f f 1 f 7 7 7 f . .
        . . . f f 2 2 2 2 f 7 7 6 f . .
        . . c c f 2 2 2 2 7 7 6 f c . .
        . c 7 7 7 7 7 7 7 7 c c 7 7 c .
        c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c
        f 1 1 1 1 1 7 6 f c c 6 6 6 c c
        f 1 1 1 1 1 1 6 6 c 6 6 6 c . .
        f 6 1 1 1 1 1 6 6 6 6 6 6 c . .
        . f 6 1 1 1 1 1 6 6 6 6 c . . .
        . . f f c c c c c c c c . . . .
    `,
    img`
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . f f f f . . . . . . . . . .
        . . . . . . . . f f 1 1 1 1 f f . . . . . . . .
        . . . . . . . f b 1 1 1 1 1 1 b f . . . . . . .
        . . . . . . . f 1 1 1 1 1 1 1 1 f . . . . . . .
        . . . . . . f d 1 1 1 1 1 1 1 1 d f . . . . . .
        . . . . 7 . f d 1 1 1 1 1 1 1 1 d f . . . . . .
        . . . 7 . . f d 1 1 1 1 1 1 1 1 d f . . . . . .
        . . . 7 . . f d 1 1 1 1 1 1 1 1 d f . . . . . .
        . . . 7 . . f d d d 1 1 1 1 d d d f f . . . . .
        . . . 7 7 . f b d b f d d f b d b f c f . . . .
        . . . 7 7 7 f c d c f 1 1 f c d c f b f . . . .
        . . . . 7 7 f f f b d b 1 b d f f c f . . . . .
        . . . . f c b 1 b c f f f f f f . . . . . . . .
        . . . . f 1 c 1 c 1 f f f f f f . . . . . . . .
        . . . . f d f d f d f f f f f . . . . . . . . .
        . . . . . f . f . f . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
    `
]