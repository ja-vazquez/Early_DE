# Early_DE
Module that incorporates an Early Dark Energy component
(EDE) into the cosmological equations.

This code subsitutes the standard cosmological constant by a 
Dark Energy component, which has the property to contribute to the
total density of the Universe even at high redshifts.
In a previous paper [arXiv:1411.1074](http://arxiv.org/abs/1411.1074) 
we explored the [Doran & Robbers](http://arxiv.org/abs/astro-ph/0601544)
parameterization as a candidate of EDE. Now, considering a more general
picture we have incorporated an scalar field with potential

Inline-style: 
![alt text](Potential.png "Logo Title Text 1")


## Python Code

`QuintCosmology` is part of the [SimpleMC](https://github.com/ja-vazquez/SimpleMC) 
code used for cosmological parameter estimation.


Here the EDE is described in the subroutine 
`Quint_init_background`.

