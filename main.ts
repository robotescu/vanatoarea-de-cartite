input.onButtonPressed(Button.A, function () {
    ciocan1.change(LedSpriteProperty.X, -1)
    ciocan2.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    ciocan1.change(LedSpriteProperty.Y, 2)
    ciocan2.change(LedSpriteProperty.Y, 2)
    if (ciocan2.isTouching(bila)) {
        game.addScore(1)
        basic.showNumber(game.score())
    }
    basic.pause(500)
    ciocan1.change(LedSpriteProperty.Y, -2)
    ciocan2.change(LedSpriteProperty.Y, -2)
})
input.onButtonPressed(Button.B, function () {
    ciocan1.change(LedSpriteProperty.X, 1)
    ciocan2.change(LedSpriteProperty.X, 1)
})
let ciocan2: game.LedSprite = null
let ciocan1: game.LedSprite = null
let bila: game.LedSprite = null
let score = 0
bila = game.createSprite(randint(0, 4), 4)
ciocan1 = game.createSprite(2, 1)
ciocan2 = game.createSprite(2, 2)
let timp_pornire = input.runningTime()
basic.forever(function () {
    basic.pause(2000)
    bila.delete()
    bila = game.createSprite(randint(0, 4), 4)
})
basic.forever(function () {
    if (input.runningTime() - timp_pornire >= 20000) {
        game.gameOver()
    }
})
