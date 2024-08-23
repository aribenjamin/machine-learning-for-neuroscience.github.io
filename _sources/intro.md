---
title: "Introduction"
exports:
  - format: tex
    logo: false
    template: ../templates/plain_latex_book_chapter
    output: exports/intro.tex
---

# Introduction

Neural network models are playsets for a young neuroscience. They are simpler arenas in which to grow and to theorize. They allow neuroscience to apply its paradigms and, with complete access and control, see what can be learned. 

Neural networks embody a commitment to understanding the brain in the lens of its function. For this aim, it helps to have some knowledge of what it takes to engineer that function. For example, the organization of spider silk might be understood by how it supplies strength to keep its shape, lightness to reduce its weight, and toughness to resist a break, all of which are concepts from mechanical engineering (Keten, Xu, Ihle, & Buehler, 2010). Similarly, learning in animals might be  best understood using concepts from the engineering of learning machines (Marblestone, Wayne, & Kording, 2016). 

The discipline concerned with engineering learning, and which may teach neuroscience something, is of course machine learning. This includes knowledge about the obstacles that make learning from expe rience difficult. These problems have been solved, somehow, by evolution. Finding nature’s solutions to the problems of learning (as defined by machine learning) is a higher-level, more normative approach than is traditional in neuroscience. It does not begin from synaptic plasticity, for example. Instead, this approach describes what is necessary of learning in the abstract and what this means for hypotheses of learning in the brain.

A focus on neural networks also represents an embrace of complexity. In artificial intelligence, the desired programs (for example, successfully playing Go at super-human levels) are often too complex to be listed as a set of human-intelligible rules. The engineering solution is to instead design a training regimen for a neural network and let a computation emerge. Recently, some in computational neuroscience have argued to similarly shift the focus of research away from describing computations and instead focus on the processes by which they arise (Richards et al., 2019). These many be easier to discover and describe at an abstract level, assuming the right theoretical language is used.

This shift has its roots in an old controversy in neuroscience. How complex is neural computation, exactly, and what does this mean about how we, as neuroscientists, should understand it? In sensory processing and in particular the neurophysiology of early vision (long a model for neuroscience practice), neural computation has been argued to be both too complex for common methods (Bruno A Olshausen & Field, 2005) and within reach (Rust & Movshon, 2005). Time has not resolved the argument, although new methods as well as arguments from machine learning are now adding weight to complexity’s side (Cadena et al., 2019; Lillicrap & Kording, 2019). This dissertation begins with two studies that add to this ongoing and field-wide debate. Specifically, these introduce tools that evaluate the success of techniques for understanding neural responses, paying particular attention to the neurophysiology of vision. These studies provide a grounding for a broader discussion about which methods for understanding neural computation are likely to be fruitful.

This dissertation is organized into two sections. Section 1 discusses complexity within the practice of neurophysiology. These studies center the use of machine learning techniques as tools. Section 2 deals with neural network models of learning and perception. This work is situated between artificial intelligence and neuroscience, and asks, broadly, how these disciplines can mutually benefit. 

## References

Aljadeff, J., Lansdell, B. J., Fairhall, A. L., & Kleinfeld, D. (2016). Analysis of neuronal spike trains, deconstructed. Neuron, 91(2), 221-259. 

Baker, B., Lansdell, B., & Kording, K. (2021). A philosophical understanding of representation for neuroscience. arXiv preprint arXiv:2102.06592. 

Barlow, H. B. (1961). Possible principles underlying the transformation of sensory messages. Sensory communication, 1(01). 
Brette, R. (2019). Is coding a relevant metaphor for the brain? Behavioral and brain sciences, 42. 

Cadena, S. A., Denfield, G. H., Walker, E. Y., Gatys, L. A., Tolias, A. S., Bethge, M., & Ecker, A. S. (2019). Deep convolutional models improve predictions of macaque V1 responses to natural images. PLoS Computational Biology, 15(4), e1006897. 

Goh, G., Cammarata, N., Voss, C., Carter, S., Petrov, M., Schubert, L., . . . Olah, C. (2021). Multimodal neurons in artificial neural networks. Distill, 6(3), e30. 

Jonas, E., & Kording, K. P. (2017). Could a neuroscientist understand a microprocessor? PLoS Computational Biology, 13(1), e1005268. 

Kersten, D., Mamassian, P., & Yuille, A. (2004). Object perception as Bayesian inference. Annu. Rev. Psychol., 55, 271-304. 
Keten, S., Xu, Z., Ihle, B., & Buehler, M. J. (2010). Nanoconfinement controls stiffness, strength and mechanical toughness of β-sheet crystals in silk. Nature materials, 9(4), 359-367. 

Lillicrap, T. P., & Kording, K. P. (2019). What does it mean to understand a neural network? arXiv preprint arXiv:1907.06374. 

Marblestone, A. H., Wayne, G., & Kording, K. P. (2016). Toward an integration of deep learning and neuroscience. Frontiers in Computational Neuroscience, 94. 

Olah, C., Mordvintsev, A., & Schubert, L. (2017). Feature visualization. Distill, 2(11), e7. 

Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. Nature, 381(6583), 607-609. 

Olshausen, B. A., & Field, D. J. (2005). How close are we to understanding V1? Neural computation, 17(8), 1665-1699. 

Olshausen, B. A., & Field, D. J. (2006). What is the other 85 percent of V1 doing. L. van Hemmen, & T. Sejnowski (Eds.), 23, 182-211. 

Rao, R. P. N., & Ballard, D. H. (1999). Hierarchical Predictive Coding Model Hierarchical Predictive Coding of Natural Images. Nature Neuroscience, 2(1), 79-87. 

Richards, B. A., Lillicrap, T. P., Beaudoin, P., Bengio, Y., Bogacz, R., Christensen, A., . . . Ganguli, S. (2019). A deep learning framework for neuroscience. Nature Neuroscience, 22(11), 1761-1770. 

Rieke, F., Warland, D., Van Steveninck, R. d. R., & Bialek, W. (1999). Spikes: exploring the neural code: MIT press.

Rust, N. C., & Movshon, J. A. (2005). In praise of artifice. Nature Neuroscience, 8(12), 1647-1650. 

Ullman, T. D., Spelke, E., Battaglia, P., & Tenenbaum, J. B. (2017). Mind games: Game engines as an architecture for intuitive physics. Trends in cognitive sciences, 21(9), 649-665. 

Wei, X. X., & Stocker, A. A. (2017). Lawful relation between perceptual bias and discriminability. Proceedings of the National Academy of Sciences of the United States of America, 114(38), 10244-10249. doi:10.1073/pnas.1619153114

Wolpert, D. H., & Macready, W. G. (1997). No free lunch theorems for optimization. IEEE transactions on evolutionary computation, 1(1), 67-82. 

Yuille, A., & Kersten, D. (2006). Vision as Bayesian inference: analysis by synthesis? Trends in cognitive sciences, 10(7), 301-308. doi:10.1016/j.tics.2006.05.002

Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O. (2021). Understanding deep learning (still) requires rethinking generalization. Communications of the ACM, 64(3), 107-115. 

