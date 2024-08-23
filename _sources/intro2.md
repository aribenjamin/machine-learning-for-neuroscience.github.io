---
title: "Introduction: Section 2"
exports:
  - format: tex
    logo: false
    template: ../templates/plain_latex_book_chapter
    output: exports/intro2.tex
---

# Learning and its consequences

Complex systems can emerge from simple rules. Recently, some in computational neuroscience have argued to shift the focus away from the computations performed in the brain and towards how they are learned (Lillicrap & Kording, 2019; Richards et al., 2019). Proponents of this shift often argue that in ANNs, the emergent computation is much more difficult to understand than the factors set by the practitioner – the architecture, the learning objective, and the learning algorithm. The same may be true of brains. Rather than deconstructing the computation of networks, this effort seeks to understand how they learn and to what ends. It is a ‘deep learning framework’ for neuroscience. 

A deep learning framework is not an effort to map the components of modern deep learning systems onto the brain. Rather, it means adopting a computational language developed by machine learning and statistical learning theory – disciplines that are concerned with describing learning and learnability in the abstract. This rich language has enormous potential to help understand how brains learn and how this shapes the meaning of neural activity.

In Section 2 of this dissertation, I embrace this approach to understanding the brain in the course of three chapters. These projects each use deep learning models and theory in order to reason about learning in the brain. Each takes up one of the following questions: what are potential learning objectives for sensory cortex? What are potential learning algorithms? And what are the sensory consequences for having learned with such algorithms? 

### A learning objective: representation learning

One of the core concepts in a learning framework is the objective or goal of learning. This is a teleological interpretation of neuronal plasticity. Much of this dissertation focuses on perception. What is the objective of plasticity in sensory cortex? 

In Chapter 5, I examine the hypothesis that the sensory cortex aims to form internal representations of the external world. This objective of representation learning is central concept in neuroscience (though not without critique (Baker, Lansdell, & Kording, 2021; Brette, 2019)). As commonly defined, representations are transformations of sensory data into forms that are more useful to an organism. Good representations might highlight the true organizing principles of the world (Kersten, Mamassian, & Yuille, 2004) or encode information as best as possible while using minimal energy (Barlow, 1961). In this broad frame, the goal of sensory learning is to form useful representations.

Representations are also key concept in machine learning. There, many works have attempted to formalize how to produce useful representations. One popular approach imagines that good sensory systems first create a model of the sensory world, and then infer the representations in that model that explain sensory data (Yuille & Kersten, 2006). Perception might be like a video-game rendering engine with representations of the lighting, materials, and objects that best explain a visual scene; a ‘simulation in the mind’ (Ullman, Spelke, Battaglia, & Tenenbaum, 2017). Many different types of models are possible, making this a general and flexible way to describe representations. 

What would be required if the brain learns representations in this way? In this Chapter, I aim to characterize the specific problems that this introduces for neural circuits. I then develop theories about possible solutions that may be taken by sensory cortex. These theories draw from machine learning techniques for representation learning, but are adapted so as to serve as biological hypotheses. The goal is to evaluate whether this class of objectives is a candidate for a description of the objective of sensory learning.

### A learning algorithm: improving upon gradient descent

A learning algorithm is a set of rules prescribing how a system ought to change over time. A deep learning framework for neuroscience aims to build a computational understanding of the brain’s learning algorithms, abstracted from the level of synaptic plasticity and its cellular implementation. Because this effort is in its infancy, a crucial first step is to identify and understand the candidate algorithms.

Chapter 6 represents a foray into the fields of deep learning optimization and deep learning theory. These fields have identified algorithms that work well on deep learning systems, and then sought to understand why they work. The baseline algorithm is gradient descent, in which all parameters change proportional to their effect upon the output. Yet in deep learning, almost all papers now use different algorithms that, in practice, produce better networks with less training data. This chapter discusses a theoretical perspective on algorithms that improve upon gradient descent, and then uses this to derive a new algorithm for learning. 

Of all that machine learning has to offer a neuroscience of learning, perhaps the most important is simply a recognition of how difficult and unlikely learning really is. Like scientists pulling general knowledge from limited experiments, learning systems must pull generalities from limited experience. This requires making assumptions (David H. Wolpert & Macready, 1997). In deep learning systems, the assumptions come as much from the learning algorithm as the constraints of the system itself (Zhang, Bengio, Hardt, Recht, & Vinyals, 2021). Somehow, on certain problems, learning algorithms ‘choose’ to learn knowledge that generalizes well. The network, algorithm, and data conspire together for effective learning. Since the brain, too, has a staggering amount of plastic parameters, the theories that describe why ANNs generalize are likely to be useful for describing why we learn so effectively, too. 

### The sensory consequences of learning algorithms

A deep learning framework does not require abandoning a study of responses for a study of objectives and algorithms. Understanding learning may be the best ways to gain insight about responses, as well. This requires that bridges be built between neuroscience and deep learning theory.

An important lesson of deep learning is that the learning algorithm leaves permanent traces upon the network and the function it implements. The algorithm is not an incidental and ultimately ignorable process. The traces left by are learning are in fact so important that useful learning in large neural networks is not possible without them (Zhang et al., 2021). These traces are the bias of the learning algorithm, which are effectively assumptions about what is important to learn. As mentioned in the previous section, such assumptions are necessary for learning. Neural network representations thus must carry the imprint of algorithms that generalize well from limited data. 

This perspective is new to neuroscience. Usually, when explaining why neural representations take one form or another, neuroscience reaches to normative explanations and describes how the adult representation is optimal in some sense. A hypothesis of this flavor is that sensory representations minimize the number of spikes required to encode external information because of evolutionary pressure on energy usage (Bruno A. Olshausen & Field, 1996; Rao & Ballard, 1999). Though pressures like this certainly exist, there also exists an evolutionary pressure to learn effectively as an infant. Explaining adult representations via their emergence from effective learning algorithms introduces a new type of explanation, this time referencing machine learning theory.

In Chapter 7, I show how such ideas can explain a set of findings in psychophysics and neurophysiology about sensory representations. In humans and other animals, sensory systems tend to better encode the features of the world that are more common, especially for low-level features like orientation and color (Wei & Stocker, 2017). In information theory, such a strategy represents an efficient code – a code that makes best use of a channel with limited capacity. In a collaboration with the lab of Alan Stocker, we use artificial neural networks as model systems to demonstrate that gradient descent learning naturally results in efficient codes, as well. 

Learning in the brain is unlikely to be gradient descent, precisely, but a similar principle is likely to be in play. As the algorithms of sensory learning come into focus for neuroscience, it will be interesting to describe how these shape what our brains choose to learn from experience.

## Summary and outlook

To understand neural computation, a learning framework looks to its source. Yet, like computation, learning can be understood at many levels. A deep learning or machine learning framework for neuroscience aims for a high-level, normative understanding in terms able to be abstracted from the brain’s implementation.

The projects in this dissertation endeavor to use modern theories of machine learning to advance neuroscience. Along the way they engage with a number of leading theories of sensory processing, asking, always, how might these be learned? To find answers, I pull ideas from multiple subfields of artificial intelligence, from optimization to generative adversarial networks to deep learning theory. These machine learning perspectives offer new types of explanations and predictions for neuroscience.


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
