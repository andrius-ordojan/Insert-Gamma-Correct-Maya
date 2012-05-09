from pymel.core import *

gammaCorrectValue = (0.455, 0.455, 0.455)

selectedNodes = selected()

for node in selectedNodes:
    if node.hasAttr('outColor') is False:
        continue
    
    nodeName = node.name()
    
    if node.outColor.isConnected():
        outputConnection = PyNode(node.outColor.connections(plugs = True)[0])
        
        if outputConnection.nodeType() == 'gammaCorrect':
            continue
        
        gammaCorrect = nt.GammaCorrect(name = '%s_GammaCorrect' % nodeName)
        gammaCorrect.gamma.set(gammaCorrectValue)
        
        node.outColor.connect(gammaCorrect.value, force = True)
        gammaCorrect.outValue.connect(outputConnection, force = True)
    else:
        gammaCorrect = nt.GammaCorrect(name = '%s_GammaCorrect' % nodeName)
        gammaCorrect.gamma.set(gammaCorrectValue)
        
        node.outColor.connect(gammaCorrect.value)
