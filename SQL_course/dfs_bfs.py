# code taken from https://stackoverflow.com/a/47234034/1168442
# Some comments:
# - Because this code needs to check v not in graph[stack[-1]] a bunch of times, it will be much more efficient if the values in the graph dictionary are sets, rather than lists. A graph usually doesn't care about the order its edges are saved in, so making such a change shouldn't cause problems with most other algorithms, though code that produces or updates the graph might need fixing.
# - If you care about performance, you should probably do result.append in the second helper function too, and do return result[::-1] in the top level recursive_topological_sort function. But using insert(0, ...) is a more minimal change.
# you shouldn't need to specify a starting node. Indeed, there may not be a single node that lets you traverse the entire graph, so you may need to do several traversals to get to everything. An easy way to make that happen in the iterative topological sort is to initialize q to list(graph) (a list of all the graph's keys) instead of a list with only a single starting node. For the recursive version, replace the call to recursive_helper(node) with a loop that calls the helper function on every node in the graph if it's not yet in seen.
# -  use graph.get(node, []) instead of graph[node] to handle nodes which are referenced as values but not as keys in the original graph.  graph[v] and graph[stack[-1]]. Change them to graph.get(v, []) and graph.get(stack[-1], [])

def iterative_dfs_improved(graph, start):
    seen = set()  # efficient set to look up nodes in
    path = []     # there was no good reason for this to be an argument in your code
    q = [start]
    while q:
        v = q.pop()   # no reason not to pop from the end, where it's fast
        if v not in seen:
            seen.add(v)
            path.append(v)
            q.extend(graph[v]) # this will add the nodes in a slightly different order
                               # if you want the same order, use reversed(graph[v])

    return path


def iterative_topological_sort(graph, start):
    seen = set()
    stack = []    # path variable is gone, stack and order are new
    order = []    # order will be in reverse order at first
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v) # no need to append to path any more
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]: # new stuff here!
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]   # new return value!


def recursive_dfs(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                result.append(neighbor)     # this line will be replaced below
                seen.add(neighbor)
                recursive_helper(neighbor)

    recursive_helper(node)
    return result


def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result
