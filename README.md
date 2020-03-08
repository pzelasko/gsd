# GSD
Get Speech Done: A collection of tools for speech models development

# Install

    # 1) Get the code
    git clone https://github.com/pzelasko/gsd
    cd gsd
    
    # 2) Create and activate a virtualenv or a conda env, and get dependencies
    
    # for virtualenv:
    pip install -r requirements.txt
    
    # for conda: 
    conda install --file requirements.txt 
    # however, it will likely fail on some dependencies
    # for now, you might need to remove them from requirements 
    # and manually install with pip
    
    # 3) Install the package
    pip install -e .
    
# Usage

The scripts in `gsd/commands` are added in PATH, so they can be executed like normal Unix commands in any directory, as long as the env is active.
