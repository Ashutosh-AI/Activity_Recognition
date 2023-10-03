from tensorflow.keras.models import load_model
import os

model_dir = os.path.join("Trained_model", "LRCN_model___Date_Time_2023_08_24__14_57_04___Loss_0.515287458896637___Accuracy_0.800000011920929.h5")

def get_trained_model(model_dir= model_dir):

    print("## Loading Trained Model")

    model = load_model(model_dir)

    print("## Trained Model Loaded Successfully")

    return model