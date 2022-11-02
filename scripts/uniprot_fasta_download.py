#!/usr/bin/env

import requests
url = 'https://rest.uniprot.org/uniprotkb/stream?compressed=true&format=fasta&query=%28%28taxonomy_id%3A33634%29%29%20AND%20%28existence%3A3%29'
with requests.get(url, stream=True) as request:
     request.raise_for_status()
     with open('stramenopile_homology_uniprot.fasta.gz', 'wb') as f:
         for chunk in request.iter_content(chunk_size=2**20):
             f.write(chunk)
