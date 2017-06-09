# audiovisual analytics vocabulary and ontology

# Implementation details
Each concept is related both to an OWL class and a SKOS
concept for [allowing OWL DL inference to be made in the ontology][1].
Otherwise it is OWL Full.

The conceptualization is formalized in OWL (as an ontology)
from which the SKOS vocabulary is automatically derived.
SKOS is less formal then OWL so a small set of conventions
allows the percolate to output the vocabulary
from ontology.

The ontology rdf/visualAnalytics.owl is synthesized by the src/ontology.py file.
The vocabulary rdf/visualAnalytics.skos is then obtained from rdf/visualAnalytics.owl
by means of src/vocabulary.py.

Visualization of RDF code involves:
* multiple RDF text formats (Turtle, n3, Manchester, XML, etc).
* diagram view (nodes are classes or concepts or raw data).
* Tree view for the relations.

Processing of data in the SparQL endpoint:
* for data selection
* for processing which can take advantage of the data types.
* for minimizing the transfered data.
* for avoiding overload in the python server data processing.

Processing in the Python server:
* Python Server is a Software As a Server?
* Optimized numerical routines in numpy and scipy (BLAS, Fortran).
* Should minimize the effort of the client processing,
which runs Javascript and has to deal with the audiovisual rendering of data and user interface.
* Serving JavaScript for the user interface.
* Data IO to both the interface and the SparQL endpoint.
* Process each request in a different thread. Use multithreading when suitable for one request.

Processing in Javascript:
* Requests to Python any measurements and data
  - Python keeps track of the data and writes measures (all?) as new data into SparQL endpoint.
* Should render images and audio from data received from Python server.
  - Audio playback: Mozart, Aphex Twin, web radio, audio from soundcloud, archive.org or youtube (librevox?)
  - Play audiofiles received from server
  - Render audio from arbitrary data
* Allow for setting interface from audio signals (e.g. from mic or audio file).
* Should manage the user interface.
* Should keep the state of the aa session.
* Will be done in the client (no node.js).
* Should allow one to download images, tables, audio and state files.
* Should enable the user to:
  - link data to methods of visualization and analysis.
  - keep a tree of current sessions, with easy forking capabilities.
  - change settings of visualizations and analysis in interactive/real time.
  - Instantiate data items from sparql queries (LOSD, DBPedia), data world or uploaded files.

Relate AA vocabulary to wordnet ASAP.
Maybe start from this linking to wordnet and DBPedia and LOSD
and then grow from them.

Adicionar o void:sparqlQuery "select ?s where ...".
Propor o acréscimo p mantenedores do VOID.






Each OWL class and property is a subclass of SKOS skos:Concept.
subClassOf and subProperty of are subProperties of skos:broader.
OWL properties also yield skos:related.

Both the ontology and vocabulary have core and extended versions.
Extended includes core.
Core is meant to keep a very simple representation of the knowledge.
* Core includes: data, analysis and audiovisualization concepts as OWL classes and properties,
and SKOS concepts.
* Extended also includes: knowledge from other fields such as statistics, complex networks,
text mining, audio and music, visual design, HCI, UI, etc.
Necessary to better account for the Visual Analytics field.

Defining classes as of owl:type another class and rdfs:subClassOf skos:Concept
allows for anotating instances of the class with SKOS properties.
This does not enable the anotations to be directly annotated in the classes,
reason why we did not choose this approach.

Descrever os tipos de dados e algo
Pseudocodes are written as RDF Schema (RDFS).
RDF collections, RDFS containers,

The data unit can correspond to a SparQL query,
from which the correspondent data structures are obtained.
We have the following layers for processing data units:
* Sparql query: data selection and preprocessing
to result in data structures to the rest of the analysis and futher processing in Python.
* Python layer that receives data from uploaded files and online queries (SparQL, Data-World).
  - Preprocessing of uploaded data in python to result in RDF data (if possible).
  - Derive preliminary ontology from data items after traslated to RDF, like in [LOSD][2][3].
    * Figures.
    * Directions for Webprotege for enhanecemnts and discussion.
    * Try to relate the classes and properties with other ontologies by names and descriptions (string).
    * 

[2]: https://github.com/ttm/linkedOpenSocialDatabase/raw/master/paper.pdf
[3]: https://github.com/ttm/linkedOpenSocialDatabase/raw/master/supportingInformation.pdf

## Issues

Find the [difference between using an inference process
or a model-driven transformation][1].

Understand the pros and cons of using hybrid part SKOS part OWL
as in the same reference.

Find the difference between skos Collection and Concept Scheme.

[1]: https://www.w3.org/2006/07/SWD/SKOS/skos-and-owl/master.html

