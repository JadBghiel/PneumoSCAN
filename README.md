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

Maybe it worked, maybe it didn't, i don't know, its still training.





## task 2

here is documentation on how to group text using scikit
[docs_link](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

here is a geekforgeek tutorial on how to do it:

[tutorial_link](https://www.geeksforgeeks.org/machine-learning/clustering-text-documents-using-k-means-in-scikit-learn/)


