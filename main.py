@namespace
class SpriteKind:
    Diamond = SpriteKind.create()

def on_life_zero():
    sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)),
        effects.fire,
        500)
mp.on_life_zero(on_life_zero)

def on_player3_button_b_pressed():
    global Proyectile3
    Proyectile3 = sprites.create_projectile_from_sprite(assets.image("""
            -
            """),
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)),
        500,
        0)
    animation.run_image_animation(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)),
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c c c . . . .
                . . . . . . c c 5 5 5 5 c c . .
                . . . . . c 5 5 5 5 5 5 5 5 c .
                . . . . c 5 5 5 f 1 5 5 5 5 5 c
                . . . c 5 5 5 5 f f 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 5 5 5 5 5 c
                . . c d 5 5 5 5 5 5 b 1 b b c c
                . . c d d d 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 5 5 5 5 5 b .
                . c c d d d d b 5 5 c b b c . .
                c d c d d d d b b 5 5 c b b c .
                c d d d d d d d d c c c c c c .
                . c d d d b 5 5 d c c c c . . .
                . . c c c b 5 5 b c c c c c . .
                . . . . c b 5 5 d c b b b c . .
                """),
            img("""
                . . . . . . . c c c c c . . . .
                . . . . . . c 5 5 5 5 5 c c . .
                . . . . . c 5 5 f 1 5 5 5 5 c .
                . . . . c 5 5 5 f f 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 b 1 b b c c
                . . c d 5 5 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 b 5 5 5 5 c .
                . . c d d d d b 5 5 c b b c . .
                c c c d d d d b b 5 5 c b b c .
                c d d d d d d d d c c c c c c .
                . c d d d b 5 5 b c c c . . . .
                . . c c c b b 5 5 d c . . . . .
                . . . . . c c c c c c c . . . .
                . . . . . . . c b b b c . . . .
                """),
            img("""
                . . . . . . . c c c c c . . . .
                . . . . . . c 5 5 5 5 5 c c . .
                . . . . . c 5 5 f 1 5 5 5 5 c .
                . . . . c 5 5 5 f f 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 b 1 b b c c
                . . c d 5 5 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 5 5 5 5 5 5 c
                . . c d d d 5 5 5 b 5 5 5 5 c .
                . . c d d d d b 5 5 c b b c . .
                c c c d d d d b b 5 5 c b b c .
                c d d d d d d d d c c c c c c .
                . c c d d d b 5 5 b c c . . . .
                . . . c c c b b 5 5 d c . . . .
                . . . . . c c c c c c c . . . .
                . . . . . . . c b b b c . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c c c . . . .
                . . . . . . c c 5 5 5 5 c c . .
                . . . . . c 5 5 5 5 5 5 5 5 c .
                . . . . c 5 5 5 f 1 5 5 5 5 5 c
                . . . c 5 5 5 5 f f 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 5 5 5 5 5 c
                . . c d 5 5 5 5 5 5 b 1 b b c c
                . . c d d d 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 5 5 5 5 5 b .
                . . c d d d d b 5 5 c b b c . .
                c c c d d d d b b 5 5 c b b c .
                c d d d d d d d d c c c c c c .
                . c c d d b 5 5 d c c c c . . .
                . . . c c b 5 5 c c c b b c . .
                . . . . . c 5 5 d c c c c c . .
                """),
            img("""
                . . . . . . . c c c c c . . . .
                . . . . . . c 5 5 5 5 5 c c . .
                . . . . . c 5 5 f 1 5 5 5 5 c .
                . . . . c 5 5 5 f f 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 b 1 b b c c
                . . c d 5 5 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 5 5 5 5 5 5 c
                . . c d d d 5 5 5 b 5 5 5 5 c .
                . . c d d d d b 5 5 c b b c . .
                . c c d d d d b b 5 5 c b b c .
                c c d d d d d d b b c c c c c .
                c d d d d d 5 5 b 5 5 c c . . .
                c c c c c c b b 5 5 b c . . . .
                . . . . . . c c c c c c . . . .
                . . . . . . c b b b c . . . . .
                """)],
        100,
        False)
    pause(200)
    sprites.destroy(Proyectile3)
controller.player3.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player3_button_b_pressed)

def on_player2_button_b_pressed():
    global Proyectile2
    Proyectile2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . 2 2 2 . . . 2 2 2 2 . .
            . . . 2 2 2 2 2 . 2 2 2 2 2 2 .
            . . 2 2 2 2 2 2 2 2 2 2 2 2 2 .
            . . 2 2 2 2 2 2 2 2 2 2 2 2 2 .
            . . 2 2 2 2 2 2 2 2 2 2 2 2 2 .
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
            . . . 2 2 2 2 2 2 2 2 2 2 2 . .
            . . . . 2 2 2 2 2 2 2 2 2 . . .
            . . . . . 2 2 2 2 2 2 2 . . . .
            . . . . . 2 2 2 2 2 2 . . . . .
            . . . . . . 2 2 2 2 . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)),
        50,
        50)
    animation.run_image_animation(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)),
        [img("""
                . . . . . f f 4 4 f f . . . . .
                . . . . f 5 4 5 5 4 5 f . . . .
                . . . f e 4 5 5 5 5 4 e f . . .
                . . f b 3 e 4 4 4 4 e 3 b f . .
                . . f 3 3 3 3 3 3 3 3 3 3 f . .
                . f 3 3 e b 3 e e 3 b e 3 3 f .
                . f 3 3 f f e e e e f f 3 3 f .
                . f b b f b f e e f b f b b f .
                . f b b e 1 f 4 4 f 1 e b b f .
                f f b b f 4 4 4 4 4 4 f b b f f
                f b b f f f e e e e f f f b b f
                . f e e f b d d d d b f e e f .
                . . e 4 c d d d d d d c 4 e . .
                . . e f b d b d b d b b f e . .
                . . . f f 1 d 1 d 1 d f f . . .
                . . . . . f f b b f f . . . . .
                """),
            img("""
                . . . . . . . f f . . . . . . .
                . . . . . f f 4 4 f f . . . . .
                . . . . f 5 4 5 5 4 5 f . . . .
                . . . f e 4 5 5 5 5 4 e f . . .
                . . f b 3 e 4 4 4 4 e 3 b f . .
                . f e 3 3 3 3 3 3 3 3 3 3 e f .
                . f 3 3 e b 3 e e 3 b e 3 3 f .
                . f b 3 f f e e e e f f 3 b f .
                f f b b f b f e e f b f b b f f
                f b b b e 1 f 4 4 f 1 e b b b f
                . f b b e e 4 4 4 4 4 f b b f .
                . . f 4 4 4 e d d d b f e f . .
                . . f e 4 4 e d d d d c 4 e . .
                . . . f e e d d b d b b f e . .
                . . . f f 1 d 1 d 1 1 f f . . .
                . . . . . f f f b b f . . . . .
                """),
            img("""
                . . . . . f f 4 4 f f . . . . .
                . . . . f 5 4 5 5 4 5 f . . . .
                . . . f e 4 5 5 5 5 4 e f . . .
                . . f b 3 e 4 4 4 4 e 3 b f . .
                . . f 3 3 3 3 3 3 3 3 3 3 f . .
                . f 3 3 e b 3 e e 3 b e 3 3 f .
                . f 3 3 f f e e e e f f 3 3 f .
                . f b b f b f e e f b f b b f .
                . f b b e 1 f 4 4 f 1 e b b f .
                f f b b f 4 4 4 4 4 4 f b b f f
                f b b f f f e e e e f f f b b f
                . f e e f b d d d d b f e e f .
                . . e 4 c d d d d d d c 4 e . .
                . . e f b d b d b d b b f e . .
                . . . f f 1 d 1 d 1 d f f . . .
                . . . . . f f b b f f . . . . .
                """),
            img("""
                . . . . . . . f f . . . . . . .
                . . . . . f f 4 4 f f . . . . .
                . . . . f 5 4 5 5 4 5 f . . . .
                . . . f e 4 5 5 5 5 4 e f . . .
                . . f b 3 e 4 4 4 4 e 3 b f . .
                . f e 3 3 3 3 3 3 3 3 3 3 e f .
                . f 3 3 e b 3 e e 3 b e 3 3 f .
                . f b 3 f f e e e e f f 3 b f .
                f f b b f b f e e f b f b b f f
                f b b b e 1 f 4 4 f 1 e b b b f
                . f b b f 4 4 4 4 4 e e b b f .
                . . f e f b d d d e 4 4 4 f . .
                . . e 4 c d d d d e 4 4 e f . .
                . . e f b b d b d d e e f . . .
                . . . f f 1 1 d 1 d 1 f f . . .
                . . . . . f b b f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . 2 2 2 2 . 2 2 2 . . . .
                . . . 2 2 2 2 2 2 2 2 2 2 . . .
                . . 2 2 2 2 2 2 2 2 1 2 2 2 . .
                . . 2 2 2 2 2 2 2 2 2 1 2 2 . .
                . . 2 2 2 2 2 2 2 2 2 1 2 2 . .
                . . 2 2 2 2 2 2 2 2 2 1 2 2 . .
                . . 2 2 2 2 2 2 2 2 2 1 2 . . .
                . . . 2 2 2 2 2 2 2 1 2 . . . .
                . . . . 2 2 2 2 2 1 2 2 . . . .
                . . . . . 2 2 2 2 2 2 . . . . .
                . . . . . . 2 2 2 2 . . . . . .
                . . . . . . 2 2 2 . . . . . . .
                . . . . . . . 2 . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . 5 . 5 . . . . . . .
                . . . . . f 5 5 5 f f . . . . .
                . . . . f 1 5 2 5 1 6 f . . . .
                . . . f 1 6 6 6 6 6 1 6 f . . .
                . . . f 6 6 f f f f 6 1 f . . .
                . . . f 6 f f d d f f 6 f . . .
                . . f 6 f d f d d f d f 6 f . .
                . . f 6 f d 3 d d 3 d f 6 f . .
                . . f 6 6 f d d d d f 6 6 f . .
                . f 6 6 f 3 f f f f 3 f 6 6 f .
                . . f f d 3 5 3 3 5 3 d f f . .
                . . f d d f 3 5 5 3 f d d f . .
                . . . f f 3 3 3 3 3 3 f f . . .
                . . . f 3 3 5 3 3 5 3 3 f . . .
                . . . f f f f f f f f f f . . .
                . . . . . f f . . f f . . . . .
                """)],
        500,
        False)
    pause(100)
    sprites.destroy(Proyectile2)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_overlap_tile():
    info.player4.change_life_by(-1)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)).set_position(114, 24)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile)

def on_player4_button_b_pressed():
    global Proyectile4
    Proyectile4 = sprites.create_projectile_from_sprite(img("""
            5 5 5 5 . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            5 5 5 5 . a a a a a a a . . . .
            . . . . 5 a a a a a a a a . . .
            5 5 5 a a a a a a a a a a a . .
            . . 5 a a a a a a a a a a a a .
            . . a a a a a a a a a a a a a .
            5 5 a a a a a a a a a a a a a .
            . . a a a a a a a a a a a a a .
            5 . a a a a a a a a a a a a a .
            . 5 a a a a a a a a a a a a a .
            5 5 5 a a a a a a a a a a a a .
            5 . . a a a a a a a a a a a . .
            . . 5 5 a a a a a a a a a . . .
            5 5 5 . . a a a a a a a . . . .
            . . . . . . . . . . . . . . . .
            """),
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)),
        50,
        50)
    animation.run_image_animation(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)),
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f e e e b b b b f f . . .
                . . . e b b e e e e f b b e . .
                . . . e b b e b b 5 5 f e e . .
                . . . . c e e 5 5 5 5 5 f . . .
                . . . . . f f f f f f f . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . a a a a a a a . . . . .
                . . . a a a a a a a a a . . . .
                5 5 5 5 a a a a a a a a . . . .
                5 5 5 5 5 5 a a a a a a . . . .
                . . . a a a a a a a a a . . . .
                . . . a a a a a a a a a . . . .
                5 5 5 5 5 5 a a a a a a . . . .
                . . . a a a a a a a a a . . . .
                . 5 5 5 5 5 a a a a a . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . a a a a a a a . . . . .
                . . . a a 5 5 5 a a a a . . . .
                5 5 5 5 5 5 a a a a a a . . . .
                5 5 5 5 5 5 a a a a a a . . . .
                . 5 5 5 5 a a a a a a a . . . .
                . . . 5 a 5 5 5 5 a a a . . . .
                5 5 5 5 5 5 a a a a a a . . . .
                . 5 5 5 5 5 5 5 5 a a a . . . .
                . 5 5 5 5 5 a a a a a . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . 5 5 5 5 5 5 5 5 5 . . . .
                5 5 5 5 5 5 5 5 5 5 5 5 . . . .
                5 5 5 5 5 5 5 5 5 5 5 5 . . . .
                . 5 5 5 5 5 5 5 5 5 5 5 . . . .
                . . . 5 5 5 5 5 5 5 5 5 . . . .
                5 5 5 5 5 5 5 5 5 5 5 5 . . . .
                . 5 5 5 5 5 5 5 5 5 5 5 . . . .
                . 5 5 5 5 5 5 5 5 5 5 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . c c c . . . . . .
                . . . . . . c b 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b b b f f . . .
                . . . e e f e e e e f e e . . .
                . . e b c b 5 b b 5 b f b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """)],
        100,
        False)
    pause(100)
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player4_button_b_pressed)

