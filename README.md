# ECO_Propagation
 This repository is created to propagate evidence codes(ECO) with respect to ECO hierarchy defined in **eco.obo** file by using **is_a**.
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
* The colums of input file muust be seperated with either tab or commo.
* **First line of input file is assumed to be identification line for each column!**

### Explanation of Parameters
* **--inputFile**: gene/protein, annotation and evidence code file containing gene/protein ids, annotations and evidence codes. Input file extension should be: **.txt** or **.csv**
* **--seperator**: seperator of input file columns, its default value is **tab**, other options can be **tab** or **commo**
* **--geneColumn**: gene/protein id/accession column number (integer) in the input file, starting index = 0
* **--infoColumn**: annotation column number (integer) in the input file, starting index = 0
* **--ecoColumn**: evidence code column number (integer) in the input file, starting index = 0
* **--outEco**: evidence code(e.g. ECO:0000265) of the annotations that you would like to have in your output file 
### A sample command to run ECO_Propagation is as follows:
```
python main.py --inputFile sample_input.txt --seperator tab --geneColumn 1 --infoColumn 4 --ecoColumn 6 --outEco ECO:0000265

```

### Output file

* The results will be located under **output_folder** with the name: **input_file_name.csv**

## License

MIT License

Copyright (c) 2021 CanSyL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

