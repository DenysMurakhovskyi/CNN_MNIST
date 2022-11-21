from tensorflow.keras.models import load_model
import pathlib

path = pathlib.Path(__file__).parents[1].resolve() / 'jupiter/digit_model.h5'
model = load_model(path)

