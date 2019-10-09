########################################
# Import nimbus CFTWrappers package here
########################################


def get_namespaces():
    #change this
    ns = ["dev","qa","fwqa","training"]
    return ns

def get_vservers(namespace):
    vserver_list = ["vserver1","vserver2","vserver3"]
    vserver_list.append(namespace)
    return vserver_list
