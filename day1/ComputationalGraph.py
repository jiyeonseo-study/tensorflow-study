
import tensorflow as tf

# graph를 먼저 빌드하고
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1:", node1, "node2:", node2) # node1: Tensor("Const:0", shape=(), dtype=float32) node2: Tensor("Const_1:0", shape=(), dtype=float32)
print("node3:", node3) # node3:  Tensor("Add:0", shape=(), dtype=float32)

sess = tf.Session()

# Session을 이용하여 실행 sess.run(graph)
print("sess.run(node1, node2):", sess.run([node1, node2])) # sess.run(node1, node2):  [3.0, 4.0]
print("sess.run(node3):", sess.run(node3)) # sess.run(node3):  7.0



