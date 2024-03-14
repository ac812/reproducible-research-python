# Introducing PyCharm

If you have a large amount of Python code, using an Integrated Development Environment (IDE) could be more beneficial. An 
IDE is a tool that enables programmers to write code productively by combining different
tools and resources that are commonly used when writing code, into one application.  Below are instructions on how to create
Jupyter Notebooks in PyCharm.  There are several other popular tools used to code Python.  We will be using
PyCharm as it is one of the most popular tools used to develop Python code (the top one according to the 
[Python Software Foundation survey](https://www.jetbrains.com/research/python-developers-survey-2018/)). It is a tool used not just in 
academia but also in industry by small to big companies.


## Creating a Project in PyCharm

Before writing code in Python, we need to create a project in PyCharm.  A project allows you to keep track of 
the files and environment associated to your code. 

````{card} Steps to create the PyCharm Project:
{bdg-primary}`PyCharm`
1. In PyCharm's Welcome screen, click **New Project**.
2. Choose **Pure Python** to create a Python project.  Choose the location of the project in the **Location** field.  
Name your project `myFirstProject`.
3. Choose **Conda** in the **New environment using** field as shown below.
![pycharm_project](images/project1.png)
4. Now click the **Create** button to create the project.
````

## Creating Jupyter Notebooks in PyCharm
Now let us get started and see how we can create Jupyter Notebooks in PyCharm.  

To create a new Jupyter Notebook:  
1. Select **File|New|Jupyter Notebook** from PyCharm's main menu.  
![notebook_file](images/notebook-menu.png)
2. Enter `notebook1` as the name your new Jupyter Notebook.
![notebook_name](images/notebook-name.png)
3. The Jupyter Notebook is now displayed in PyCharm. If this is your first time creating a Jupyter Notebook in PyCharm, 
most likely you will get a message at the top of Jupyter Notebook file saying that "Jupyter is not installed". If so,
click on the **Install Jupyter** link on the right hand side. This will install the package `Jupyter`.
![jupyter-install](images/jupyter-install.png)
When this is installed, you would be able to add content to your Jupyter Notebook file.


```{exercise-start} Creating Notebooks in PyCharm
:label: pycharm-notebook
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Edit `notebook1` and write the code shown in {numref}`jupyter-code-cell`, and execute it in a Jupyter Notebook.

```{exercise-end}
```


