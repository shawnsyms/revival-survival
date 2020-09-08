# Revival = Survival: a data project on the overdose crisis

<img src="img/revival_hero_image-dan-meyers-unsplash.png">

## Overview
I learned at a Shopify internship process webinar that applicants would need to submit a personal coding project to walk through. So I decided to try and build something from scratch by the deadline. And I wanted to ensure my project would be different from everyone else's. 

I chose to focus on the opiate overdose crisis because of my interest in social-justice issues. And it's personal, too; I lost my cousin, Vince, my uncle, Kevin and Xephiral, my friend. The theme is relevant to my application, as well: Shopify empowers merchants and consumers — but you can't become empowered if you're dead. 

The opiate overdose crisis sits at the nexus of two intractable social forces — (1) rampant overprescribing of addictive medications, and (2) a toxic, unregulated street drug supply. No one deserves to die because of that. And now there's a chance for them to get better. Once revived, they can survive. Naloxone, a treatment that can temporarily reverse an opioid overdose, is available free at pharmacies around Ontario and across Toronto. 

This project has two parts. First, I use data visualization tools and techniques to tell the story of the overdose epidemic. Second, I've built a simple tool based on a geo-spatial dataset that can inform people about the locations of nearby recovery resources, including pharmacies where they can access naloxone. Carrying it on their person, anyone can save a life. 



## Configuration
This project was set up using an anaconda virtual environment:

<code>conda create --name shopify flask  numpy pandas requests</code> 

Run the following from a command prompt whilst inside the environment:

<code>conda install -c conda-forge folium</code>

The directory structure of the repository should be fairly self-explanatory. For instance, csv files are in the csv directory. 



## Assessment

<ul>
    <li><strong>Data visualization:</strong> I believe I've done a reasonably good job bringing the data to life using visualization best practices and attempting to conform to the Polaris style system whilst doing so.</li>
    <li><strong>Overdose resource locator:</strong> There are a number of improvements necessary for this app. It relies on geolocation via IP to identify user location, which is not sufficiently accurate. As a next step, it should be re-written in a combination of Javascript and python and deployed for online access using Heroku or a similar platform. This will add ease of use and drastically increase location accuracy.  
</ul>






## Data sources

### Visualizations

<ul>
    <li>
        <a href='https://www.toronto.ca/community-people/health-wellness-care/health-inspections-monitoring/toronto-overdose-information-system/'>Toronto Overdose Information System</a>
    </li>
    <li>
        <a href='https://www.ottawapublichealth.ca/en/reports-research-and-statistics/drug-use-and-overdose-statistics.aspx#Drug-Checking-Results'>Drug Testing Results, Ottawa</a>
    </li>
    <li>
        <a href='https://health-infobase.canada.ca/substance-related-harms/opioids/'>Opioid-related Harms in Canada</a>
    </li>
    <li>
        <a href='https://www.cihi.ca/en/opioids-in-canada'>Canadian Institute for Health Information</a>
    </li>
</ul>

### Locators

<ul> 
    <li>
        <a href='Description:[http://members.ocpinfo.com/TCPR/Public/PR/EN/#/forms/new/?table=0x800000000000003C&form=0x800000000000002B&command=0x80000000000007C4](https://www.google.com/url?q=http://members.ocpinfo.com/TCPR/Public/PR/EN/%23/forms/new/?table%3D0x800000000000003C%26form%3D0x800000000000002B%26command%3D0x80000000000007C4&sa=D&source=calendar&usd=2&usg=AOvVaw0XPdW-MhYPS0ZSylwRNN18) '>Ontario College of Pharmacists</a>
    </li>
    <li>
        <a href='https://www.canada.ca/en/health-canada/services/substance-use/supervised-consumption-sites/status-application.html#wb-auto-8'>Toronto Safer Injection Sites</a>
    </li>
    <li>
        <a href='https://www.ontario.ca/page/mental-health-services'>Toronto R.A.A.M. clinics</a></li>
</ul>




