#include <stdlib.h>
#include <stdio.h>

int main(){
    FILE * graph = fopen("test1Graph.gv","w");
    
    fprintf(graph,"digraph{\n");
    fprintf(graph,"edge [color=black]\n");
    fprintf(graph, "\"main\" -> \"printf\" [label=\"2 times line 20,21\"]\n");
    fprintf(graph,"\"main\" -> \"ms.f\" [label=\"2 times line 20,21\"]\n");
    fprintf(graph,"\"ms.f\" -> \"facto\" [style=dotted]\n");
    fprintf(graph, "\"facto\" -> \"facto\" [label=\"2 times line 11,12\"]\n");
    fprintf(graph,"\"facto\" -> \"f1\" [label=\"1 times line 13\"]\n");
    fprintf(graph,"\"facto\" -> \"a\" [label=\"1 times line 14\"]\n");
    fprintf(graph,"\"a\" -> \"facto\" [style=dotted]\n");
    fprintf(graph,"}");
    fclose(graph);
    system("dot -Tjpg test1Graph.gv -o test1Graph.jpg");

}
