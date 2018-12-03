from sklearn.tree import export_graphviz
import os

def visualize_tree(tree, feature_names):
    with open("/tmp/dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f, impurity=False, class_names=["blue", "red"], feature_names=feature_names, label="none")

    os.system("dot -Tpng /tmp/dt.dot -o /tmp/dt.png")