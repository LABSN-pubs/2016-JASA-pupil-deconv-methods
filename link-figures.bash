#!/bin/bash

# make figures available for LaTeX
for fig in ../figures/*.eps; do
	ln -s $fig
done
