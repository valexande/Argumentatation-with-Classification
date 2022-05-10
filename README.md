# Argumentatation-with-Classification
This repository is for the Argumentation Framework with Attack Classifiation that was submitted at the Journal of Logic and Information


- .idea and venv are configuration files for the virtual environment needed by pycharm.

- MAAFSemantics file contains the ASP code for each extension. The files are named in a manner which makes clear which file corresponds to which extension.

- asprin-master file contains the source code that Potassco provides for the asprin module. Notice that asrpin needs clingo 5.4 to run, for 5.5 is not compatible yet.

- asp&AAFD_API contains the web api. One can built locally the web interface from her/his computer (i.e., the server will be at your computer), only by executing the api.py file. The api will then run at IP.8888, where IP is your IP. Moreover, notice that asprin needs clingo 5.4 therefore !!before executing for the first time the api.py file!!, shoot the command "conda create --name asprin -c potassco asprin" in the cmd of the editor you are using.


It is a Python project, thus we recommend PyCharm to run locally the api. At least that is what we did.


The project now runs at http://155.207.131.42:5000/ or http://argumentation.csd.auth.gr:5000/

#Due to security reasons the server was down for some time, if you want to try the application please send as a mail at valexande@csd.auth.gr, so that we will give the new credentials.
