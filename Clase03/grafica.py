def main():
    node1  = input("Ingrese el primer nodo: ");
    node2  = input("Ingrese el segundo nodo: ");
    node3  = input("Ingrese el tercer nodo: ");
    nodes = [node1, node2, node3];
    createDot(nodes);
    createDotOS(nodes);

import graphviz;

def createDot(nodes):
    dot = graphviz.Digraph(comment='Mi primer grafica');
    for i in range(len(nodes)):
        dot.node(f'n{i}', f'{nodes[i]}');
        if (i != 0):
            dot.edge(f'n{i-1}', f'n{i}');
    dot.render('test-output/round-table.gv', view=True);

# utilizando el sistema operativo 
import os;
def createDotOS(nodes):
    dot = 'digraph G {';
    for i in range(len(nodes)):
        dot += f'n{i} [label="{nodes[i]}"];';
        if (i != 0):
            dot += f'n{i-1} -> n{i};';
    dot += '}';
    f = open('test-output/graficaOS.gv', 'w');
    f.write(dot);
    f.close();
    os.system('dot -Tpdf test-output/graficaOS.gv -o test-output/graficaOS.pdf');

if __name__ == "__main__":
    main();