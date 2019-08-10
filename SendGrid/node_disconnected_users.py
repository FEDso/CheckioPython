"""
Welcome to the GridLand. All the citizens here are connected through the global internal network because the main way for 
communication here is via email. Every new district of the city starts with building a node – center of the district. All 
citizens are connected to this node in order to send and receive emails. All nodes of GridLand are connected so one node can 
send emails between the connected nodes. In such a way, no matter how big the city is all users can send messages to each 
other as long as all of the nodes are connected.

The Mayor of GridLand is using this network to quickly send emergency emails to all citizens when necessary. But the system 
is not perfect. When one of city nodes gets crushed it may leave the citizens of this node district disconnected from these 
emergency emails. It may also leave districts around the crushed node disconnected if their nodes do not have other ways to 
connect. To resolve this occurrence, the Mayor uses mail-pigeons – an old method of sending mail that was invented before the 
global internal network. All of the citizens still connected to the network receive the emergency emails, but the disconnected 
citizens receive their messages from these pigeons.

Your mission is to figure out how many pigeons you need when some of the nodes are crushed.

Input: Four arguments: network structure (as a list of connections between the nodes), users of each node (as dict where keys 
are the node-names and values are the amounts of users), name of the node that sends email, and the list of crashed nodes.

Output: Int. The amount of users that won't receive an email. 
"""

def nums_in_nodes(net):
    nodes_in = {}
    for node in net:
        nodes_in[node[1]] = nodes_in.get(node[1], 0) + 1
    return nodes_in

#------------------------------------------------------------------------------#

def net_ways(net):
    net_dict = {}
    for node in net:
        net_dict[node[0]] = net_dict.get(node[0], [])
        net_dict[node[0]].append(node[1])
    return net_dict

#------------------------------------------------------------------------------#

def minus_in_n(node, net_dict, nodes_in):
    if node in net_dict:
        for n in net_dict[node]:
            nodes_in[n] -= 1
            minus_in_n(n, net_dict, nodes_in)

#------------------------------------------------------------------------------#

def disconnected_users(net, users, source, crushes):
    if source in crushes:
        return sum(users.values())
    nodes_in = nums_in_nodes(net)
    net_dict = net_ways(net)
    for node in crushes:
        minus_in_n(node, net_dict, nodes_in)
            
    s = sum(users[node] for node in crushes)
    users.pop(source)
    return sum(v for k, v in users.items() if k in nodes_in and nodes_in[k] == 0) + s

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    print(disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']))
    
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
    
    
