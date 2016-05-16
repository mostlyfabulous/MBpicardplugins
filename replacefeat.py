PLUGIN_NAME = 'Replaces Feat. with Ft'
PLUGIN_AUTHOR = 'Lukas Lalinsky, Bryan Toth, Andrew Wong'
PLUGIN_DESCRIPTION = '''Replaces "feat." with "Ft".<br/>
For example:<br/>
"Kanye feat. Kanye feat. Kanye" becomes: "Kanye Ft Kanye Ft Kanye"<br/>
Will modify these tag fields:
<ul>
	<li>artist</li>
	<li>artistsort<li>
    <li>albumartist</li>
    <li>albumartistsort</li>
</ul>
Known bugs: Does not rename artist tag for the album itself
'''
PLUGIN_VERSION = "0.62"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "0.16"]

import re
from picard.metadata import (
    register_track_metadata_processor,
    register_album_metadata_processor,
    )

_feat_re = re.compile(r"\s+ *feat\. *", re.IGNORECASE)
# old version
# _feat_re = re.compile(r"\s+\(feat\. [^)]*\)", re.IGNORECASE) - needs (feat. ) for a match

def remove_featartists(tagger, metadata, release, track): # adding album to here doesn't breaks it
    metadata["artist"] = _feat_re.sub(" Ft ", metadata["artist"])
    metadata["artistsort"] = _feat_re.sub(" Ft ", metadata["artistsort"])
    metadata["albumartist"] = _feat_re.sub(" Ft ", metadata["albumartist"])
    metadata["albumartistsort"] = _feat_re.sub(" Ft ", metadata["albumartistsort"])

register_album_metadata_processor(remove_featartists)
register_track_metadata_processor(remove_featartists)
