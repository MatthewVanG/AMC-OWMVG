import unittest
import os 
import os.path
from webapp.antimonyTools import *
class testPythonFiles(unittest.TestCase):
    
    def testInit(self):
        dict1 = init('A,B', 'A', '10,2', 'C', 'C', '0', '3', False)
        dict = {
            'Reactants' : ['A', 'B'],
            'FixedReactants' : ['A'],
            'ReactantIC' : ['10','2'],
            'Products' : ['C'],
            'FixedProducts' : ['C'],
            'ProductIC' : ['0'],
            'Reversibility' : False,
            'RxnConstant' : ['3']
        }
        self.assertEqual(dict, dict1)

    def testResetFiles(self):
        resetFiles()
        self.assertTrue(os.path.getsize('webapp/static/antimony1.txt') == 0)
        self.assertTrue(os.path.getsize('webapp/static/antimony2.txt') == 0)


    def testReactionAntimony(self):

        dict = {
            'Reactants' : ['A', 'B'],
            'FixedReactants' : ['A'],
            'ReactantIC' : ['10','2'],
            'Products' : ['C'],
            'FixedProducts' : ['C'],
            'ProductIC' : ['0'],
            'Reversibility' : False,
            'RxnConstant' : ['3']
        }
        currentK = 0
        reactionAntimony(dict, currentK)
        self.assertFalse(os.path.getsize('webapp/static/antimony1.txt') == 0)

    def testConditionsAntimony(self):
        dict = {
            'Reactants' : ['A', 'B'],
            'FixedReactants' : ['A'],
            'ReactantIC' : ["10","2"],
            'Products' : ['C'],
            'FixedProducts' : ['C'],
            'ProductIC' : ["0"],
            'Reversibility' : False,
            'RxnConstant' : ["3"]
        }
        kList = ['k0']
        conditionsAntimony(dict, kList)
        self.assertFalse(os.path.getsize('webapp/static/antimony2.txt') == 0)
        
    def testRunSim(self):
        resetFiles()
        if (os.path.exists("webapp/static/output.jpg")):
            os.remove("webapp/static/output.jpg")
        runSim()
        self.assertTrue(os.path.exists("webapp/static/output.jpg"))

    def testLoadModel(self):
        resetFiles()
        file1 = open("webapp/static/test.txt", "r")
        file2 = open('webapp/static/antimony1.txt', "w")

        for line in file1:
            file2.write(line)
        file1.close()
        file2.close()
        
        loadModel()
        self.assertFalse(os.path.getsize('webapp/static/antimony1.txt') == 0)

    def testLoadSBML(self):
        resetFiles()
        if (os.path.exists("webapp/static/output.jpg")):
            os.remove("webapp/static/output.jpg")
        loadSBML("https://www.ebi.ac.uk/biomodels/model/download/BIOMD0000000090.2?filename=BIOMD0000000090_url.xml")
        self.assertTrue(os.path.exists("webapp/static/output.jpg"))

if __name__ == '__main__':
    unittest.main()