**What does this project do**

This project uses a linear regression model to estimate someone's age based off of facial proportions. The theory was to reduce the dimensionality of the dataset to however many pixels the image has to a single feature, the ratio of the forehead to chin. As we grow, our bones get bigger, but some bones grow more than others. As a result, it was my belief that if we took the forehead to chin ratio we would have a machine that would be able to estimate someone's age fairly accurately up to about age 25 where bones stop growing. The graph of predicted versus actual age has a slope of .997 and a b value of 0.5. Which gets good results, however even though it works on average, the variability is high so this approach needs refinement.

**Instructions**

Have the UTKFace Dataset downloaded in same folder you have ageDetector.py loaded. then run the command: python ageDetector.py

It covers the entire dataset to Linear Regression model pipeline
