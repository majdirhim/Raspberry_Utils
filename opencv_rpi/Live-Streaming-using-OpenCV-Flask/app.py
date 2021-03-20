from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
print("starting")
camera = cv2.VideoCapture(0)  # use 0 for web camera

print("starting")
def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        global frame2
        success, frame = camera.read()  # read the camera frame
        frame2 = frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture')
def capture():
    """Video streaming home page."""
    print("capture")
    cv2.imwrite("capture.png", frame2)
    return "nothing"

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, port="8000",host="192.168.100.131")