## Technical references
I reviewed the following relevant references whilst working on **Revival = Survival.** Many of them include details on code/packages/tactics that I did not end up using, however they are all useful to visit.
<ul>
    <li>
        <a href='http://www.openstreetmap.org'>Open Street Map</a>
    </li>
    <li>
        <a href='https://polaris.shopify.com'>Shopify Polaris</a>
    </li>
    <li>
    <a href='https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889'>A tour of the top 5 sorting algorithms with Python code</a>
    </li>
    <li>
    <a href='https://www.arcgis.com/home/webmap/viewer.html?webmap=b44592265a7e405d95be7d811e1a52ef'>ArcGIS City of Toronto basemap</a>
    </li>
	<li>
    <a href='https://open.toronto.ca/dataset/neighbourhoods/'>City of Toronto Open Data Project: Neighbourhoods</a>
	</li>
	<li>
    <a href='https://medium.com/@lisachen_7431/using-folium-to-visualize-distribution-of-public-services-in-140-toronto-neighbourhoods-e53271b7f43f?sk=cac47558e62ead38bd07e0e335f49c44&fbclid=IwAR2N5CnDwXumLtgUajXNiEWy8SP8IFGah8klYc8eIhkki-mOeel6YrJATDo'>Using Folium to Visualize Distribution of Public Services in 140 Toronto Neighbourhoods</a>
	</li>
	<li>
    <a href='https://developer.here.com/blog/understanding-geocoding-with-python'>Geocoding a Location Using Python and Flask</a>
	</li> 
	<li>
    <a href='https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html'>Geographic Data with Basemap</a>
	</li>
	<li>
    <a href='https://datascience.quantecon.org/applications/maps.html'>Mapping in Python – QuantEcon DataScience</a>
	</li>
	<li>
    <a href='https://mobiforge.com/design-development/geo-sorting-using-device-geolocation-to-sort-distance'>Geo-sorting: Using Device Geolocation to Sort by Distance</a>
	</li>
	<li>
    <a href='http://maps.stamen.com'>Map Stack | Stamen Design</a>
	</li>
	<li>
    <a href='https://www.kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python'>How to find the distance between two lat-long coordinates in Python</a>
	</li>
	<li>
    <a href='https://oslandia.com/en/2017/07/03/openstreetmap-data-analysis-how-to-parse-the-data-with-python/'>OpenStreetMap data analysis: how to parse the data with Python?'</a>
    </li>
	<li>
    <a href='https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac'>Mapping with Matplotlib, Pandas, Geopandas and Basemap in Python</a>
	</li>
	<li>
    <a href='https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972'>GeoPandas 101</a>
	</li>
	<li>
    <a href='https://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html'>Creating a GeoDataFrame from a DataFrame with coordinates</a>
	</li>
	<li>
    <a href='https://www.ontario.ca/page/get-naloxone-kits-free'>Recognize and temporarily reverse an opioid overdose</a>
	</li>
	<li>
	<a href='https://github.com/mcrr/isleofinsanityandhope/'>Github for Isle of Insanity and Grief: Overcoming my son's overdose and death</a>
	</li>
</ul>    	



## Subject matter references 

There is not as much out there as you would think when it comes to opioid overdose and data science, but here are a few influential articles that inspired me. Note that in some cases, their approaches were only possible because of access to large amounts of privacy-protected data. 

<a href='https://www.nature.com/articles/s41598-020-61281-y'>Epidemiological and geospatial profile of the prescription opioid crisis in Ohio, United States</a>

<a href='https://towardsdatascience.com/relapse-trigger-predicting-stress-with-a-i-f559af5a19a3'>Relapse trigger: Predicting stress with A.I.</a> 

<a href='https://towardsdatascience.com/patterns-in-accidental-drug-overdose-fatalities-994573a2be72'>Patterns in Accidental Drug overdose fatalities</a>

<a href='https://www.sas.com/content/dam/SAS/en_us/doc/research2/iia-data-analytics-combat-opioid-epidemic-108369.pdf'>White paper: Data and Analytics to Combat the Opioid Epidemic</a>

<a href='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6774610/'>Towards automating location-specific opioid toxicosurveillance from Twitter via data science methods</a>





