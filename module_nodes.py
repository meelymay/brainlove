from collections import defaultdict

def distance(node, neighb, pos):
    p1 = pos[node]
    p2 = pos[neighb]
    return sum([abs(p1[x]-p2[x])**2 for x in range(3)])**.5


def print_module_size(modules, nodes):
    for module in modules:
        mod_nodes = list(modules[module])
        farthest = max([max([distance(n1, n2, nodes) for n2 in mod_nodes]) for n1 in mod_nodes])
        print module, farthest

def print_distances(modules, nodes):
    for module in modules:
        print 'Module',module
        mod_nodes = list(modules[module])
        for node in mod_nodes:
            print ',',node,
        print
        for node in mod_nodes:
            print node,
            # print '%s\t%s\t%s' % (module, node, nodes[node])
            for neighbor in mod_nodes:
                print ',',distance(node, neighbor, nodes),
            print

def print_extra_bars(modules, bars):
    for module in modules:
        mod_nodes = list(modules[module])
        for neighbor_mod in modules:
            printed = set([])
            print module,neighbor_mod
            for node in mod_nodes:
                for neighbor in bars[node]:
                    if node+neighbor in printed:
                        break
                    if not bars[node][neighbor]:
                        break
                    neighb_mod_nodes = modules[neighbor_mod]
                    if neighbor in neighb_mod_nodes and node not in neighb_mod_nodes:
                        print '\t',node,neighbor
                        printed.add(node+neighbor)
                        printed.add(neighbor+node)

if __name__ == '__main__':

    module_struts = 'module_struts.txt'
    f = open(module_struts, 'r')
    modules = {}
    module = set([])
    for line in f:
        if 'module' in line:
            module = set([])
            mod_name = line.split()[-1]
            modules[mod_name] = module
        else:
            node1, node2 = [x.strip().upper() for x in line.split()]
            module.add(node1)
            module.add(node2)
    f.close()

    nodes_3d = 'node_info.csv'            
    f = open(nodes_3d, 'r')
    nodes = {}
    bars = defaultdict(lambda: defaultdict(bool))
    for line in f:
        fields = line.split(',')
        node = fields[0].upper()
        if node == 'NAME':
            continue
        x = float(fields[1])
        y = float(fields[2])
        z = float(fields[3])
        nodes[node] = (x,y,z)
        neighbors = [fields[i].strip().upper() for i in range(4,len(fields),2)]
        for neighbor in neighbors:
            bars[node][neighbor] = True
            bars[neighbor][node] = True

    print_extra_bars(modules, bars)
