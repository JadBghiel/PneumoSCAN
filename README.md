# CVRIE

## task 1

note: i put the old multi class [notebook](Supervised/image_classification_supervised.ipynb) in gitignore as we no longer need it everything is in the supervisd file (3 models and 1 for )


run the [image_classification_pneumonia](Supervised/image_classification_pneumonia.ipynb) file
- it has 3 model (one of them k=5 clusters)
- with clear viz and output
- its done






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
- touch on other aspect a part from the accuracy result, the speed etc (explain in the markdown)
- do eveyting for every model of everytask documented well everything
- compare our notebook with other people notebook i have link: jad do it (find another model online that does the same thing in this case for task 1: supervised its finding diseases in the chest IRM imagery)
- model quality and insight: have a propse solution for the classifed problem
- have gained insight on the issue of our dataset
- reference real research on the topic of the dataset
- on the unsuprvised part we need to jusityf the clusters, need to choose how many cluster not random its a stander do research and jusutfu the number of clusters (we need 1 model with 5 clusters) the rest can have whatver its fine no need to overdo it 
- when possible after each codeblock have a matplotlib visuatltion and the output and a markdown explaining it (the things i said before such as the speed the accuracy any notes etc)




- unsupervied: at least 4 improvements, that can be shown and explained/jusitife din the notebook
- use the ideal number of clusters NOT 5
- put unseend data in the new clusters, can u write a new testiminy of tbe new clsuter ? do these eperiemnt 5 times
- using only the easy data in 9 clusters, what % of the easy data are we able to cluster correclty ? 

## THE NOTEBOOK MUST BE THROG PLEASE MAKE IT AS COPLETE AS POSSIBLE AND GOOD LOOKING AND USE MATPLOTLIB AND ERROR MESSAGE AND OUTPUT WELL DONE PLEASE


# SECOND FOLLOW UP TODO FOR THE FINAL DEFENSE:
SUPERVISED: JAD
- explain in more details how the models works conceptually, the more info and explanation the better
- explain better the loss function
- metion that online notebook with for penumnia 
- provide context of the disease, a bit of info, les enjeux
## jad: done

UNSUPERVISED: ALRIK
- add a desc 
- how do i measure my success ? -> add a seciton to epxlain - silouhette score like guess how many diff clusters
- at least presnt 4 improvements made during the training that improved the result (rn we have 2 add 2 more)
- uses the correct amount of clusters (we guessed 19), its less than 19, oriol hinted at 9 cluster, he finna give a csv file with 9 clusters apparently