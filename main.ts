basic.forever(function on_forever() {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    basic.pause(2000)
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    music.playTone(440, music.beat(BeatFraction.Half))
    basic.pause(1000)
    music.playTone(880, music.beat(BeatFraction.Half))
})
