# CVRIE

## task 1


run the image_classification.ipynb

when testing on things like pneuomina, whic only have a yes or no and are pretty easy to check even with the naked eye if the patient has pneumonia, we can easily acheive accuracy of up to 96%.

However, when checking images that have multipe choices (meaning that it can be multiple deceases, not just sick or not sick), things get much more complex, much more quickly. With these types of images, i struggle to get even above 50% accuracy, even with huge datasets and long training times.

I decided to check chest images, because contrary to the rest, they havequite a few options, and sometimes, a patient can have multile diseases at once, greatly increasing complexity, so that seemed like a func challenge.


I then tested with multiple different ways of train ing ml to see what performed best.

i first tested with the random tree permutation model, but that performed increadibly badlly.
The model would simply pick one disease at random, (usually the one that i gave that had the most examples), and simply say that every image had this disease.
To avoid this, i went back to svc search since it had performed so well when faced with binary decisions. to avoid confusing it with multiple decisions, as i would surely have to do if i put all 14 options (13 diseases + no disease), i reduced it to 3 options (disease_1, disease_2, no disease).

It got 51% (so better than random since random would be 33%)





## task 2

here is documentation on how to group text using scikit
[docs_link](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

here is a geekforgeek tutorial on how to do it:

[tutorial_link](https://www.geeksforgeeks.org/machine-learning/clustering-text-documents-using-k-means-in-scikit-learn/)



# DEFENSE TODO for tasl 1 and 2
- well structured
- can be flowed throuhg w/ errors
- each aprt of the notebook ahve explanation, codeblack vizualiton and output
- matplotlib use need to be beautiful
- please respecr the notebook

MiSSING these:
- at least 3 model on the same dataset (add regression) and eplxained the best chouce in the notebook
- re push the old dataset ??
- give a good exlpantion on how the selected model perform and why we choose it
- give a good explanation on its loss function
- touch on other aspect a part from the accuracy result, the speed etc 
- do eveyting for every model of everytask documented well everything
- compare our notebook with other people notebook i have link: jad do it
- model quality and insight: have a propse solution for the classifed problem
- have gained insight on the issue of our dataset
- reference real research on the topic of the dataset
- on the unseorived part we need to jusityf the clusters, need to choose how many cluster not random its a stander do research and jusutfu the number f clusters (5 i think its between 5 and 10)
- unsupervied: at least 4 improvements, that can be shown and explained/jusitife din the notebook
- use the ideal number of clusters NOT 5
- put unseend data in the new clusters, can u write a new testiminy of tbe new clsuter ? do these eperiemnt 5 times
- using only the easy data in 9 clusters, what % of the easy data are we able to cluster correclty ? 

## THE NOTEBOOK MUST BE THROG PLEASE MAKE IT AS COPLETE AS POSSIBLE AND GOOD LOOKING AND USE MATPLOTLIB AND ERROR MESSAGE AND OUTPUT WELL DONE PLEASE