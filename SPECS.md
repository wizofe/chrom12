## General Requirements
 * Database
    - Store Genbank data
    - Parser to extract the relevant data to `SQL` (identify introns/exons
& find DNA coding sequence)
    - Python wrapper to `SQL` that returns data to the middle layer
    - Calculating codon usage across all coding regions

* Middle Layer
    - Identifying where the coding regions are and generating the coding DNA sequence
    - Aligning the protein translation with the DNA coding sequence
    - Identifying restriction enzyme (RE) sites
    - Providing a list of known REs to the front end
    - Identify whether an RE has restriction sites within the coding region
    - Counting codon usage in a gene
    - Extracting information from the database layer (e.g. the complete gene list or individual gene information; can be wrappers to the database layer code)
* Web Interface
    - A (set of) web pages that allow the user to query the database - via the middle tier.
    - Supporting Python/CGI scripts that access the business logic layer of code when forms are submitted and generate new pages.
    - Requirements for the queries are listed below.

##
