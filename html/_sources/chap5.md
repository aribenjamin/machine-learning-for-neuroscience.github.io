---
title: "Chapter 5"
exports:
  - format: tex
    logo: false
    template: ../templates/plain_latex_book_chapter
    output: exports/chap5.tex
---
<a href="https://arxiv.org/abs/1805.08289" class="prominent-link">
  <div class="prominent-link-title">Article link</div>
  <div class="prominent-link-description">ICLR 2019</div>
</a>

# Measuring and regularizing networks in function space

_Foreword_

Deep learning provides a catalog of concepts for neuroscience. This chapter is about expanding that catalog. It is written for a deep learning audience, not neuroscience per se, and was published in a peer-reviewed deep learning conference . The motivating ideas are common to both fields. What are the available learning algorithms for neural networks? 

In deep learning, the algorithm of reference is gradient descent. However, one can make better choices than this. As I review in this chapter, most of deep learning now uses different algorithms in the same family (like Adam, RMSprop, or natural gradients). 

The insight of these methods is that all parameters are not equal. Some have a bigger effect on the output, and thus on the function encoded by the network. Yet gradient descent treats all parameters equally, in a sense, by measuring distances in parameter space. One can do better by using the space of functions (i.e. behavior). This chapter claims that this is a more natural way of thinking about learning.

Plasticity in the brain might be interpreted in this way, as well. Synapses that are very influential upon behavior (like those on a motor unit in the spinal cord) ought to change more slowly than other, less efficacious synapses. A solution to continual learning (not ‘catastrophically forgetting’ previous things) can also be derived with this function-space approach. As neuroscience discovers the brain’s learning algorithms, this concept may help to interpret what is found.
