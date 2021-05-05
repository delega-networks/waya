#!/usr/bin/python2.7
#
# Author: manfer33
#
# Version 2.0 14-dic-2019 made by https://github.com/manfer33
# Latest mod 4-may-2021 by wimel85
#
### Where Are You All (waya) - script to find node info (monikers and IPs) from Cosmos and based networks

import requests, json

node_list = {} # List of nodes located
node_checked = {} # List to save nodes checked 
debug_file = False
debug_file_name = "rpc_net_info_output"
## Open input file with an initial list of nodes to explore, parse information (moniker and IP) and save them in node_list dictionary var
# Format: 
# 'Lorem' '127.0.0.1'
# 'Ipsum' '127.0.0.1'
with open('input.txt','r') as content:
    for line in content:
        (key, val) = line.split(" ")
        node_list[key.replace("'",'')] = val.replace("'",'').replace('\n','')

## Get info about nodes connected to those who are included in the node_list var and save an output file with results.
def get_data():
    global node_list
    global node_checked

    # Check each node of node_list 
    for moniker,ip in node_list.items():
        # Check if the current node has been processed
        if not moniker in node_checked:
            peers=[]
            try:
                if debug_file:
                    # Open debug file in JSON format and load useful data 
                    with open(debug_file_name,'r') as f:
                        response = json.load(f)
                    peers.append(response["result"]["peers"])
                    # Add moniker and ip information to node_list var for each one of that peers located
                    for peer in range(int(response["result"]["n_peers"])):
                        ip_index = str(peers[0][peer]['remote_ip']).split(':')[0].split('.')[0]
                        # Avoid ip's like 10.x.x.x or 72.x.x.x 
                        if( ip_index != 10 and ip_index != 72 ):
                            node_list[str(peers[0][peer]['node_info']['moniker'])]= str(peers[0][peer]['remote_ip']).split(':')[0]
                else:
                    # Get the list of peers connected to the current node
                    response = requests.get("http://" + str(ip) + ":26657/net_info", timeout=2)
                    peers.append(response.json()["result"]["peers"])
                    # Add moniker and ip information to node_list var for each one of that peers located
                    for peer in range(int(response.json()["result"]["n_peers"])):
                        ip_index = str(peers[0][peer]['remote_ip']).split(':')[0].split('.')[0]
                        # Avoid ip's like 10.x.x.x or 72.x.x.x 
                        if( ip_index != 10 and ip_index != 72 ):
                            node_list[str(peers[0][peer]['node_info']['moniker'])]= str(peers[0][peer]['remote_ip']).split(':')[0]

            except Exception as e:
                print e

            # Include current node in the node_checked var to avoid process it again in the next call of the function
            node_checked[moniker]=ip

    # To end generate an output file with the complete list of nodes located.
    # This file is continuously overwritten with the last complete result at the end of each iteration
    with open('output.txt', 'w') as out:
        for key, val in node_list.items():
            out.write("'%s' '%s'\n" % (key, val))

## Non-stop execution of the script
# TODO: Think about any end condition
while True:
    get_data()
    print node_list #Debug
    # print node_checked #Debug
    pass
