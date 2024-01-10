# Activity_Recognition
The UGV ((Unmanned Ground Vehicle)) based Surveillance solution system is a deep learning-based object detection
the model which will help us to detect the anomalies in society and take the necessary
action.

The main aim is to create an AI solution for surveillance using a rover or UGV and to
implement the following use cases.
1. To detect mob (illegal) activities (like Fighting) and inform the Police.
2. To detect disasters (like fire and explosion) and send details to concerned authorities.
3. To detect a medical emergency (Road Accident) and take emergency action (call an
   ambulance and raise an alarm to the nearest hospital) for help.

#This Project works in These Steps:
1. First Detect the Activity in the Video or WebCam, If there is unethical Activity Detected
2. then, first get the Camera's Current Location IP, Current Address, City Postal Code
3. Store some Frames of the Disaster
4. Send all the details (Emergency Location, Emergency small clip, what type of emergency) to the Concerned Authorities
5. For explosion send Mail to the Fire Brigade, for Fighting send Mail to the Police and for Accident mail to the Hospital with a small clip.


![Screenshot 2023-10-03 213225](https://github.com/Ashutosh-AI/Activity_Recognition/assets/53949585/7d8a9fea-fcf2-477e-88c4-0d1a87c3d77c)



https://github.com/Ashutosh-AI/Activity_Recognition/assets/53949585/52ac1b0f-55a1-4fac-9095-4ff26bb019e5





# This Project Recognise three classes 
Explosion
Road Accident
Fighting

# This is the Trained Model Architecture
The Network combines CNN with LSTM to use the CNN as a feature extractor for images and then feeds the features into the LSTM to analyze the Sequence (CNN + RNN)

![LRCN_model_structure_plot (1)](https://github.com/Ashutosh-AI/Activity_Recognition/assets/53949585/1bb7e338-c387-4f33-9564-b6adbaf3150e)

# Dataset:
  The dataset for this project for the Indian continent contains small videos of all three classes.
  Datasets link:
  https://www.crcv.ucf.edu/projects/real-world/
