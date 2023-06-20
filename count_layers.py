import tensorflow as tf

def count_layers(model):
   num_layers = len(model.layers)
   for layer in model.layers:
      if isinstance(layer, tf.keras.Model):
         num_layers += count_layers(layer)
   return num_layers