import mpv

video1 = "/videos/video1.mp4"
video2 = "/videos/video2.mp4"

player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True)

player.pause = True

player.play(video1)
player.wait_for_playback()

player.loop = "inf"
player.play(video2)
player.wait_for_playback()