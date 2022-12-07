# AMC-OWMVG
## Antimony Model Creator - Olivia Walsh, Matthew Van Ginneken

This package allows the user to visualize a reaction via a steady state graph.  The user can create and submit their own reactions on the Flask Webpage, or they can submit an antimony txt file or a SBML file also through the webpage.  The Webpage will run a simulation using the reactions with tellurium and show the steady state graph.  

### Installation

To install this package the user should open up to their terminal and navigate to the directory of choice (example below to get to Desktop)
> cd Desktop

Next the user must use a pip installation of the program
> pip install AMC-OWMVG

Once the terminal has confirmed installation, the user must make a python file and fill it with the following code. Then they execute their python file using either a terminal or IDE. 
>    import AMCowmvg as AMC
>    AMC.runApp()

This will produce a few lines of response including a website link, the user should copy and paste this into their browser.