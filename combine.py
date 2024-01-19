import tensorflow as tf

# Assume `model` is your model's architecture

# Load the weights from each checkpoint
checkpoint_paths = ['models/starry_nights/model_checkpoint.ckpt.data-00000-of-00002', 'models/starry_nights/model_checkpoint.ckpt.data-00001s-of-00002', ...]  # List your checkpoint paths
latest_checkpoint = tf.train.latest_checkpoint(checkpoint_paths)

# Load the latest checkpoint
model.load_weights(latest_checkpoint)

# Save the combined checkpoint
model.save_weights('starry_night.ckpt')
