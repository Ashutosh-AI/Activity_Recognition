# Visit for setup gmail to get access
# https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4Pc3hWsPtRRTWDja1kWct-GW1Zs-vC3A-lm48Atn2L0cny5WomKU3L0ofogLEzW-cnkZlp6O9b2RSxkJCuutgbHZwvR4w

import smtplib
from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import get_location

class Send_Email():

    def __init__(self):
        self.myEmail = "xyz@gmail.com"
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.location = get_location.location()

        self.msg = MIMEMultipart()
        self.msg["From"] = self.myEmail
        self.msg["To"] = self.myEmail


        # creates SMTP session
        self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)

        # start TLS for security
        self.server.starttls()

        # Authentication
        self.server.login(self.myEmail, "**********")


    def attech_video(self):

        with open("Utils/clip_to_send_on_mail/clip.mp4", "rb") as f:
            video = MIMEBase("application", "octet-stream")
            video.set_payload(f.read())
            encoders.encode_base64(video)
            video.add_header('Content-Disposition', 'attachment; filename=clip.mp4')
            self.msg.attach(video)


    def emergency(self, emergency_class):

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.date()

        if emergency_class == "RoadAccidents":

            road_emer_msg = """Dear Emergency Services,
                            I am reporting a road accident that occurred on the {}.
                            at approximately {} on {}.
                            Please dispatch emergency services AMBULANCE to the scene immediately.
                            Check out this small clip, please.
                            Thank you,
                            Send by Surveillance Emergency System""".format(self.location, current_time, current_date)

            self.msg["Subject"] = "Road Accident Alert Notification to Emergency"
            self.msg.attach(MIMEText(road_emer_msg))
            self.attech_video()

            self.server.send_message(self.msg)
            # terminating the session
            #self.server.quit()

        if emergency_class == "Explosion":

            expl_emer_msg = """Dear Emergency Services,
                            An explosion has occurred at the above {}.
                            at approximately {} on {}.
                            Please stay away from the area and allow emergency FIRE BRIGADE personnel to respond.
                            Check out this small clip, please.
                            Thank you,
                            Send by Surveillance Emergency System""".format(self.location, current_time, current_date)

            self.msg["Subject"] = "Explosion Alert Notification to Emergency"
            self.msg.attach(MIMEText(expl_emer_msg))
            self.attech_video()

            self.server.send_message(self.msg)
            # terminating the session
            #self.server.quit()

        if emergency_class == "Fighting":

            fight_emer_msg = """Dear Emergency Services,
                             Fighting alert in progress at {}.
                             at approximately {} on {}.
                             Please dispatch emergency services POLICE to the scene immediately
                             Check out this small clip, please.
                             Thank you,
                             Send by Surveillance Emergency System""".format(self.location, current_time, current_date)

            self.msg["Subject"] = "Fighting Alert Notification to Emergency"
            self.msg.attach(MIMEText(fight_emer_msg))
            self.attech_video()

            self.server.send_message(self.msg)
            # terminating the session
            #self.server.quit()


    def mail_emergency(self, unique_str_classes):

        # all classes above 95%
        print("unique_str_classes", unique_str_classes)

        for classes in unique_str_classes:
            Send_Email.__init__(self)
            #print("classes", classes)
            self.emergency(classes)

        self.server.quit()
        print("Mail Successfully Send to the Emergency")


        """
        sorted_dict = sorted(collected_acc.keys(), reverse=True)

        max1_values_key = sorted_dict[0]
        max1_accuracy_class = collected_acc[max1_values_key]

        max2_values_key = sorted_dict[1]
        max2_accuracy_class = collected_acc[max2_values_key]

        if max1_accuracy_class == max2_accuracy_class:
            self.emergency(max1_accuracy_class)

        else:
            self.emergency(max1_accuracy_class)
            self.emergency(max2_accuracy_class)"""