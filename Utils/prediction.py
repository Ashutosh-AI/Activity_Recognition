import cv2
from collections import deque
import numpy as np

from Utils import model_util

class Prediction():

    def __init__(self):

        self.IMAGE_HEIGHT = 64
        self.IMAGE_WIDTH = 64
        self.CLASSES_LIST = ["Explosion", "Fighting", "RoadAccidents"]
        self.SEQUENCE_LENGTH = 30
        self.score_thresh = 0.55

        self.frames_queue = deque(maxlen=self.SEQUENCE_LENGTH)
        self.LRCN_model = model_util.get_trained_model()


    def prediction(self, frame):

        predicted_class_name = ""
        predicted_class_accuracy = ""

        # Resize the Frame to fixed Dimensions.
        resized_frame = cv2.resize(frame, (self.IMAGE_HEIGHT, self.IMAGE_WIDTH))

        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1.
        normalized_frame = resized_frame / 255

        # Appending the pre-processed frame into the frames list.
        self.frames_queue.append(normalized_frame)

        # Check if the number of frames in the queue are equal to the fixed sequence length.
        if len(self.frames_queue) == self.SEQUENCE_LENGTH:

            # Pass the normalized frames to the model and get the predicted probabilities.
            predicted_labels_probabilities = self.LRCN_model.predict(np.expand_dims(self.frames_queue, axis=0))[0]

            # Get the index of class with highest probability
            predicted_label = np.argmax(predicted_labels_probabilities)

            if predicted_labels_probabilities[predicted_label] > self.score_thresh:

                # Get the class name using the retrieved index.
                predicted_class_name = self.CLASSES_LIST[predicted_label]
                predicted_class_accuracy = str(np.round(predicted_labels_probabilities[predicted_label], 2))

        return predicted_class_name, predicted_class_accuracy
