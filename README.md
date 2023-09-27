# phys-231-exercises -- fall semester 2023

Repository for the exercise sessions for the phys-231 class at EPFL, fall semester 2023.

## How to generate links to open the notebooks in noto@epfl

[Noto](https://www.epfl.ch/education/educational-initiatives/jupyter-notebooks-for-education/one-click-access-to-jupyter-notebooks-online-with-noto/) is EPFL's version of Google colab.
It allows to edit and run jupyter notebooks easily. 

To generate a link that opens noto, automatically clones (or pulls) this repo, and opens a given notebook, you can use this [link generator](https://nbgitpuller.readthedocs.io/en/latest/link.html), with parameters

    JupterHub URL: https://noto.epfl.ch
    Git repository URL: https://github.com/SPOC-group/phys-231-exercises
    Branch: main
    File to open: path to the notebook that must be opened, relative to the root of the git directory. For example "lecture1/file_name.ipynb"
    Application to open: JupyterLab
    Named Server to open: blank

Then, [GO EPFL](https://go.epfl.ch) can be used to generate a shorter version of the link.
