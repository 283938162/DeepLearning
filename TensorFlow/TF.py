import tensorflow as tf

# a= tf.constant([1,2,3],name='a')  Tensor("a:0", shape=(3,), dtype=int32)
a = tf.constant([[1, 2, 3]])  # Tensor("Const:0", shape=(3,), dtype=int32)

print('a = ', a)
