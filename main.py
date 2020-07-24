def on_on_overlap(projectile, enemy):
    enemy.start_effect(effects.fire, 500)
    enemy.destroy()
    projectile.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_a_pressed():
    sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . 5 . . . .
                    . . 5 . . . . . . 1 2 5 . . . .
                    1 4 2 . . . . . . 1 . 5 4 . . .
                    1 . . . 2 2 2 2 2 . . . . . . .
                    . . . 2 2 4 4 4 2 2 2 2 2 2 2 .
                    . . 2 2 4 4 5 5 4 4 4 4 4 4 2 .
                    2 2 2 4 4 4 5 5 5 5 5 5 5 4 2 .
                    2 2 2 2 4 4 5 5 5 5 5 5 4 4 2 .
                    . . . 2 2 4 4 4 4 4 4 4 4 2 2 .
                    . 1 . . . 2 2 2 2 2 2 2 2 2 . .
                    . 1 . . . . . . 5 . . . . . . .
                    . 1 5 2 . . . . 2 4 1 . . . . .
                    . . . . . . . . . . 1 . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        hero,
        50,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(player2, enemy):
    info.change_life_by(-1)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

# Goes to the next level of our maps
def nextLevel():
    global enemy, currentLevel
    scene.set_tile_map(maps[currentLevel])
    scene.place_on_random_tile(hero, 7)
    for index in range(3):
        enemy = sprites.create(enemyImgs[currentLevel], SpriteKind.enemy)
        scene.place_on_random_tile(enemy, 1)
        enemy.set_velocity(50, 50)
        enemy.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
    # increase the level to prepare for next time when we call next level
    currentLevel = currentLevel + 1

def on_hit_tile(sprite):
    game.over(True)
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile)

def on_hit_tile2(sprite):
    nextLevel()
scene.on_hit_tile(SpriteKind.player, 2, on_hit_tile2)

enemy: Sprite = None
currentLevel = 0
enemyImgs: List[Image] = []
maps: List[Image] = []
hero: Sprite = None
hero = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(hero)
scene.camera_follow_sprite(hero)
scene.set_tile(15,
    img("""
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
    """),
    True)
scene.set_tile(14,
    img("""
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
    """),
    True)
scene.set_tile(1,
    img("""
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
    """),
    False)
scene.set_tile(2,
    img("""
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
    """),
    True)
scene.set_tile(7,
    img("""
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
    """),
    False)
scene.set_tile(5,
    img("""
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
    """),
    True)
# Define all my maps
maps = [img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """)]
# There are 3 levels, and we need 3 enemies
enemyImgs = [img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """)]
info.set_life(3)
nextLevel()