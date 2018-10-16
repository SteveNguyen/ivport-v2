#!/usr/bin/env python

import os
import ivport
import time

def picam_sequence():
    FRAMES = 30
    CAM = 0
    def sequence_outputs(iv):
        frame = 0
        while frame < FRAMES:
            camera = (frame%2)+1
            time.sleep(0.2)   # SD Card Bandwidth Correction Delay
            iv.camera_change(camera)
            time.sleep(0.2)   # SD Card Bandwidth Correction Delay
            yield 'sequence_%02d.jpg' % frame
            frame += 1
            print camera

    ivA = ivport.IVPort(ivport.TYPE_QUAD2, iv_jumper='A')
    ivA.camera_open(camera_v2=True, resolution=(640, 480), framerate=60)
    #iv.picam.resolution = (640, 480)
    #iv.picam.framerate = 30
    #time.sleep(1)
    ivA.camera_sequence(outputs=sequence_outputs(iv), use_video_port=True)
    ivA.close()

def picam_capture():
    iv = ivport.IVPort(ivport.TYPE_QUAD2, iv_jumper='A')
    iv.camera_open()
    iv.camera_change(1)
    iv.camera_capture("picam", use_video_port=False)
    iv.camera_change(2)
    iv.camera_capture("picam", use_video_port=False)
    iv.camera_change(3)
    iv.camera_capture("picam", use_video_port=False)
    iv.camera_change(4)
    iv.camera_capture("picam", use_video_port=False)
    iv.close()

def still_capture():
    # raspistill capture
    def capture(camera):
        "This system command for raspistill capture"
        cmd = "raspistill -t 10 -o still_CAM%d.jpg" % camera
        os.system(cmd)

    iv = ivport.IVPort(ivport.TYPE_QUAD2, iv_jumper='A')
    iv.camera_change(1)
    capture(1)
    iv.camera_change(2)
    capture(2)
    iv.camera_change(3)
    capture(3)
    iv.camera_change(4)
    capture(4)
    iv.close()



def still_capture2():
    # raspistill capture
    def capture(camera):
        "This system command for raspistill capture"
        cmd = "raspistill -t 10 -o still_CAM%d.jpg" % camera
        os.system(cmd)

    ivA = ivport.IVPort(ivport.TYPE_QUAD2, iv_jumper='A')
    ivA.camera_change(1)
    capture(1)
    # ivA.camera_change(2)
    # capture(2)
    # ivA.camera_change(3)
    # capture(3)

    ivB = ivport.IVPort(ivport.TYPE_QUAD2, iv_jumper='B')
    ivB.camera_change(2)
    ivA.camera_change(4)
    capture(2)
    ivA.close()
    ivB.close()


# main capture examples
# all of them are functional
def main():
    # still_capture()
    # picam_capture()
    #picam_sequence()
    still_capture2()
if __name__ == "__main__":
    main()
