
conda create --name posnetworkENV
conda env remove -n posnetworkENV 


conda install python=3.7.3
conda activate posnetworkENV

conda deactivate

conda config --set allow_conda_downgrades true
