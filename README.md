# YelpKml

A Python-based script hacked together in an attempt to convert a list of Yelp urls into a Google Map.

Given Google's limited support of web service APIs for constructing maps dynamically, the next best thing that doesn't require use of Google Map's JavaScript API is to construct a KML document and upload it through Google Map's interface - the end result: a Yelp to Kml conversion script.

You can read more about Google's Map APIs below:
  * [JavaScript API v3](https://developers.google.com/maps/documentation/javascript/tutorial)
  * [Static Maps API v2](https://developers.google.com/maps/documentation/staticmaps/)
  * [Geocoding API](https://developers.google.com/maps/documentation/geocoding/)
  * [Keyhole Markup Language](https://developers.google.com/kml/documentation/kmlelementsinmaps)

Url requests are sent using [urllib](http://docs.python.org/2/library/urllib.html), Html parsing is done via [lxml](http://lxml.de/), and Xml/Kml parsing/construction done via [xml.etree.ElementTree](http://docs.python.org/2/library/xml.etree.elementtree.html) and [xml.dom](http://docs.python.org/2/library/xml.dom.minidom.html)

Asyncronous runtime for converting 31 listings to kml was averaging out at ~65000ms.

In stumbling upon [gevent](http://sdiehl.github.io/gevent-tutorial/) from [stackoverflow](http://stackoverflow.com/questions/14616883/multithreading-asynchronous-i-o) synchronous runtime average was brought down to *~8000ms* - that's a riduculous amount of runtime perf improved. It is likely that this may not scale out entirely as the number of outgoing requests increases however discovering the power of *gevent* and multithreaded processing was well worth it.

If you are having trouble installing gevent on Ubuntu see [here](http://stackoverflow.com/questions/6431096/gevent-does-not-install-properly-on-ubuntu)

# Usage

Python 2.7.2 was used to execute the code:

```bash
$ python YelpKml.py --f [FILENAME]
```

### Options and Arguments

  * `--f [FILENAME]`
    Specify the file name containing the Yelp urls