# Drafts:

Should include subfields like data visualization,
information and scientific visualization,
HCI, visual design, UI,
Should include visualization methods including other
senses, at least hearing
(for the blind to have information of the visual environment,
such as location and colors. Michel Hospital (FEE/UFSCar)
visualization method/technique:
  * number of dimensions of data that the visualization handles (Wilkings, 1994).
  * number of dimensions used for visualization (pca 2-3)
  * main visualization dimensions (pca 2)
  * each dimension might have an specific priority for figures or tabular.
  Properties:
    - tabularPriority (pca table, components and eigenvalues)
    - scalarPriority (liapunov coefficient, single topological measures)
    - visualizationPriority (2-3 dimensions in pca)
    - bestVisualization (2 pca)
  * for what data type is the visualization best suited for?
  * 
Should include methods for graphs:
  * Standard models comparisson.
    - Is the Erdös the only standard model to compare against?
    - Gaussian, power-law, geometric, Weibull,
    noise model distributions (black, purple, brown, green, white.).
    Make available the various color relation used (green, black).
    And the mathematical model of the distribution (equations and code).

Method suitable for any kind of data:
  * Curve fitting: power-law (Newman). Kolmogorov-Smirnv tests for all distributions (Fabbri, 2017). See what scipy has by standard.
      - make automatic methods or presenting the best guess for an empirical distribution.
      - minimum squares for lines and polinomials and probability distributions and other functions.
      Use other interpolation methods beyond minimum squares.
      - visual interface should have:
          * The empirical distribution and the fitted curve
	  * bin settings (width, number of bins, min max mean sample size, sample size distribution).
	  * measures of the empirical and fitted distributions or curves.
	  * widgets to change settings. These might be set also by the analysis.
  * Statistical and other measures: mean, Std, Kurtosis, etc. Median, quartiles, dispersion measures. Mean, max, etc.
  * 

The visual analytics interface should have:
  * a widget to define the data from linked data resources, by hand or by uploading files.
    - Should include a menu with the data items defined.
    - Should also include data generated by analysis.
    - Shoul enable dowloading of data items selected.
    - indications of methods suitable for each item,
    be them derived from the number of elements, serial or set organization,
    and relations established between elements.
    - should allow one to give metadata to each item:
    audio, social networks, set or sequence of topological measures and statistics, 
    a bag of words, a set or sequence of bag of words, etc.
    - persistent presentation of the visualization methods related to each data item.
    - Definition of data by SparQL queries and the LOSD, DBPedia, Data World sources (which other?).
    - Should allow one to group multiple items in one item.
    - Should allow one to define sets of internal structures of items as data items.
  * a widget for browsing analysis methods and data items that are suitable to each of them.
    - Colors in the data items widget and the analysis methods should reflect such relations.
    - Should include visualizations consistent with each analysis method.
    	- Curve fitting
	- Graph layout (include node and edge metadata and network metadata if any)
	- Text measures
	- Social Network (with text)
	- 
    - Displays data they generate (can be saved as data items)
    - Should have widgets that groups other analysis widgets in a chain to achieve statistics over large data bases (e.g. LOSD e linked data cloud)
       * The first node should be a data generator, which should iterate over items defined in the data selections widget.
       Both sequences of data items or data structure elements in the data item should be iterable.
       
  *

O vocabulário e ontologia Visual Analytics visa
sistematizar e contextualizar (via vínculos com outros vocabulários e ontologias)
o conhecimento utilizado por grupos de pesquisa
e do mercado para analisar os dados.
Há intuitos menores:
  * permitir consulta e rápida assimilação de aspectos da analítica visual
  tanto para o especialista quanto para outros interessados.
  * sustentar possíveis software de analítica visual. através de relações
  entre dados, métodos de análise e visualizações específicas.
      - 1D: histograms, medians, cumulativas, ajuste de curva ou distribuição).
      - 2D: scatter plot com ajuste de curva 2d histogram, 1d histogram of a measure over other measure, curve and distribution fitting
      - 3D: scatter plot com ajuste de curva, componentes principais, histograma 3d?, curve and distribution fitting
      - 4-XD: PCA, MDS, outro?
      - Riemmanian manifolds: circular statistics (circular histgrams?).
      - temporal/sequencial: timeline, 1D methods, other?
      - PCA: plot 1D, 2D, 3D. Visualização como tabela. (analíse -> visualização)
      - Histogram and derivatives (e.g. cumulative distribution): bar graph, timeline, other?
      - Suitable analysis and visualization for basic data types (linked list, set, dictionary, homogeneus and eterogeneous arrays).
	
