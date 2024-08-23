---
title: "Conclusions"
exports:
  - format: tex
    logo: false
    template: ../templates/plain_latex_book_chapter
    output: exports/conclusion.tex
---

# Conclusions

This dissertation aims to justify and implement a machine learning framework for computational neuroscience. Together, these chapters demonstrate new ways in which machine learning can be used as tools (Chapters 1-3) or as a theories (Chapters 4-6) within neuroscience.

Since each chapter relates to a different subfield, the conclusions and future directions drawn from each one are best directed at each field. A general conclusion follows.

## Chapters 1 and 2: neurophysiology

The techniques we developed in these chapters are ways to validate descriptions of neural activity and function. Along with these techniques is a message: such descriptions need to be validated in order to be meaningful.

To illustrate this, we documented a failure of assumptions in a few specific situations. These were narrow, by necessity. In recordings of neurons in area V4 in two macaque monkeys, we found that although neurons have strong hue tuning, these do not capture how hue affects those neurons in general (Chapter 2). Likewise, generalized linear models mischaracterize how macaque M1 cells encode arm direction and velocity (Chapter 3). These findings do not alone indict the entire methodology. They are warnings and demonstrations of the necessity of validating a generalization of experimental findings. 

Our demonstrations are not the only papers with similar conclusions. It is not a rare situation that features unvaried by a researcher affect the neural response (and as argued in Chapter 2, it should be expected). Area V1 is a canary for the approach. There, papers have asked about generalization of orientation tuning to natural scenes (David et al., 2004; Touryan et al., 2005), and compared typical models with machine learning benchmarks (Cadena et al., 2019; Prenger et al., 2004). As warned by Olshausen and Field (Bruno A Olshausen & Field, 2005, 2006), it seems much about the computations performed in V1 still remain to be understood. This warning exists for V1 because, unusually, the validating measurements have been performed. 

In other areas, however, it is rare that key validations are presented along with an encoding model or tuning curve. When omitted, it signals a tacit comfort with the possibility that tuning curves will change with context or that encoding models will miss explainable variance. Encouragingly, this trend may be changing. As experimental methods improve and to allow more neurons to be simultaneously recorded,  researchers are again using benchmarks to challenge previous assumptions about the meaning of neural activity (e.g. (Musall, Kaufman, Juavinett, Gluf, & Churchland, 2019)). 

In addition to more frequent benchmarking, the future directions for neurophysiology might include theories of processing that guide one’s assumptions about responses to untested stimuli. Since the sensory systems know a great deal about the external world (Lillicrap & Kording, 2019), models that incorporate naturalistic statistics are perhaps the most promising. Knowing the statistics of the training data allows neurophysiologists a crucial leg up. An older example taking this approach (to great success) is the notion of efficient coding (Barlow, 1961). Another possibility is to describe the effects of learning effectively with limited exposure to the natural world, as I explored in Chapter 7. By studying the principals by which neural codes emerge, neurophysiology might begin to better understand the codes themselves.

## Chapter 4: Probabilistic representation learning

This chapter aimed to further theories of learning. Adopting a popular hypothesis of the computational goal of learning (probabilistic representation learning), it attempted to draw a line reaching down to the cortical circuits that could implement this learning goal. Two ends thus constrained the project: the known biology, and the desired computation.

If any lesson is to be taken from this section, it is that an adversarial algorithm could, in principal, be implemented by the cortex. It is one way the brain might learn internal models of the world via switching between externally- and internally- driven modes of processing (Honey et al., 2017). If this is the case, it would mean that the brain contains discriminators of the two modes of activity, which we hypothesized could be certain interneuron cell types. These would be identifiable by a plasticity rule that switches sign with the mode switch. This algorithm is not implausible, to the extent it is not yet ruled out by known data, and would allow the cortex to solve the difficult and currently unresolved problems inherent to representation learning.

This project treated with less flexibility the top-level computational goal: probabilistic representation learning, learning internal models of neural activity in sensory areas, and Bayesian inference over those models. In certain communities this framework is quite popular (Fiser, Berkes, Orbán, & Lengyel, 2010; Friston, 2005). Yet this theory is not thoroughly linked to a biological substrate, and as described in this project, it is unclear how this objective could be learned by neural circuits. Previous proposals for learning circuits (e.g. (Friston, 2005; Hinton, Dayan, Frey, & Neal, 1995; Rezende & Gerstner, 2014)) have clear problems, and, candidly, my attempt at resolution involved an uncomfortable level of speculation. Since there is inconclusive evidence at the level of biology, the high-level computational goal must do more work to carry the theory than otherwise. If this, too, is inconclusive, perhaps a new and humble attention should be paid to learning circuits, especially during the sensitive or critical period of sensory plasticity.

## Chapter 5: Neural network optimization

Neural networks encode functions. For certain questions of learning, one can bracket away the specific parameters that encode those functions and think about how the overall function changes. For neuroscience, this would amount to looking at changes in behavior instead of synapses, but using the mathematical language of optimization.

This chapter proposed a learning rule for ANNs in which the allowed change in behavior is constant over time. This type of learning rule may be at play for animals, as well. In motor tasks, for example, learning appears dependent on the direction of an error but independent of the magnitude of that error (Fine & Thoroughman, 2006). Thinking about optimization in function space, which is well-appreciated in machine learning, may be a concept that is useful for neuroscience as well.

