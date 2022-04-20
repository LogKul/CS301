

# ===============================
#             TREES
# ===============================


class TreeNode:
    def __init__(self, input_id, val):
        self.id = input_id
        self.value = val
        self.children = []


class Tree:
    def __init__(self, root_value):
        self.start = TreeNode(0, root_value)
        self.nodes = 1

    def search(self, search_val):
        if self.start.value == search_val:
            return True
        else:
            return self.search_recur(self.start, search_val)

    def search_recur(self, parent_node, search_val):
        if len(parent_node.children) > 0:
            for child in parent_node.children:
                if child.value == search_val:
                    return True
                branch = self.search_recur(child, search_val)
                if branch == True:
                    return branch
        return False

    def node_dfs(self, search_id):
        if self.start.id == search_id:
            return self.start
        else:
            return self.node_dfs_recur(self.start, search_id)

    def node_dfs_recur(self, parent_node, search_id):
        if len(parent_node.children) > 0:
            for child in parent_node.children:
                if child.id == search_id:
                    return child
                branch = self.node_dfs_recur(child, search_id)
                if branch is not False:
                    return branch
        return False

    def put(self, value, parent_id):
        parent_node = self.node_dfs(parent_id)
        if parent_node == False:
            print("Error, parent node does not exist.")
        else:
            parent_node.children.append(TreeNode(self.nodes, value))
            print("Node ID:", self.nodes, "value:", value,
                  "Parent:", parent_node.value)
            self.nodes += 1


# ===============================
#        DIRECTED GRAPHS
# ===============================


class Vertex:
    def __init__(self, id, val):
        self.id = id
        self.value = val
        self.children = []


class DirectedGraph:
    def __init__(self, val):
        self.vertexes = []
        self.start = Vertex(0, val)
        self.vertices = 1

    def search(self, search_val):
        if self.start.value == search_val:
            return True
        else:
            return self.search_recur(self.start, search_val, [self.start])

    def search_recur(self, parent_vertex, search_val, search_stack):
        if len(parent_vertex.children) > 0:
            for child in parent_vertex.children:
                if child.value == search_val:
                    return True
                if child.id not in search_stack:
                    search_stack.append(child.id)
                    branch = self.search_recur(
                        child, search_val, search_stack)
                    if branch is not False:
                        return branch
        return False

    def vertex_dfs(self, search_id):
        if self.start.id == search_id:
            return self.start
        else:
            return self.vertex_dfs_recur(self.start, search_id, [self.start])

    def vertex_dfs_recur(self, parent_vertex, search_id, search_stack):
        if len(parent_vertex.children) > 0:
            for child in parent_vertex.children:
                if child.id == search_id:
                    return child
                if child.id not in search_stack:
                    search_stack.append(child.id)
                    branch = self.vertex_dfs_recur(
                        child, search_id, search_stack)
                    if branch is not False:
                        return branch
        return False

    def put(self, value, parent_ids, child_ids):
        newVertex = Vertex(self.vertices, value)
        flag = False
        for parent_id in parent_ids:
            parent_vertex = self.vertex_dfs(parent_id)
            if parent_vertex == False:
                flag = True
                print("Error, parent vertex does not exist. Vertex aborted.")
            else:
                parent_vertex.children.append(newVertex)
                print("Vertex ID:", self.vertices, "value:", value,
                      "Parent:", parent_vertex.value)
        if flag == False:
            for child_id in child_ids:
                child_vertex = self.vertex_dfs(child_id)
                if child_vertex == False:
                    flag = True
                    print("Error, child vertex does not exist. Vertex aborted")
                else:
                    child_vertex.children.append(Vertex(self.vertices, value))
                    print("Vertex ID:", self.vertices, "value:", value,
                          "Child:", child_vertex.value)
        if flag == False:
            self.vertices += 1


print(" ---- TREE ---- ")

a = Tree(7)
a.put(12, 0)
a.put(13, 0)
a.put(14, 1)
a.put(15, 1)
a.put(16, 4)
a.put(17, 4)

print(a.search(7))
print(a.search(12))
print(a.search(13))
print(a.search(14))
print(a.search(15))
print(a.search(16))
print(a.search(17))
print(a.search(18))

print(" ---- DIRECTED GRAPH ---- ")

b = DirectedGraph(0)
b.put(1, [0], [])
b.put(2, [0], [1])
b.put(3, [1], [])
b.put(4, [3], [2])
b.put(5, [5], [6])

print(b.search(-1))
print(b.search(0))
print(b.search(1))
print(b.search(2))
print(b.search(3))
print(b.search(4))
print(b.search(5))
print(b.search(6))

#
# 4.) What is the running time of each of the search algorithms?
#
#   a.) O(N). For the recursive DFS search for the Tree class, we have N elements that we
#       need to search through, while we have N-1 branches. The only operation that
#       is not constant-runtime is the "for child in parent.children", which performs
#       a few operations of constant runtime for every child, and in the case of our
#       Tree class, each child represents an element of N, so our DFS algorithm runs
#       in O(N) time.
#
#   b.) O(N^2). For the recursive DFS search for the Directed Graph class, we have n
#       elements that we want to search through, while we can have an undetermined number
#       of branches, because we can decide where we want individual connections, rather
#       than connections existing under some rule. However, because we keep track of the
#       vertices that we have already begun to search the children of, we eliminate the need
#       to travel down every branch, so we should travel through our graph around N times.
#       However, this does not mean that our runtime is O(N), because for every child we
#       look at, we look through an unsorted list of vertices that we have already checked
#       to determine to continue searching through that specific child or not, which takes
#       O(N) time to complete for each of our O(N) runtime elements. This means that our
#       total runtime is O(N) for our DFS searching algorithm.
