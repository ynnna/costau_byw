It explores the Family expenditure workbook as an assignment for the Cost of Living (in Welsh costau byw - I hope!). 
## Installation
First clone this repo using this command:

    git clone https://github.com/ynnna/costau_byw.git

Then create and activate a new environment. For example, to create an enviorenment named env_cost:

    <path> -m venv env_cost
    cd <path>
    source env_cost/bin/activate

After activating the enviornment install all the packages in the requirement text file.
    
    pip install -r requirements.txt
To be able to reproduce the notebooks, the costau_byw package needs to be installed locally, using this command:

    pip install -e costau_byw


There is also the report saves as an html file (report.html) which does not require any instalation. 

---

## Repo structure

**costau_byw**

The package containing the function used to the explorations.  

**data**

The data used and produced in this project separated by type (csv and excel).

**notebooks**

- data_processing: Notebook processing and merging different datasets.

- report: Notebook showing the main findings.