def on_overlap_tile2():
    info.player1.change_life_by(-1)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).set_position(114, 24)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile2)

def on_life_zero2():
    sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)),
        effects.fire,
        500)
mp.on_life_zero(on_life_zero2)

def on_on_overlap():
    mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.FOUR),
        MultiplayerState.life,
        -1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_player2_button_a_pressed():
    if mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).vx == 0:
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).y += -19
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_overlap_tile3():
    info.player3.change_life_by(-1)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).set_position(114, 24)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile3)

def on_life_zero3():
    sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)),
        effects.fire,
        500)
mp.on_life_zero(on_life_zero3)

def on_overlap_tile4():
    info.player2.change_life_by(-1)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).set_position(114, 24)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile4)

def on_on_overlap2():
    mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.TWO),
        MultiplayerState.life,
        -1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap2)

def on_player4_button_a_pressed():
    if mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)).vx == 0:
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)).y += -19
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player1_button_a_pressed():
    if mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).vx == 0:
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).y += -19
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_on_overlap3():
    mp.change_player_state_by(mp.player_selector(mp.PlayerNumber.THREE),
        MultiplayerState.life,
        -1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap3)

def on_player3_button_a_pressed():
    if mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).vx == 0:
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).y += -19
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_player1_button_b_pressed():
    global Proyectile1
    Proyectile1 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . 1 b . . . . .
            . . . . . . . . 1 . b . 5 . . .
            . . . . . . . . . . b . 5 5 . .
            . . . . . . . . . . b . . 5 5 .
            . . . . . . . . . . b . 5 . 5 .
            . . . . . . . . . . b . . 5 . .
            . . . . . . . . . 1 1 . . . 5 .
            . . . . . . . . 1 b b . 5 . . .
            . . . . . . . . . b . . 5 . . 5
            . . . . . . . . 1 b . . 5 5 5 5
            . . . . . . . . b . . . 5 . . .
            . . . . . . . . . . . 5 . 5 . .
            . . . . . . . . . . . 5 . . . .
            . . . . . . . 5 . . . . 5 . . 5
            . . . . . . . 5 5 . . . 5 5 . .
            . . . . . . . . . . . . . . . .
            """),
        mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)),
        50,
        0)
    animation.run_image_animation(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)),
        [img("""
                ........................
                ....ffffff..............
                ..ffeeeef2f.............
                .ffeeeef222f............
                .feeeffeeeef...cc.......
                .ffffee2222ef.cdc.......
                .fe222ffffe2fcddc.......
                fffffffeeeffcddc........
                ffe44ebf44ecddc.........
                fee4d41fddecdc..........
                .feee4dddedccc..........
                ..ffee44e4dde...........
                ...f222244ee............
                ...f2222e2f.............
                ...f444455f.............
                ....ffffff..............
                .....fff................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ........................
                .......fff..............
                ....fffff2f.............
                ..ffeeeee22ff...........
                .ffeeeeee222ff..........
                .feeeefffeeeef..........
                .fffffeee2222ef.........
                fffe222fffffe2f.........
                fffffffffeeefff.....cc..
                fefe44ebbf44eef...ccdc..
                .fee4d4bbfddef..ccddcc..
                ..feee4dddddfeecdddc....
                ...f2222222eeddcdcc.....
                ...f444445e44ddccc......
                ...ffffffffeeee.........
                ...fff...ff.............
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                .......ff...............
                ....ffff2ff.............
                ..ffeeeef2ff............
                .ffeeeeef22ff...........
                .feeeeffeeeef...........
                .fffffee2222ef..........
                fffe222ffffe2f..........
                ffffffffeeefff..........
                fefe44ebf44eef..........
                .fee4d4bfddef...........
                ..feee4dddee.c..........
                ...f2222eeddeccccccc....
                ...f444e44ddecddddd.....
                ...fffffeeee.ccccc......
                ..ffffffff...c..........
                ..fff..ff...............
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ....ffffff..............
                ..ffeeeef2f.............
                .ffeeeef222f............
                .feeeffeeeef............
                .ffffee2222ef...........
                .fe222ffffe2f...........
                fffffffeeefff...........
                ffe44ebf44eef...........
                fee4d41fddef............
                .feee4ddddf.............
                ..fdde444ef.............
                ..fdde22ccc.............
                ...eef22cdc.............
                ...f4444cddc............
                ....fffffcddc...........
                .....fff..cddc..........
                ...........cdc..........
                ............cc..........
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ......ffff..............
                ....fff22fff............
                ...fff2222fff...........
                ..fffeeeeeefff..........
                ..ffe222222eef..........
                ..fe2ffffff2ef..........
                ..ffffeeeeffff..........
                .ffefbf44fbfeff.........
                .fee41fddf14eef.........
                ..feeddddddeef..........
                ...fee4444eef...........
                ..e4f222222f4e..........
                ..4df222222fd4..........
                ..44f445544f44..........
                .....ffffff.............
                .....ff..ff.............
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """)],
        100,
        False)
    pause(100)
    sprites.destroy(Proyectile1)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_controller_connected(player2):
    global Players
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
        sprites.create(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            SpriteKind.player))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
        sprites.create(img("""
                . . . . . . 5 . 5 . . . . . . .
                . . . . . f 5 5 5 f f . . . . .
                . . . . f 1 5 2 5 1 6 f . . . .
                . . . f 1 6 6 6 6 6 1 6 f . . .
                . . . f 6 6 f f f f 6 1 f . . .
                . . . f 6 f f d d f f 6 f . . .
                . . f 6 f d f d d f d f 6 f . .
                . . f 6 f d 3 d d 3 d f 6 f . .
                . . f 6 6 f d d d d f 6 6 f . .
                . f 6 6 f 3 f f f f 3 f 6 6 f .
                . . f f d 3 5 3 3 5 3 d f f . .
                . . f d d f 3 5 5 3 f d d f . .
                . . . f f 3 3 3 3 3 3 f f . . .
                . . . f 3 3 5 3 3 5 3 3 f . . .
                . . . f f f f f f f f f f . . .
                . . . . . f f . . f f . . . . .
                """),
            SpriteKind.player))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
        sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c c c . . . .
                . . . . . . c c 5 5 5 5 c c . .
                . . . . . c 5 5 5 5 5 5 5 5 c .
                . . . . c 5 5 5 f 1 5 5 5 5 5 c
                . . . c 5 5 5 5 f f 5 5 5 5 5 c
                . . . c 5 5 5 5 5 5 5 5 5 5 5 c
                . . c d 5 5 5 5 5 5 b 1 b b c c
                . . c d d d 5 5 5 5 5 3 3 3 5 c
                . . c d d d 5 5 5 5 5 5 5 5 b .
                . c c d d d d b 5 5 c b b c . .
                c d c d d d d b b 5 5 c b b c .
                c d d d d d d d d c c c c c c .
                . c d d d b 5 5 d c c c c . . .
                . . c c c b 5 5 b c c c c c . .
                . . . . c b 5 5 d c b b b c . .
                """),
            SpriteKind.player))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR),
        sprites.create(img("""
                . . . . . . . c c c . . . . . .
                . . . . . . c b 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b b b f f . . .
                . . . e e f e e e e f e e . . .
                . . e b c b 5 b b 5 b f b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).ay = 350
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).ay = 350
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).ay = 350
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)).ay = 350
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).set_position(114, 24)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).set_position(12, 23)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).set_position(137, 103)
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)).set_position(12, 92)
    Players = player2
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE), 100, 0)
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO), 100, 0)
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.THREE), 25, 0)
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.FOUR), 250, 0)
    scene.camera_follow_sprite(mp.get_player_sprite(player2))
mp.on_controller_event(ControllerEvent.CONNECTED, on_controller_connected)

Players: mp.Player = None
Proyectile1: Sprite = None
Proyectile4: Sprite = None
Proyectile2: Sprite = None
Proyectile3: Sprite = None
turtle.show_turtle()
game.splash("A para saltar, B para atacar")
scene.set_background_color(11)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
info.player1.set_life(3)
info.player2.set_life(3)
info.player3.set_life(3)
info.player4.set_life(3)

def on_forever():
    music.play(music.string_playable("A F E F D G E F ", 40),
        music.PlaybackMode.IN_BACKGROUND)
forever(on_forever)
