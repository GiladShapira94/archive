from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

funcs = {}

# init functions is used to configure function resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(auto_mount())

@dsl.pipeline(
    name="Testing Conditions",
    description="Testing Conditions"
)

def kfpipeline():
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)

    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)

    

