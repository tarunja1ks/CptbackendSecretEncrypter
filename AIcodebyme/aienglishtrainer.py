from aienglish import aienglish
import pickle
airunner=aienglish() 
airunner.preprocess()
airunner.train() 
airunner.export()


