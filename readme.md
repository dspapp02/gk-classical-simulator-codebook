# Gottesmann-Knill Codebook

This is a codebook designed to be presented alongside or to supplement an introduction to the Gottesmann-Knill theorem / stabiliser formalism. It serves to demonstrate the polynomial time scaling of the formalism in simulating quantum states. It should be accompanied by an appropriate proof of the theorem. 

The codebook (to the extent it is finished) complete. It can be presented as is, or the logic of certain functions can be removed to provide a brief, simple coding challenge. It is also designed to prioritise a pedagological approach to building a simulator. It explicitly does not employ a more efficient stabiliser tableau for state and operator representation. 

This codebook is being developed for an upcoming workshop on the subject. The aim of the workshop will be both an introduction to classical simulation, but also a means to encourage discussions on the quantum-classical boundary. The codebook demonstrates that in certain cases 'quantum' phenomena, such many-body entanglement and contextuality, can be efficiently simulated. As such, determining where quantum advantage arises is not as simple as one might originally think. 

Prerequisites:
    -Python
    -numpy
    -A Jupyter-compatible environment (such as JupyterLab, VS Code with the Jupyter extension or Google Colab)

## Status:

The project is a work in progress. 

### To-dos

    -Bug testing current output
    -Complete measurement simulation code
    -Complete state validation in polynomial time
    -Add test cases and complexity plots to demonstrate polynomial scaling
    -Second pass of ancillary text
    -Class for simulation of mixed states?
