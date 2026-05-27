**What does this project do**

This project uses a linear regression model to estimate someone's age based off of facial proportions. The theory was to reduce the dimensionality of the dataset to however many pixels the image has to a single feature, the ratio of the forehead to chin. As we grow, our bones get bigger, but some bones grow more than others. As a result, it was my belief that if we took the forehead to chin ratio we would have a machine that would be able to estimate someone's age fairly accurately up to about age 25 where bones stop growing. The graph of predicted versus actual age has a slope of .997 and a b value of 0.5. Which gets good results, however even though it works on average, the variability is high so this approach needs refinement. If you take 100 people and estimate their ages, the average age will be close to the true average but individual results could be off by decades. In addition, I tested this on myself where I intentionally jutted out my chin and was able to go from an estimated 26 years old to 116 years old. Interestingly enough, the variablility does not increase with age as I had predicted. The one feature I use is the forehead to jaw ratio, and I used it because as we grow from being an infant to being an adult, the jaw grows more than the forehead, but this process stops at around 25 so I thought the results would be accurate for minors but less accurate for the elderly but this assumption did not turn out to be correct. 

Still, as is, more features need to be considered if the age estimator were to be truely accurate. One idea is to somehow measure the texture of the skin, because as we age our bodies stop producing collagen, which is what causes our face to wrinkle.

**Instructions**

Have the UTKFace Dataset downloaded in same folder you have ageDetector.py loaded. then run the command: python ageDetector.py

It covers the entire dataset to Linear Regression model plus showing the results in matplotpy pipeline
