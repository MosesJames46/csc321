import networkx as nx
from dns.resolver import resolve
import dns
from dns import reversename
import matplotlib.pyplot as plt
import numpy as np
from os.path import exists
empty=[]

#/
# /#
#obatins domains from the tsv
with open('domains.tsv', 'r') as dom:
    for line in dom:
        for domain in line.split():
            if '.com' in domain or '.net' in domain or '.org' in domain or '.co' in domain:
                empty.append(domain)

#makes individual plots of each graph consiting of name values that point to correspoing domain
def make_plot(graphing,el,el2):
    graphing.add_edges_from(el)
    graphing.add_edges_from(el2)
    nx.draw(G,with_labels=True)
    file_exists = exists(f"png_folder/{el[0][0]}.jpg")
    #makes sure there are no repeated png withing folder
    if file_exists == True:
        pass
    else:
        plt.savefig(f"png_folder/{el[0][0]}.jpg")
    
    return plt.figure(f'graph{count}.png')
    
#First half of loop sends forward dns that obtains the IP addresses
graphs = []
count = 0
for website in empty:
    try:
        a_record = resolve(website , "A")  
    except dns.resolver.NXDOMAIN :
        continue
    except dns.resolver.NoAnswer:
        continue
    count += 1
    if len(a_record):
        edge_list = []
        # Second half is contributed by Zach Chatman and returns the reverse DNS 
        for addr in a_record:
            edge_list.append((website,str(addr)))
            search_addr = reversename.from_address(str(addr))
            try:
                reverse_search_results = resolve(search_addr, "PTR")
            except dns.resolver.NXDOMAIN:
                continue
            except dns.resolver.NoNameservers:
                continue
            except dns.resolver.LifetimeTimeout:
                continue
            if len(reverse_search_results):
                G = nx.DiGraph()
                edge_list_2 = []
                for d in reverse_search_results:
                    edge_list_2.append((str(addr),str(d)))
                    G.add_node(str(d))
                    G.add_edge(domain, str(d))
                    print(f"Adding edge {website} -> {str(d)}")
        graphs.append((edge_list,edge_list_2))
        plot = make_plot(G,edge_list,edge_list_2)
        
dom.close()