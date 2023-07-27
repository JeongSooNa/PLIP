# PLIP
Protein Ligand Interaction Profiler

This repository contains test content and script.

<img src="https://github.com/pharmai/plip/raw/master/pliplogo.png" width="100" height="100">

---

# Quick start
### Download Docker Images
```sh
docker pull pharmai/plip
```
### Shell Command
```sh
docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f input.pdb -yv -o output_dir_path -x -t -y -p
```

### Option
- '-f' or '-i' is a necessary parameter
```
  -h, --help            show this help message and exit

  -f INPUT [INPUT ...], --file INPUT [INPUT ...]
                        Set input file, '-' reads from stdin

  -i PDBID [PDBID ...], --input PDBID [PDBID ...]

  -o OUTPATH, --out OUTPATH

  -O, --stdout          Write to stdout instead of file

  --rawstring           Use Python raw strings for stdin

  -v, --verbose         Turn on verbose mode

  -q, --quiet           Turn on quiet mode

  -s, --silent          Turn on silent mode

  -p, --pics            Additional pictures

  -x, --xml             Generate report file in XML format

  -t, --txt             Generate report file in TXT (RST) format

  -y, --pymol           Additional PyMOL session files

  --maxthreads MAXTHREADS
                        Set maximum number of main threads (number of binding
                        sites processed simultaneously).If not set, PLIP uses
                        all available CPUs if possible.

  --breakcomposite      Don't combine ligand fragments with covalent bonds but
                        treat them as single ligands for the analysis.

  --altlocation         Also consider alternate locations for atoms (e.g.
                        alternate conformations).

  --nofix               Turns off fixing of PDB files.

  --nofixfile           Turns off writing files for fixed PDB files.

  --nopdbcanmap         Turns off calculation of mapping between canonical and
                        PDB atom order for ligands.

  --dnareceptor         Treat nucleic acids as part of the receptor structure
                        (together with any present protein) instead of as a
                        ligand.
  --name OUTPUTFILENAME
                        Set a filename for the report TXT and XML files. Will
                        only work when processing single structures.

  --peptides PEPTIDES [PEPTIDES ...], --inter PEPTIDES [PEPTIDES ...]
                        Allows to define one or multiple chains as peptide
                        ligands or to detect inter-chain contacts

  --intra INTRA         Allows to define one chain to analyze intra-chain
                        contacts.

  --keepmod             Keep modified residues as ligands

  --nohydro             Do not add polar hydrogens in case your structure
                        already contains hydrogens.

  --model MODEL         Model number to be used for multi-model structures.
```




## Reference
#### [PLIP](https://github.com/pharmai/plip)