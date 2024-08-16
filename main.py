def on_forever():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    basic.pause(2000)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    music.play_tone(440, music.beat(BeatFraction.HALF))
    basic.pause(1000)
    music.play_tone(880, music.beat(BeatFraction.HALF))
basic.forever(on_forever)
