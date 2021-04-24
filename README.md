# ECO_Propagation
 This repository is created to propagate evidence codes(ECO) with respect to ECO hierarchy defined in **eco.obo** file by using **is_a** relations.
* The following figure shows a sample of evidence code(ECO) hierarchy
![alt text](https://github.com/gozsari/ECO_Propagation/blob/main/images/eco.PNG)

## Installation

## How to run ECO_Propagation to obtain the propogation results 

## Preparation to run ECO_Propagation

* Clone the Git Repository

### Downloading eco.obo !!!
* Due to the periodic updating of the ECO hierarchy, **eco.obo** must be downloaded from [here](https://raw.githubusercontent.com/evidenceontology/evidenceontology/master/eco.obo) into the ECO_Propagation folder to have the latest version of the ECO hierarchy

### Input file 
* The input file must be located under **input_folder**.
* It must be in either a txt or cvs format
* The colums of input file muust be seperated with either space, tab or commo.
* **First line of input file is assumed to be identification line for each column!**

### Explanation of Parameters
* **--inputFile**: gene/protein, annotation and evidence code file containing gene/protein ids, annotations and evidence codes. Input file extension should be: **.txt** or **.csv**
* **--seperator**: seperator of input file columns, its default value is **tab**, other options can be **space** or **commo**
* **--geneColumn**: gene/protein id/accession column number (integer) in the input file, starting index = 0
* **--annotationColumn**: annotation column number (integer) in the input file, starting index = 0
* **--ecoColumn**: evidence code column number (integer) in the input file, starting index = 0
* **--outEco**: evidence code(e.g. ECO:0000265) of the annotations that you would like to have in your output file 
### A sample command to run ECO_Propagation is as follows:
```
python main.py --inputFile sample_input.txt --seperator tab --geneColumn 1 --annotationColumn 4 --ecoColumn 6 --outEco ECO:0000265

```

### Output file

* The results will be located under **output_folder** with the name: *input_fileName***_propagated_genes_annotation_ecoIDs.csv**

## License
ECO_Propagation

Copyright (c) 2021 CanSyL
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.


