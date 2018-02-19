# "Learning Shape Priors for Object Segmentation via Neural Networks": the code

This repo contains the code for the ICIP paper mentioned above, by me and [Ming-Hsuan Yang](http://faculty.ucmerced.edu/mhyang/index.html).

The interesting part is deep_nets/templated_net, it has all the experiments presented in the paper (even a bit more) + some Python code for evaluation. Also included are some scripts to generate the training data from the PFP & CUB datasets.

## Dependencies
- [Pyratemp](https://www.simple-is-better.org/template/pyratemp.html), a Python templating framework, to generate the protobufs for the experiments (used instead of copy-pasting by hand)
- the [redo](https://github.com/apenwarr/redo) build system for preprocessing image data (in all the "do" files). It has a very simple syntax (they're basically bash scripts), so it shouldn't be hard to tell what they're doing even without running them
- the images for the datasets, along with our annotations refined by hand, are available at my site at http://eng.ucmerced.edu/people/ssafar

## How to run it?

A possible starting point is [gen_models.sh](https://github.com/ssafar/learning_shape_priors/blob/master/deep_nets/templated_net/gen_models.sh). We have different YAML config files for different datasets and "stages" (when we change parameters during training); these specify values for variables (see e.g. the [config file](https://github.com/ssafar/learning_shape_priors/blob/master/deep_nets/templated_net/cub.yaml) for the Caltech-UCSD Birds 200 (CUB) dataset). These will be subsituted into templates describing different parts of the network, along with a script that actually runs Caffe with this configuration.

The main issue is that the code uses a relatively old version of Caffe as it hasn't been updated recently. Also, it needs some patches to this old codebase (e.g. an old version of the reshape layer that got into the codebase since, along with possibly other, relatively simple but still mandatory additions). You can take a look at the branch I was working with at https://github.com/ssafar/caffe/tree/unpooling; this should include most (if not all) of the additional code and point to a version of Caffe that actually works with the configurations in this repo.
