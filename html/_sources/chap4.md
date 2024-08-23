---
title: "Chapter 4"
exports:
  - format: tex
    logo: false
    template: ../templates/plain_latex_book_chapter
    output: exports/chap4.tex
---
<a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011484" class="prominent-link">
  <div class="prominent-link-title">Article Link</div>
  <div class="prominent-link-description">PLoS Computational Biology</div>
</a>

# A role for cortical interneurons as adversarial discriminators

_Foreword_

This chapter asks how the sensory cortex might learn representations of the external world. It is situated most closely to the field of artificial intelligence called, appropriately, representation learning. The goal of this chapter is to reconcile representation learning algorithms with biology, and thus act as hypotheses for sensory neuroscience. Broadly, it is an example of Role 4: machine learning as a model of the brain.

Representation learning is an old idea within AI. Here, a representation is defined as some transformation of sensory data into a new space. Principal Components Analysis (PCA), sparse coding, and k-means clustering are all examples of unsupervised representation learning algorithms. What is common to these algorithms is the existence of transformations both from data to a representation and from representation to data. 

When taken as a model of the sensory cortex, one must adopt a central dogma that the brain, too, forms various representations and can transform information between them. These transformations are presumed to be more complicated than e.g. in PCA. 

Temporarily bracketing the question of what these transformations might be, this chapter asks what neural circuits might be used to adjust and improve them towards their objective. This question is possible because the objective of representation learning has a general mathematical form that applies to many architectures and systems. This objective appropriately considers the uncertainty in choosing a correct representation. It represents a Bayesian framework for sensory processing and representation learning. 

This article also appeared as a preprint with the title (Learning to infer in recurrent biological networks)[https://arxiv.org/abs/2006.10811].
