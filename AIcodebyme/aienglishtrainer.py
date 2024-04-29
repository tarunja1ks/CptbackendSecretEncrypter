from aienglish import aienglish
import pickle
airunner=aienglish() # this is script for retraining the model any time I want for improving score reports with modficiations
airunner.preprocess()
airunner.train() 
airunner.export()


