# 用PageRank挖掘希拉里邮件中的重要任务关系
import pandas as pd
import networkx as nx
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

# 文件读取
emails = pd.read_csv("./Emails.csv")
file = pd.read_csv("./Aliases.csv")
aliases = {}
for index, row in file.iterrows():
    aliases[row['Alias']] = row['PersonId']
file = pd.read_csv("./Persons.csv")
persons = {}
for index, row in file.iterrows():
    persons[row['Id']] = row['Name']

# 名字预处理，包括转化为小写、去除标点符号，与@后缀、别名转换（name->unify_name）
def unify_name(name):
    name = str(name).lower()
    name = name.replace(",","").split("@")[0]
    if name in aliases.keys():
        return persons[aliases[name]]
    return name

# 画网络图 spring_layout 中心散射状布局, circular_layout 圆环状布局
def show_graph(graph):
    positions=nx.spring_layout(graph)
    # 设置网络图中的节点大小, *20000(方便可视化)
    nodesize = [x['pagerank']*20000 for v,x in graph.nodes(data=True)]
    # 设置网络图中的边长度
    edgesize = [np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]
    # 绘制节点、边、节点的 label
    nx.draw_networkx_nodes(graph, positions, node_size=nodesize, alpha=0.4)
    nx.draw_networkx_edges(graph, positions, alpha=0.2)
    nx.draw_networkx_labels(graph, positions, font_size=10)
    plt.show()

# 将预处理后的寄件人和收件人姓名进行规范化
emails.MetadataFrom = emails.MetadataFrom.apply(unify_name)
emails.MetadataTo = emails.MetadataTo.apply(unify_name)

# 边的权重等于发邮件的次数
edges_weights_temp = defaultdict(list)
for row in zip(emails.MetadataFrom, emails.MetadataTo, emails.RawText):
    temp = (row[0], row[1])
    if temp not in edges_weights_temp:
        edges_weights_temp[temp] = 1
    else:
        edges_weights_temp[temp] = edges_weights_temp[temp] + 1

# 转化格式 (from, to), weight => from, to, weight
edges_weights = [(key[0], key[1], val) for key, val in edges_weights_temp.items()]

# 创建一个有向图 设置有向图中的路径及权重(from, to, weight) 计算每个节点（人）的PR值
graph = nx.DiGraph()
graph.add_weighted_edges_from(edges_weights)
pagerank = nx.pagerank(graph)
# 获取每个节点的pagerank数值
pagerank_list = {node: rank for node, rank in pagerank.items()}
# 将pagerank数值作为节点的属性
nx.set_node_attributes(graph, name = 'pagerank', values=pagerank_list)
show_graph(graph)

# 精简，设置阈值，筛选大于阈值的重要核心节点
pagerank_threshold = 0.010
small_graph = graph.copy()
# 剪掉PR值小于pagerank_threshold的节点
for n, p_rank in graph.nodes(data=True):
    if p_rank['pagerank'] < pagerank_threshold:
        small_graph.remove_node(n)
# 画网络图
show_graph(small_graph)