One possible future application in neuroscience is to extend the framework of Chapter 7 and ask about the behavioral consequences of learning with algorithms that incrementally adjust behavior. This is to replace gradient descent in parameter space with that in function space, but ask the same question about the residual effects of learning algorithms. This might allow similar insights, but would be agnostic to the specific mechanism by which the brain adjusts behavior. By circumventing the mechanistic issue of what mediates learning, this perspective may afford a more direct (yet abstract) description of the effects of learning on perception and behavior.

## Chapter 6: The sensory consequences of learning algorithms

Neuroscience can gain from ‘artiphysiology’ of neural networks as a complement to neurophysiology. Would artificial neural networks trained on ImageNet be, like humans, more sensitive to basic visual features that are more common? Finding that the answer was ‘yes’, this chapter documented how this emerges from the learning mechanism of gradient descent. This was a move to link artiphysiology with deep learning theory. The consequences may resonate back from theory, though deep learning representations, and to a better understanding of the brain.

In the course of this project, it became clear that this was a powerful way of thinking and just the beginning of what is possible. This paper focused on efficient coding, but a learning framework may help explain a constellation of neural phenomena. Already it has been tied to why representations appear low-dimensional (Flesch, Juechems, Dumbalska, Saxe, & Summerfield, 2022) and why certain categories are learned before others (Saxe, McClelland, & Ganguli, 2019). Future research may help to further describe these effects of learning in greater detail.

With the bridge between machine learning theory and neuroscience now open, it is important that new concepts continue to be brought over. Machine learning theory is an emerging discipline. Many of its central issues – like why deep neural networks generalize, or what exactly they prefer to learn first – are still unresolved. These theories must be ported to neuroscience when and if they are found. One important area, in particular, is to incorporate theories that bridge the lazy (kernel) and rich (feature-learning) regimes identified by deep learning theory. These insights will almost certainly help to describe learning in the brain.

## Conclusion

The process of science is not unlike a learning algorithm. From limited experience, it must make generalizations about an underlying reality or events in the future. This requires making assumptions. If these are incorrect, one is at danger of overgeneralizing (Chapters 2-3). If the assumptions are appropriate, one can learn effectively (Chapter 6) even though the biases of those assumptions are never totally escapable (Chapter 7). Proceeding in both domains requires identifying and optimizing one’s prior beliefs.

As the theory of machine learning progresses, this field will have increasingly more to say about learning in the brain and its consequences. It is important that this bridge remain open. Why can we learn some things, and not others? What determines the function of cortical areas, as plastic as they are? These questions will continue to motivate me and hopefully many others in the coming years.

## References

Barlow, H. B. (1961). Possible principles underlying the transformation of sensory messages. Sensory communication, 1(01). 

Cadena, S. A., Denfield, G. H., Walker, E. Y., Gatys, L. A., Tolias, A. S., Bethge, M., & Ecker, A. S. (2019). Deep convolutional models improve predictions of macaque V1 responses to natural images. PLoS Computational Biology, 15(4), e1006897. 

David, S. V., Vinje, W. E., & Gallant, J. L. (2004). Natural stimulus statistics alter the receptive field structure of v1 neurons. Journal of Neuroscience, 24(31), 6991-7006. 

Fiser, J., Berkes, P., Orbán, G., & Lengyel, M. (2010). Statistically optimal perception and learning: from behavior to neural representations. Trends in cognitive sciences, 14(3), 119-130. 

Flesch, T., Juechems, K., Dumbalska, T., Saxe, A., & Summerfield, C. (2022). Orthogonal representations for robust context-dependent task performance in brains and neural networks. Neuron, S0896-6273(0822)00005-00008. doi:10.1016/j.neuron.2022.01.005

Friston, K. (2005). A theory of cortical responses. Philosophical Transactions of the Royal Society B: Biological Sciences, 360(1456), 815-836. 

Hinton, G. E., Dayan, P., Frey, B. J., & Neal, R. M. (1995). The" wake-sleep" algorithm for unsupervised neural networks. Science, 268(5214), 1158-1161. 

Lillicrap, T. P., & Kording, K. P. (2019). What does it mean to understand a neural network? arXiv preprint arXiv:1907.06374. 

Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., & Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. Nature Neuroscience, 22(10), 1677-1686. 

Olshausen, B. A., & Field, D. J. (2005). How close are we to understanding V1? Neural computation, 17(8), 1665-1699. 

Olshausen, B. A., & Field, D. J. (2006). What is the other 85 percent of V1 doing. L. van Hemmen, & T. Sejnowski (Eds.), 23, 182-211. 

Prenger, R., Wu, M. C.-K., David, S. V., & Gallant, J. L. (2004). Nonlinear V1 responses to natural scenes revealed by neural network analysis. Neural Networks, 17(5), 663-679. 

Rezende, D., & Gerstner, W. (2014). Stochastic variational learning in recurrent spiking networks. Frontiers in Computational Neuroscience, 8, 38. doi:10.3389/fncom.2014.00038

Saxe, A. M., McClelland, J. L., & Ganguli, S. (2019). A mathematical theory of semantic development in deep neural networks. Proceedings of the National Academy of Sciences, 116(23), 11537-11546. 

Touryan, J., Felsen, G., & Dan, Y. (2005). Spatial structure of complex cell receptive fields measured with natural images. Neuron, 45(5), 781-791. 

