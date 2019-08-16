"""
Citizens of GridLand are sending emails to each other all the time. They send everything - what they just ate, a funny 
picture, questions or thoughts that are bothering them right now. All the citizens are happy because they have such a 
wonderful network that keeps them connected.

The main goal of the Mayor is to control the city's happiness. The city's happiness is a sum of all citizens' happiness. And 
the happiness of each citizen is equal to the number of citizens (always including oneself) that one can send emails to.

Because the city is growing, the citizens have decided that the Mayor needs an assistant to focus on the node protection.

Your mission is to figure out what will be the first nodes to investigate and protect for the new assistant. Remember, you 
should choose the most important node in the network. If several nodes have the maximal importance, find all of them

Input: Two arguments: the network structure (as a list of connections between the nodes), users on each node (as dict where 
keys are the node-names and values are the amounts of users).

Output: List of the most cruсial nodes. 
"""


def net_to_dict(net):
    net_dict = {}
    for edge in net:
        net_dict[edge[0]] = net_dict.get(edge[0], [])
        net_dict[edge[0]].append(edge[1])
        net_dict[edge[1]] = net_dict.get(edge[1], [])
        net_dict[edge[1]].append(edge[0])
    for node in net_dict:
        net_dict[node] = set(net_dict[node])
    return net_dict

#------------------------------------------------------------------------------#

def all_nodes_set(net):
    all_nodes = set()
    for edge in net:
        all_nodes.add(edge[0])
        all_nodes.add(edge[1])
    return all_nodes

#------------------------------------------------------------------------------#

def round(node, net, nodes):
    component = [node]
    for n in net[node]:
        if n in nodes:
            nodes.remove(n)
            component.extend(round(n, net, nodes))
    return component

#------------------------------------------------------------------------------#

def most_crucial(net, users):
    net_dict = net_to_dict(net)
    all_nodes = all_nodes_set(net)
    most_crucial_vertex = {}
    for crush_node in all_nodes:
        nodes = all_nodes - set(crush_node)
        most_crucial_vertex[crush_node] = users[crush_node]
        clusters = []
        while nodes != set():
            node = nodes.pop()
            clusters.append(round(node, net_dict, nodes))
        for cluster in clusters:
            most_crucial_vertex[crush_node] += sum(users[node] for node in cluster)**2
    most_crucial_vertex = sorted(most_crucial_vertex.items(), key=lambda x: x[1])
    return [v[0] for v in most_crucial_vertex if v[1] == most_crucial_vertex[0][1]]

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')

