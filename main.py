import time
import cv2
import numpy as np
from collections import deque

from Utils import model_util
from Utils.prediction import Prediction
from send_mail import Send_Email

results = Prediction()
mail_to_emergency = Send_Email()

# Initialize the VideoCapture object to read from the video file.
cap = cv2.VideoCapture("Datasets/accident.mp4")
#cap = cv2.VideoCapture("Merged.mp4")

# Get the Width and Height of the video.
orignal_video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
orignal_video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(orignal_video_width, orignal_video_height)

# Initialize the VideoWritter Object to store the output video in the disk.
video_writer = cv2.VideoWriter(filename= "outputs/output.mp4", fourcc= cv2.VideoWriter_fourcc("m", "p", "4", "v"),
                               fps= cap.get(cv2.CAP_PROP_FPS), frameSize= (orignal_video_width, orignal_video_height))

clip_writer = cv2.VideoWriter(filename="Utils/clip_to_send_on_mail/clip.mp4", fourcc=cv2.VideoWriter_fourcc("m", "p", "4", "v"),
                                    fps=20, frameSize=(64, 64))
collect_accuracy = set()

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video Unable to Read")
            break

        start_time = time.time()

        predicted_class_name, predicted_class_accuracy = results.prediction(frame)
        print(predicted_class_name, predicted_class_accuracy)

        # Write predicted class name on top of the frame.
        cv2.putText(frame, predicted_class_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, predicted_class_accuracy, (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Calculate FPS
        end_time = time.time()
        total_time = end_time - start_time
        try:
            fps = 1 / total_time
        except ZeroDivisionError:
            fps = 0

        # Write fps on frame
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Write The frame into the disk using the VideoWriter Object.
        video_writer.write(frame)

        # Write some frames to send on the Emergency mail Ids
        if (float(predicted_class_accuracy) if len(predicted_class_accuracy) > 0 else 0) >= 0.80:
            collect_accuracy.add(predicted_class_name)
            #print("Collected_acc", collect_accuracy)
            clip_writer.write(frame)

        frame = cv2.resize(frame, (1000, 720))
        cv2.imshow("Activity Recognition", frame)
        if cv2.waitKey(1) & 0xFF == "q":
            cv2.destroyAllWindows()
            # Release the VideoCapture and VideoWriter objects.
            cap.release()
            video_writer.release()
            clip_writer.release()
            break
    mail_to_emergency.mail_emergency(collect_accuracy)
    print("Process Completed")
    print("Average FPS:", str("{0:2f}".format(fps)))

except KeyboardInterrupt:
    print("Process Terminated")
    print("Average FPS:", str("{0:2f}".format(fps)))
