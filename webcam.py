import cv2 
import threading

from speech import voice

recognized_text = ""

def recognize_speech():
    global recognized_text
    while True:
        recognized_text = voice()
  
def capture_video():
    # define a video capture object 
    vid = cv2.VideoCapture(0) 
  
    while(True): 
      
        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 

        cv2.putText(frame, recognized_text, (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
  
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
      
        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
  
    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows()

# Create and start the threads
speech_thread = threading.Thread(target=recognize_speech)
video_thread = threading.Thread(target=capture_video)
speech_thread.start()
video_thread.start()