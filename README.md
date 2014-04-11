# GeoPy

A Python-based script hacked together to convert a list of Yelp urls into a Google Map compatible KML file.

Google's web service APIs currently lack support for constructing maps dynamically without a hosted web application w/ their Javascript API, thus the need for scripting together a KML document to be uploaded through Google Map's interface.

You can read more about Google's Map APIs below:
  * [JavaScript API v3](https://developers.google.com/maps/documentation/javascript/tutorial)
  * [Static Maps API v2](https://developers.google.com/maps/documentation/staticmaps/)
  * [Geocoding API](https://developers.google.com/maps/documentation/geocoding/)
  * [Keyhole Markup Language](https://developers.google.com/kml/documentation/kmlelementsinmaps)

Url requests are sent using [urllib](http://docs.python.org/2/library/urllib.html), Html parsing is done via [lxml](http://lxml.de/), and Xml/Kml parsing/construction done via [xml.etree.ElementTree](http://docs.python.org/2/library/xml.etree.elementtree.html) and [xml.dom](http://docs.python.org/2/library/xml.dom.minidom.html)

Asyncronous runtime for converting 30 listings to kml was averaging out at ~65000ms.

The [gevent](http://sdiehl.github.io/gevent-tutorial/) variation ([stackoverflow](http://stackoverflow.com/questions/14616883/multithreading-asynchronous-i-o)) improves the runtime average to *~8000ms* through asynchronous execution of HTTP requests. It is possible this may not scale out entirely as the threshold of outgoing requests increases however discovering the power of *gevent* and multithreaded processing was well worth it.

If you are having trouble installing gevent on Ubuntu see [here](http://stackoverflow.com/questions/6431096/gevent-does-not-install-properly-on-ubuntu)

# Usage

Python 2.7.2 was used to execute the code:

```bash
$ python geopy.py --f [FILENAME]
```

### Options and Arguments

  * `--f [FILENAME]`
    Specify the file name containing the Yelp urls
