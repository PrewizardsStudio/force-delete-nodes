def deleteChildrenNodes(node):
    if cmds.objExists(node):
        allChildNodes = cmds.listRelatives(node, children=1, fullPath=1)
        if allChildNodes:
            allChildNodes.append(node)
        else:
            allChildNodes = [node]
        print(allChildNodes)
        for child in allChildNodes:
            print(child)
            if cmds.objExists(child):
                if cmds.referenceQuery(child, isNodeReferenced=1):
                    referenceNode = cmds.referenceQuery(child, referenceNode=1)
                    cmds.file(removeReference = True, referenceNode = referenceNode)
                elif isGroup(child) and cmds.listRelatives(child, children=1):
                    deleteChildrenNodes(child)
                    if cmds.objExists(child):
                        cmds.lockNode(child, lock=0)
                        cmds.delete(child)
                else:
                    cmds.lockNode(child, lock=0)
                    cmds.delete(child)

# delete selected node, referenced node
def forceDeleteSelectedNodes():
    for nodee in cmds.ls(sl=1, allPaths=1):
        deleteChildrenNodes(nodee)    