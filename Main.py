from Node import Node
import pprint
import sys

if __name__ == '__main__':

    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2P()
    
    if port == 10002:
        node.p2p.connect_with_node('localhost', 10001)