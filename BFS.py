{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOlnR3n5yyGWY26l2MdR3AU"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"BLnjRCS4ETAY"},"outputs":[],"source":["# BFS algorthm in python\n","\n","import collections\n","\n","# BFS algorithm\n","def bfs(graph, root):\n","\n","  visited, queue = set(), collections.deque([root])\n","  visited.add(root)\n","\n","  while queue:\n","\n","      #dequeue a vertex from queue\n","      vertex = queue.popleft()\n","      print(str(vertex) + \" \", end = \"\")\n","\n","      #if not visited, mark it as visited, and\n","      #enqueue it\n","      for neighbour in graph[vertex]:\n","        if neighbour not in visited:\n","          visited.add(neighbour)\n","          queue.append(neighbour)\n","\n","if __name__ == '__main__':\n","  graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}\n","  print(\"Following is Breadth First Traversal: \")\n","  bfs(graph, 0)"]}]}