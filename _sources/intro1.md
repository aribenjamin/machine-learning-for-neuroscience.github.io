---
title: "Introduction: Section 1"
exports:
  - format: tex
    logo: false
    template: ../templates/plain_latex_book_chapter
    output: exports/intro1.tex
---

# Neurophysiology practice and the complexity of sensory cortex 

What is the meaning of the activity of single neurons in the visual cortex? This question has been the subject of some of the most intense and dedicated study in all of neuroscience. In the tradition of Hubel and Wiesel, a predominant approach has been to present visual stimuli to animals while electrically recording the activity of neurons, and then to describe a model (conceptual or mathematical) that describes when neurons typically fire. This approach has been successful in revealing many unexpected aspects about what happens during vision, and it remains a mainstay of the perceptual neurosciences. 

Arguably the central difficulty for single-neuron neurophysiology that one only records the responses to the select stimuli shown in the experiment. One cannot show all possible stimuli. From these concrete instances, the challenge is to extract an understanding that is more general. This perennial problem for the sciences (and epistemology, no less) carries precise meaning for neurophysiology. Given some observations, one should say something about the response to different stimuli than those shown. Models and descriptions necessarily generalize from limited instances.

Most critiques of typical methods for neurophysiology are critiques of an overgeneralization of experimental results that create a misleading or false picture of neural function. In their “neurophysiology” of a microprocessor, for example, Jonas & Kording illustrate such overgeneralization in practice (Jonas & Kording, 2017). After observing that the voltage of a transistor correlates with an action in a video game, one could overgeneralize to say that the transistor’s “role” is to encode that action. This is an extrapolation and, in this case, an incorrect one. Olshausen & Field have also highlighted problems of overgeneralization in the study of V1 responses (Bruno A Olshausen & Field, 2005, 2006). They argue that experiments are systematically biased towards certain inputs (simple and artificial stimuli) as well as certain neurons (those with high firing rates on those stimuli), which results in failures when generalizing to other contexts. In light of these critiques, the onus lies with neurophysiology to establish exactly how far our models generalize, or in other words, to prove that an experiment does in fact establish the meaning of neural activity.

Statisticians and epistemologists alike recognize that generalizing from limited experience requires assumptions. What are the assumptions of typical approaches in neurophysiology? How might these assumptions be empirically verified? The concrete aim of Section 1 is to introduce tools for verification for neurophysiologists that quantify how much a model will generalize. The two sets of methods that I will focus on are tuning curves and more broadly encoding models. 

### Chapter 2: Tuning curves

A tuning curve characterizes whether or not a neuron is “tuned for” a variable describing the sensory world, like a tuning fork might be tuned for a particular acoustic frequency. Tuning curves clearly have meaning with regards to the stimuli and responses from which they were constructed, but what meaning do they have about how the brain processes other stimuli? Often, the interpretation is quite general. If a neuron responds strongly to certain orientations of a bar of light, it might be said to encode whether that orientation is present in its receptive field (in general). If this interpretation is taken, it implies a strong assumption about the meaning of neural activity in other contexts. 

In Chapter 2, I present a method that allows testing the assumption that tuning curves generalize beyond the laboratory context. Specifically, this is a method to estimate tuning from responses in more complicated contexts, and in particular naturalistic stimuli. This technique was demonstrated in a collaboration with Prof. Matthew Smith of Carnegie Mellon University for tuning to hue in macaque area V4. By testing for a change of tuning with context, one can assess whether this description of activity is a correct generalization from responses to laboratory stimuli.

### Chapter 3: Encoding models

Tuning curves are just one type of encoding model, statistical models for describing a neural response in terms of the stimulus. An encoding model takes as its central metaphor the idea of a “neural code”, that activity is like a cipher for sensory information (Aljadeff, Lansdell, Fairhall, & Kleinfeld, 2016; Rieke, Warland, Van Steveninck, & Bialek, 1999). Whereas tuning curves are built by directly tabulating the stimulus/response function, encoding models may also be obtained by fitting regression models. Different assumptions can be made depending on the form of the regression. Most often neurophysiologists select models by considering ease of use, interpretability, and the quantitative success of fitting neural activity.

In Chapter 3, I describe a method that can verify that the assumptions embedded in an encoding model are well-suited for the neurons in question. This approach is simple in principle: apply the methods and techniques of black-box machine learning to predict neural activity, and then take this predictive ability as a performance benchmark for simpler, hypothesis-driven statistical models. This approach circumvents some of the drawbacks of other standard verification methods, such as repeating a stimulus multiple times to establish the noise level. If performance is near the benchmark, one can be more confidence that a statistical description of neural activity is an accurate one.

## Summary

Tuning curves and encoding models make assumptions about neural activity in other contexts. These assumptions are necessary but must be verified in order to be trusted. Each project in Section 1 introduces a tool for such a verification as well as demonstrations on recordings of single neurons in macaque cortex. 

Such verifications provide an opportunity for an honest evaluation of encoding models in future experiments, and also inform a broader discussion about encoding models and their interpretation. In general, given a new tuning curve or encoding model of cortical activity, how much should a neurophysiologist that summarizes a general computation? This is a generalization of past experiments to future, unperformed experiments. Since even generalizations about generalizations require assumptions, neuroscience must consider arguments for the likely form and complexity of sensory processing. 

## Outlook: how might we understand an artificial neural network?

Neurophysiology ought to be easy in artificial neural networks (ANNs). There are no unobserved confounds like attention or neuromodulation. All nodes are perfectly visible and there are no hidden variables. How well might a neurophysiologist succeed at parsing the meaning of units in these networks?

This is not purely hypothetical; many in artificial intelligence have attempted such a thing. Scientists have ported over methods such as tuning curves to see what might be illuminated (Goh et al., 2021). New methods have also been developed, such as visualizing the stimuli that maximally excite a specific unit or layer (Olah, Mordvintsev, & Schubert, 2017). Yet, while these methods give an intuitive understand of how ANNs work, it has become clear that one cannot use them to predict how an ANN will classify and respond to new inputs. 

It is a concerning possibility that the extraordinary complexity of computation in large artificial networks may evade a complete understanding. If one measures complexity by how much information would be required to describe how a system works, any description would need to be extraordinarily lengthy and, perhaps, too lengthy for a human to internalize (Lillicrap & Kording, 2019). New concepts and theories might help break down and package these computations, but at the moment it is clear that we do not currently have the tools to understand how ANNs ‘see’ their inputs and come to their decisions.


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
