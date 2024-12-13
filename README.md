# Tutorials

A set of tutorials written to introduce students the topics of computing and analysis for high energy physics and FCC-ee software. The tutorials are of general interest, but specific examples and commands rely on MIT resources. 

Authors: Jan Eysermans, Luca Lavezzo.

**Table of contents**
- `00_Intro`: Introudction to the basic tools and software you will need for doing research in High Energy Physics (HEP). How to set up your accounts, access to subMIT cluster, and environment.
- `01_Basics`: Introduction to HEP computing basics, including data structures, ROOT, ROOT DataFrames, histograms, and plotting.
- `z_mumu_xsec`
- `z_mumu_afb`
- `wmass`
- `zh_xsec`
- `functions`: a set of commonly used functions for the tutorials.

## Getting started

Detailed instructions on how to set up your environment and access the tutorials are provided in the `00_Intro` tutorial. In summary,

To run the tutorials you need:
- A SubMIT account
- A Github account, and fork this repository.

Once you have access to SubMIT (via ssh, VS Code, or JupyterHub), clone your fork of this repository:
```shell
git clone git@github.com:<git-username>/<fork-name>.git
cd <fork-name>
```

To set up the FCCAnalyses software, run the following command:
```shell
# only required once per shell
source /work/submit/jaeyserm/software/FCCAnalyses/setup.sh 
```

You can now run the tutorials!