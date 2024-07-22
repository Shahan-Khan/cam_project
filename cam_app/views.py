import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render

def video_stream():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Encode the frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)

        # Convert the encoded image to bytes
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

    # cap.release()

def video_feed(request):
    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_page(request):
    return render(request, 'video_page.html')
