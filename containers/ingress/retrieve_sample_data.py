"""Simple script to dump some database raw data into a file for use in tests."""

import json
from typing import Any, Dict, List

from elasticsearch import Elasticsearch
import elasticsearch_dsl as es

from ingress.utils import setup_mappings

setup_mappings('tweets-brexit-remain-leave', 'localhost:9200')

client = Elasticsearch()

search = es.Search(using=client)

geotagged_records = search.query('match', geotagged=True)[0:10].execute()
untagged_records = search.query('match', geotagged=False)[0:10].execute()

combined_records: List[Dict[str, Any]] = []
combined_records.extend(geotagged_records.hits)
combined_records.extend(untagged_records.hits)

geotagged_data = []

for hit in combined_records:
    record = {}
    for attr in dir(hit):
        attr_data = getattr(hit, attr)
        if isinstance(attr_data, es.AttrDict):
            record[attr] = attr_data.to_dict()
        else:
            record[attr] = attr_data
    geotagged_data.append(record)

with open('sample_data.py', 'w') as sample_data:
    for record in geotagged_data:
        sample_data.write('{}\n'.format(json.dumps(record)))

print('sample_data.py written.')
