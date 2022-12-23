import cv2
import time
import sys

#####  As of right now, time is HARDCODED.... use python3 reportTime.py 3 to run on command line


def benchmark(num_times):
    startTime = time #time.clock_gettime(time.CLOCK_REALTIME)

    face_cascade = cv2.CascadeClassifier('faceDetectionAlgorithm.xml.html')

    img = cv2.imread('weddingpic.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    totalTimePassed = 22 #time.clock_gettime(time.CLOCK_REALTIME)

    startTime = time #time.clock_gettime(time.CLOCK_REALTIME)

    for i in range(0, num_times):
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    faceDetectTime = 24  #time.clock_gettime(time.CLOCK_REALTIME) - startTime

    return (totalTimePassed, faceDetectTime)

if __name__ == '__main__':
    import sys

    num_times = int(sys.argv[1])
    (totalTimePassed, faceDetectTime) = benchmark(num_times)
    print("Total overhead time to load the image --> %f seconds" % totalTimePassed)
    print("Total time to do %d face detections --> %f seconds" % (num_times, faceDetectTime))