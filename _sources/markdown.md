# Markdown Cells

Markdown Cells are cells that contain Markdown.  Markdown is a markup language that is used to format text. In this section
we are going to look at different formatting options to make our text more structured and user-friendly.  
To add a Markdown cell:  
1. Choose `Markdown` from the dropdown list in the notebook toolbar.
![type-code-cell](images/type-code-cell.png)
2. Then click on the **Add Cell Below** button ![](images/add-cell.png). 
3. This will add Markdown cell in your Jupyter Notebook. Click on the cell and start typing your Markdown.
4. Click on the **Run Cell and Select below** ![](images/run-cell.png) button in the notebook toolbar to run the code in that cell only, or **Run All** ![](images/run-all.png) button to run all the cells of the Notebook.


## Headings

Below is the Markdown code you need to use to specify headings at different levels and the rendered output respectively below the code:

`# Heading 1`

<p style="font-weight:500; font-size:34px">Heading 1</p>

`## Heading 2`

<p style="font-weight:500; font-size:30px">Heading 2</p>

`### Heading 3`

<p style="font-weight:500; font-size:24px">Heading 3</p>

`#### Heading 4`

<p style="font-weight:500; font-size:18px">Heading 4</p>

## Inline text formatting

To make text **bold** use `**double asterisks**` or `__double underscores__`.  
To make text *italic* use `*asterisks*` or `_underscores_`.  
To make text ^superscript^ use `^caret^`.  
To make text ~subscript~ use `~tilde~`.  
To mark text as `inline code` use `` `backticks` ``.   
To  ~~strikethrough~~ text use `~~double tilde~~`.

## Line breaks
To create a line break, put more than 2 spaces at the end of a sentence.

```{exercise-start} Markdown in Jupyter Notebook
:label: markdown1
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Replicate the output of the text below in a new Jupyter Notebook `notebook2`. 
![notebook_exercise1](images/notebook-exercise1.png)
The text comes from [a paper by Monya Baker](https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970) 
that was published in 2016 in the Nature journal that triggered the discussion about Reproducibility Crisis.

```{exercise-end}
```

## Links

### Linking text to Headers

To link text to a header use `[link to header](#section-title)`. Inside the parenthesis, titles are written in lower case letters
and spaces are converted to a hyphen, for example, `[link to header](#markdown-cells)` will be rendered as [link to header](#markdown-cells).

### Linking text to a webpage

To create a link to a webpage use `[text of link](https://jupyter.org/)`.  This is rendered as [text of link](https://jupyter.org/). 

## Footnotes

To indicate a footnote use`[^2]` and, for example, indicate another one as`[^3]`, then specify the wordings of the footnotes as:

`[^2]: This is the first footnote.`  
`[^3]: This is the second footnote.`

You do not need to put footnotes at the end of the document for them to be rendered there.  This example is rendered as follows:  

To indicate a footnote use[^2] and, for example, indicate another one as[^3] and then specify the wordings of the footnotes as:

[^2]: This is the first footnote.  
[^3]: This is the second footnote.

## Lists

### Ordered lists

To create an ordered list use the following syntax:

```
1. Item 1
2. Item 2
3. Item 3
```

This is rendered as:

1. Item 1
2. Item 2
3. Item 3

Use 4 spaces to indent an item if you would like to have sub-lists:
```
1. Item 1
2. Item 2
3. Item 3  
    a. Item 3a  
        i.  Item 3ai  
        ii. Item 3aii  
    b. Item 3b  
    c. Item 3c  
4. Item 4
```

1. Item 1
2. Item 2
3. Item 3  
    a. Item 3a  
        i.  Item 3ai  
        ii. Item 3aii  
    b. Item 3b  
    c. Item 3c  
4. Item 4

### Unordered lists

In an unordered bulletted list, each item begins with `*`, `+` or `-`.  Example:

```
* Item 1
* Item 2
* Item 3
    * Item 3a
        *  Item 3ai
        * Item 3aii
    * Item 3b
    * Item 3c
* Item 4
```
Will be rendered as:

* Item 1
* Item 2
* Item 3
    * Item 3a
        *  Item 3ai
        * Item 3aii
    * Item 3b
    * Item 3c
* Item 4

## Inserting images
To insert an image use the following syntax: `![alternative text](path_to_image "Title")`.  Example:

`![Jupyter Logo](images/jupyter.png)`

Will be rendered as:

![Jupyter Logo](images/jupyter.png)


```{exercise-start} More Markdown
:label: markdown2
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Continue working on `notebook2.ipynb` from the {numref}`markdown1`. Extend the output of `notebook2.ipynb` to look like
[this](notebook-solutions/notebook2.ipynb).  
You can find the image used in this exercise at this location:
https://www.nature.com/news/polopoly_fs/7.36716.1469695923!/image/reproducibility-graphic-online1.jpeg_gen/derivatives/landscape_630/reproducibility-graphic-online1.jpeg

```{exercise-end}
```
