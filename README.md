## Open Data Research Bibliography

This repository contains scripts for converting and displaying data in the ['Open Data Research' group on Zotero](https://www.zotero.org/groups/open_data_research/) in the [Simile Exhibit Faceted Browser](http://www.simile-widgets.org/exhibit/).

### Currently
Data in the Zotero group is tagged according to [a defined tagging schema](https://docs.google.com/spreadsheets/d/1gmF8vaWY2NZaYoM82YdUU2cSWFa-9O7hIvyMpwmEHJ0/edit?usp=sharing). The script takes any tags with ':' in, and splits them into prefix and tag value. It cleans basic errors (incorrect whitespace) and outputs the data as Exhibit JSON.

It iterates over all the items in the group.

#### Running

Run buildbib.py to fetch new data. It will merge the new data with the template.json contents to provide labels for relevant elements. 

Then view index.html (this must be served from a web server, as browser security models otherwise prevent the scripts directly accessing the data.json file through a filesystem)

### ToDo

* The tagged content on Zotero also includes 'notes' related to each article. These should be displayed in the interface.
* The template.json should be automatically generated from the schema. 
* It would be nice to include screen-shot images of the file associated with entry. Explore options for doing this. 