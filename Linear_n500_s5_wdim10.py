#!/usr/bin/env python

gam = False
M = None
n = 500
s = 5
wdim = 10
niter = 1000000

import generic_experiment

generic_experiment.run_experiment(gam,M,n,s,wdim,niter)