A obtenção de cumulativa é uma técnica para análise de distribuições,
então ela é um item dentre as técnicas e métodos de processamento:
PCA e curve fitting é uma técnica de análise de distribuições
que resultam em boas visualizações de dados.
O curve fitting pode ser parametrizado e escrutinizado
através de uma interface visual.

a interface visual serve para:
  * a escolha de visualizações
  * a parametrização de visualizações
  * a audiovisualização de resultados, seja via texto, números, imagens, números, video ou música.
  * Download any of the information in any visualization or visualization interface.

Each visualization, datatype or analysis method has a standard visualization interface.

# Concept: Interface
# # narrower: Analysis, Visualization, Datatype, Widget

# Concept: Analysis
# # subClass: PCA, curve fitting, histogram, 1D method, 2D method, 3D method
# # necessaryAudiovisualization: class Visulization Interface
# # necessaryAudiovisualization: subPropertyOf skos:related
# # note: the analysis method might be tightly linked to a visualization Interface

# Concept: AudioVisualization
# # subClass: 1D visualizaton, 2D visualization, 3D visualization, audio

# Concept: Datatype
# # type: linked list, homogeneous and heterogeneous set, homogeneous array, heterogeneous array, dictionary with numbers or other datatypes, compound
# # datatypeChildren: same values as type
# # child: DataType Instance 
# # childs: set, array or dictionary of DataTypes

# Concept: Data
# # provenance: audio, social network, temporal/sequential, etc.
# # type: Data Type
# # data: the specific data structure

# Python parlance for synthesizing the triples:
import nltk
import percolation as p

skos = p.rdf.ns.skos
owl = p.rdf.ns.owl
rdf = p.rdf.ns.rdf
rdfs = p.rdf.ns.rdfs
aao = p.rdf.ns.aao # Audiovisual Analytics Ontology
aav = p.rdf.ds.aav # Audiovisual Analytics Vocabulary
po = p.rdf.ns.po # Participation Ontology

triples = [(aa.AudiovisualAnalytics, a, skos
]


# Interface
The interface uses Data, Analysis and Visualization
compatibilities for rendering itself.
An interface might be related to them by:
- dedicatedInterfaceOf
- possibleInterfaceOf
- isInterfaceOf

An interface has sessions, which are subInterfaces (?).

# Data, Analysis and Visualization compatibility

- Data and analysis:
the analysis method has to be compatible
with the "Data type ?" triple.

- Analysis and AudioVisualization:
an analysis method also generates data,
and for a visualization to be compatible
the "Analysis output ?data. ?data type ?"
should be compatible with visualization input.
"Visualization input ?data.
?data type ?".

- Data and AudioVisualizations.
Visualizations also might generate data.
"AudioVisualization output ?data".
Any data might be directly visualized without
any analysis (e.g. scatter plot). In which
The datatype of both data and
of the input of the visualization should be compatible
"select ?compatible where {
  Data type ?DataType1 .
  ?Datatype1 type ?dt1.
  AudioVisualization input ?DataType2 .
  ?Datatype2 type ?dt2.
  compare( ?d1, ?d2) as ?compatible.
  }

Data is a URI of an instance of the Data class.
Visualization and ?DataTypeX are classes/concepts.
?dt1, ?dt2 are data values, strings in this case.
?compatible is also a data value, a boolean.

- Visualization and Visualization:
The Visualization output might be compatible
with another visualization's input.

Other relation among visualizations
are if they are often used for the same type of
analysis or data.

- Analysis and Analysis
The Analysis output might be compatible with
another visualization's input.

Other relation among analysis methods
are if they are often used for the sime type of
data or visualization.

- Data and Data:
Data can always be merged toguether.
They are said compatible if their datatypes
match.

Other relation among data types and instances
are if they are often used for the same type of
analysis or visualization.


Each OWL class has a related SKOS concept.
Annotations are made in each class
and inherited by the concept.
  * super classes are maped to broader relations.
  * definitions and notes are inherited in related fields.
  * OWL properties have skos properties as superproperties (broader, related concept, etc)
  * How to map OWL meronyms to SKOS?
  * 




- Data and

- 

- Visualization and data

Or with the Data datatype ? tripe.





Distinguish between array and matrix?

A visualization is suitable for a analysis method if 
the output data type of the method is 

há técnicas e métodos de visualização.

Cada técnica TM de visualização e de processamento
deve possuir uma widget específica (com visualizações e parametrização)
no software de AA.
Cada tipo de dado deve ter também uma widget especifica.




and methods for tables:




    
Link to external semantic structures
from DBpedia and Wordnet as possible.

# Terms

