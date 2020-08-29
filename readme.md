# Similar image recommender application based on Flask for Heroku deployment based on Resnet18 from PyTorch

This is a basic item-item recommender system implementation in Flask. 
Based on the resnet18 implementation from PyTorch it creates feature vectors from the input images, compares it to the other images and sorts for each image a similarity list. Eventually, the result is visualized for a tiny test set that is provided within the repository.


The implementation from this repository is described **in detail** in another article on Medium https://medium.com/@maciek.korzec/image-recommendations-with-pytorch-flask-postgresql-heroku-deployment-206682d06c6b

The overall theory for the core item-to-item image recommender system is explained here: https://towardsdatascience.com/effortlessly-recommending-similar-images-b65aff6aabfb

## Starting the application 

For this article I was using a Windows 10 machine and Python 3.5.4. I have left out any exception handling.

With new Python versions you might have problems running PyTorch
Needed libraries are listed in requirements.txt and need to be installed. This package runs on Heroku without problems in August 2020.

When you installed all packages in the right environment you can create the database with 

`flask createDB`

import the test data

`flask import DB`

and start the application with 

`flask run`

and you should be able to access it in your browser via 

`http://localhost:5000/`

Then you can browse the gallery and recommendations with the images provided in the repository.



## Getting pickle files for similar images and similarity values
In an earlier post I described the implementation for getting similar images out of a larger image set https://towardsdatascience.com/recommending-similar-images-using-pytorch-da019282770c

You can check-out the Jupyter notebook from my GitHub repository https://github.com/MathMagicx/JupyterNotebooks/tree/master/ImageRecommenderResnet18

If you run it with your own images it shall give you two pickle files in the main directory. These should be moved for the app to the folder 

imageRecommender\static\pickles

and the images to 

imageRecommender\static\site_imgs\images

However, if you intend to work with many images, you should change the implementation to work with object storage, for example.