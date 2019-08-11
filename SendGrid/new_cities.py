"""
 Sometimes damaged nodes are unrecoverable. In that case, people that were connected to the crushed node must migrate to 
 another district while administration attempts to fix the node.

But if a crushed node disconnects multiple districts from one another, then the network splits into two sub-networks and every 
sub-network should have their own Mayor. And Mayors must use pigeons for mailing between each other. In that case, when the 
network is split you don’t need hundreds of pigeons.

Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed. In other words, 
you need to figure out how many sub-networks will be formed after some nodes are crush and not recovered.

Input: Two arguments: the network structure (as a list of connections between the nodes) and the list of crashed nodes.

Output: Int. The amount of sub-networks formed after some nodes were crushed. 
"""

def nodes_set(net):
    nodes = set()
    for node in net:
        nodes.add(node[0])
        nodes.add(node[1])
    return nodes
    
#------------------------------------------------------------------------------#

def net_without_crashes(net, crushes):
    net_break = {}
    for way in net:
        if way[0] not in crushes and way[1] not in crushes:
            net_break[way[0]] = net_break.get(way[0], set())
            net_break[way[0]].add(way[1])
    return net_break
    
#------------------------------------------------------------------------------#

def build_cluster(node, net_break, nodes):
    cluster = []
    for n in node:
        if n in nodes:
            nodes.remove(n)
        else:
            break
        node_to = net_break.pop(n, [])
        cluster.append(n)
        cluster.extend(build_cluster(node_to, net_break, nodes))
    return cluster
    
#------------------------------------------------------------------------------#

def subnetworks(net, crushes):
    nodes = nodes_set(net)
    for node in crushes:
        nodes.remove(node)
    net_break = net_without_crashes(net, crushes)
    clusters = []
    i = 0
    while True:
        if not net_break:
            break
        node, node_to = net_break.popitem()
        nodes.remove(node)
        clusters.append([node])
        clusters[i].extend(build_cluster(node_to, net_break, nodes))
        i += 1
    return len(clusters) + len(nodes)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    print(subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']))

    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')

