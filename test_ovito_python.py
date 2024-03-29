from ovito.data import *
from ovito.io import import_file
from ovito.modifiers import CalculateDisplacementsModifier, ExpressionSelectionModifier, InvertSelectionModifier, DeleteSelectedModifiern
def modify(frame, data):
    
    # This user-defined modifier function gets automatically called by OVITO whenever the data pipeline is newly computed.
    # It receives two arguments from the pipeline system:
    # 
    #    frame - The current animation frame number at which the pipeline is being evaluated.
    #    data   - The DataCollection passed in from the pipeline system. 
    #                The function may modify the data stored in this DataCollection as needed.
    # 
    # What follows is an example code snippet doing nothing except printing the current 
    # list of particle properties to the log window. Use it as a starting point for developing 
    # your own data modification or analysis functions. 
    
    if data.particles != None:
        print("There are %i particles with the following properties:" % data.particles.count)
        for property_name in data.particles.keys():
            print("  '%s'" % property_name)
    
def select_jumping_atoms (file):
    pipeline = import_file()
    print(str(pipeline.source.num_frames)+ 'frames')
    pipeline.modifiers.append(CalculateDisplacementsModifier())
