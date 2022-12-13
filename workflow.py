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
    
    serving_3 = funcs['test'].as_step().after(serving_2)
    
    asdsad = funcs['test'].as_step()
    
    adsad_1 = funcs['test'].as_step().after(asdsad)
    
    adsad_2 = funcs['test'].as_step().after(adsad_1)
    
    adsad_3 = funcs['test'].as_step().after(adsad_2)

    
    safsaf = funcs['test'].as_step()
    
    safff_1 = funcs['test'].as_step().after(safsaf)
    
    sfsf = funcs['test'].as_step().after(safff_1)
    
    eeeee = funcs['test'].as_step().after(sfsf)

    
    rrr = funcs['test'].as_step()
    
    rrfafa = funcs['test'].as_step().after(rrr)
    
    www = funcs['test'].as_step().after(rrfafa)
    
    rrtw = funcs['test'].as_step().after(www)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving_3 = funcs['test'].as_step().after(serving_2)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving_3 = funcs['test'].as_step().after(serving_2)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving_3 = funcs['test'].as_step().after(serving_2)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving_3 = funcs['test'].as_step().after(serving_2)
    
    serving = funcs['test'].as_step()
    
    serving_1 = funcs['test'].as_step().after(serving)
    
    serving_2 = funcs['test'].as_step().after(serving_1)
    
    serving_3 = funcs['test'].as_step().after(serving_2)
    

