# audiovisual analytics vocabulary and ontology (AAVO)
This repository holds:
* a SKOS vocabulary;
* an OWL ontology;
* Python code to synthesize them both.
* This README.md with directions on the implementation
and intended uses.

In summary, audiovisual analytics (AA) is an extension of visual analytics
to encompass both visualizing and hearing data.
It is a broad subject which related data structures and provenance,
analysis techniques and methods, audiovisualization of data and
visual interfaces.
Therefore, AAVO should strive to use already existing vocabularies
and ontologies (e.g. DBpedia and Wordnet).

AAVO formalizes the knowledge involved in AA
and gives context by relations to external vocabularies and ontologies.

Check the documentation in this README.md and in the [wiki]
for further directions on how AAVO is being implemented.

[wiki]: https://github.com/ttm/aavo/wiki/notes-on-the-audiovisual-analytics-framework

# intended use
AAVO is intended for conceptual organization and discussion
and for obtaining relations by machine inference
(e.g. what analysis and visualizations might be useful for a given dataset).
Other and minor intended uses are described at the end of this README
(includes Portuguese text for now).

It is also conceived as a part of an [AA] framework
in which the following components are foreseen:
* [Social]/[Participation]/[Gmane]: routines for representing data
from diverse provenance as linked data. (Done)
* [Percolation]: linked data and data analysis facilities. (migrating code)
* [Visuals]: useful routines for generating images and videos. (migrating code, WIP)
* [Music]: routines useful for rendering sound and music. (migrating code, WIP)
* [AAVO]: the conceptualization formalized as linked data/semantic web. (WIP)
* [AAI]: a gluing component for providing audiovisual analytics interfaces.
Should include a web frontend using D3.js and ccNetViz. (incipient)

All implementations should be in Python (backend)
and Javascript (frontend).

[AA]: https://github.com/ttm/aavo/wiki/notes-on-the-audiovisual-analytics-framework "Audiovisual Analytics"
[AAI]: https://github.com/ttm/AAI "Audiovisual Analytics Interface"
[AAVO]: https://github.com/ttm/AAVO "Audiovisual Vocabulary and Ontology"
[Social]: https://github.com/ttm/social "Social Python package"
[Participation]: https://github.com/ttm/participation "Participation Python package"
[Gmane]: https://github.com/ttm/gmane "Gmane Python package"
[Percolation]: https://github.com/ttm/Percolation "Percolation Python package"
[Music]: https://github.com/ttm/Music "Music Python package"
[Visuals]: https://github.com/ttm/visuals "Visuals Python package"

# implementation details
Each concept is related both to an OWL class and a SKOS
concept for [allowing OWL DL inference to be made in the ontology][1].
This have pros and cons, but the other possibilities:
* yields OWL Full (if a SKOS concept, and instance, is a class), or
* annotations on instances o OWL classes, not on the classes
(if we annotate instances of OWL classes with SKOS properties), or
* a less formal ontology (if we went from SKOS to OWL), or
* would extrapolate the purpose of SKOS AFAIK
(giving enough expressive power to SKOS to achieve
an OWL without degeneration of the conceptualization).

Therefore, conceptualization is formalized in OWL (as an ontology)
from which the SKOS vocabulary is automatically derived.
SKOS is less formal then OWL so a small set of conventions
allows [Percolate] to output the vocabulary
from the ontology.

The ontology rdf/audiovisualAnalyticsOntology.owl is synthesized by the src/ontology.py file.
The vocabulary rdf/audiovisualAnalytics.skos is then obtained from rdf/audiovisualAnalytics.owl
by means of src/vocabulary.py.
Example usages of AAVO for reasoning and extracting knowledge
should be in src/sparql.py.

Visualization of RDF code:
* multiple RDF text formats (Turtle, n3, Manchester, XML, etc).
* diagram view (nodes are classes or concepts or raw data).
* Tree view for the taxonomic relations.
* These files should be in the rdf/ and img/ directories.
* (See [VIOLA] for good online tools for visualizing OWL and data from endpoints as node-edge diagrams, but no textual visualization.)

Notes on the implementation of the full [AA] framework should be in the [wiki]
of this repository while other components are incipient.

### deriving the vocabulary from the ontology
By standard, each OWL class and property is a subclass of skos:Concept.
Both subClassOf and subPropertyOf are subProperties of skos:broader.
OWL properties also yield skos:related.
OWL properties can be annotated to yield vocabulary relations and not concepts.
See [issues](#issues).

# conceptualization details
* Text and numbers are considered visualization.
* Some analysis methods involve visualization.
  - We keep under analysis methods only what involves data processing
and arbitrary consultation.
  - Under visualization are kept only methods for representing data visually.
  - Example: PCA in an analysis. The scatter plot is a visualization
  (which might be useful for plotting data with respect to the first principal components).
  - Relations between analysis and visualization concepts are defined in the ontology and vocabulary.
  - If for an analysis technique this distinction is not possible,
  we can use the concept of (audio)visual analysis.

# core and extended AAVO
Both the ontology and vocabulary have core and extended versions.
Extended includes core.
Core is meant to keep a very simple representation of the knowledge.
* Core includes: data, analysis, audiovisualization and interface concepts as OWL classes and properties,
and as SKOS concepts. Some sub classes and properties.
* Extended also includes: knowledge from other fields such as statistics, complex networks,
text mining, audio and music, visual design, HCI, UI, etc.
When necessary to better account for the [AA] field and
link to external OWL.
Also includes definitions of further sub classes and properties of the main classes.

# further notes
* Maybe start from this linking to Wordnet and DBPedia and LOSD
and then grow from them.
* Revisit Pandas, Sympy, other python data-related libraries
and the Entoght videos for obtaining a solid conceptualization
of the analysis (and visualizations).
* Defining classes as of owl:type another class and rdfs:subClassOf skos:Concept
allows for annotating instances of the class with SKOS properties.
This does not enable the annotations to be directly annotated in the classes,
reason why we did not choose this approach.
* Pseudocodes for data structures and algorithms are written as RDF Schema (RDFS).
RDF collections, RDFS containers, and SparQL queries.
- Each OWL class has a related SKOS concept.
Annotations are made in each class
and inherited by the concept.
  * super classes are maped to broader relations.
  * definitions and notes are inherited in related fields.
  * OWL properties have skos properties as superproperties (broader, related concept, etc)
  * If needed, define ontology annotation properties that can be mapped or inherited by the vocabulary. Another approach is to use textual tags in the string.
  The first approach leads to better defined ontological structures while the second might involve in simples structures and less coding (an maybe to less clear and less clean comments).
  * How to map OWL meronyms to SKOS?
* [MOOC in semantic web][3]. Another [MOOC][8]. And [another MOOC][15].
  - Send to Tomas and Ales: https://www.coursera.org/learn/web-semantica/lecture/A33ef/aplicaciones-en-biologia-de-la-web-semantica
  - What are the most useful analysis and visualizations for biological and medical data? [MOOC][4], [MOOC specialization][5]. This other [MOOC specialization][6] has a Python for BioInformatics course. A [MOOC for big data and bioinformatics][7].
  - How to combine these bio data with textual and social networks data?
    * Search drug names in texts of social networks.
    * What kind of bio data exhibits the same [stable patterns found in social networks][2].
* Maybe use [EARL][13] to report on the tests performed.
The application of analysis methods to data most yields automated results.
Audiovisualization should require annotation by the user to yield results.
Output EARL RDF for the user, allow for changing and adding to it.
* Get text from Gutemberg books, DBpedia (or wikipedia pages)j.
* Get networks from SparQL queries and from the online networks repository (find URL again to cite ).
* Use [Content RDF][12] to represent content.
* Understand what Google Cloud and Firebase and other services can and cannot provide.
  - Firebase (BaaS) is a slim backend that delivers frontend. App engine (PaaS) the backend. Cloud (DaaS?) deals with massive data. Is that it?
* Use [algorithmia][8] (AaaS?) for running algorithms?
* Explore the open model of the semantic web (anyone can say anything about anything).
  - Make some text about this design, what it implied for AAVO/AAI and possibilites.
  - Make the open design of the semantic web very explicit in AAI.
* Algorithmia post has good resources for NLP and text mining: http://blog.algorithmia.com/introduction-natural-language-processing-nlp/
* Revisit scikit-learn, scipy, anaconda, etc. Maybe use e.g. scipy to derive ontology until it reaches DBpedia or so.
* Study [KNIME][9] (and [book][11]) in depth to understand their approaches.
* See with Vilson Vieira (The Grid) how to implement the dataflow in client JS.
* [Course on ETL with KNIME!!!][10]
* See source of KNIME to know if they use a vocabulary or ontology for organizing all the concepts.
* Understand [RIF][14] and confirm that we do not need it for now.
* [WebVOWL] for visualizing OWL ontologies online.
It is very good. The [VOWL] project includes online querying an endpoint
for visualizing the structure of data and other tools.
* A list of alive SparQL endpoints [HERE].
They ([SPARQLES]) provide 24h updated information on endpoint availability.
* DBPedia [Spotlight] searching in a text for terms on DBpedia, Freebase and others

[Spotlight]: http://demo.dbpedia-spotlight.org/
[HERE]: http://sparqles.ai.wu.ac.at/availability
[SPARQLES]: http://sparqles.ai.wu.ac.at/
[VOWL]: http://vowl.visualdataweb.org/
[WebVOWL]: http://visualdataweb.de/webvowl/#
[2]: https://github.com/ttm/thesis/raw/master/tese-rfabbri.pdf
[3]: https://www.coursera.org/learn/web-semantica
[4]: https://www.coursera.org/specializations/bioinformatics
[5]: https://www.coursera.org/learn/bioinformatics-pku/
[6]: https://www.coursera.org/specializations/genomic-data-science
[7]: https://www.coursera.org/learn/data-genes-medicine
[8]: https://algorithmia.com
[9]: https://tech.knime.org/screencasts
[10]: https://www.knime.org/knime-introductory-course
[11]: https://www.knime.org/knimepress/will-they-blend
[12]: https://www.w3.org/TR/Content-in-RDF10/#namespaces
[13]: https://www.w3.org/TR/EARL10-Schema/
[14]: https://www.w3.org/TR/rif-fld/
[15]: https://miriadax.net/web/semantic-web-and-linked-data

<a name="issues"></a>
# issues
* Find the [difference between using an inference process
or a model-driven transformation][1].
* Find the difference between skos Collection and Concept Scheme.
* Define the set of external properties and classes that will be used.
* Distinguish between array and matrix?
* What is the difference between method and technique?
* Any better way for linking resources with properties without axioms (including range and domain) and restrictions? 
  - One approach is to define subclasses, but it is clumsy. Ex:
    * :Analysis should have a name, but it is not necessary.
    * One way is to write:
      - :analysisName rdfs:subPropertyOf dct:title . 
      - :analysisName rdfs:domain :Analysis
    * Now the ontology has some explicit bond between :analysis and a naming property.
    * But this could be substituted by something like:
      - dct:title :unrestrictiveDomain :Analysis
      OR:
      - :Analysis :usesProperty dct:title
      - This approach yields less (unecessary) triples, the correct meaning and the desired non-restrictive bond between :Analysis and dct:title.
    * Class restrictions have inference costs, add many triples and asserts a wrong meaning in this context.
 * Revisit Curl documentation.
* What should we use to yield a SKOS with relations such as meronymy and hyponymy (which is related to OWL sub and super classes)?


[1]: https://www.w3.org/2006/07/SWD/SKOS/skos-and-owl/master.html

 
# drafts in English:
Should include subfields like data visualization,
information and scientific visualization,
HCI, visual design, UI.
Should include visualization methods including other
senses, at least hearing
(for the blind to have information of the visual environment,
such as location and colors. Michel Hospital (FEE/UFSCar).

# drafts in a English and Portuguese mix
Há intuitos menores do AAVO:
  * permitir consulta e rápida assimilação de aspectos da analítica audiovisual
  tanto para o especialista quanto para outros interessados.
  * sustentar possíveis software de analítica visual através de relações
  entre dados, métodos de análise e visualizações específicas:
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

Each visualization, datatype or analysis method should have a standard visualization interface.

- Concept: Interface
  * narrower: Analysis, Visualization, Datatype, Widget
 
- Concept: Analysis
  * subClass: classification, regression, clustering, dimensionality reduction,
  model selection, preprocessing, NN, GA, PCO, ACO, etc.
  PCA, curve fitting, most probable distributions, histogram,
  1D method, 2D method, 3D method,
  most frequent values, most frequent sequences of values, stability measures,
  difference measures between data items, bag of words,
  regression, ML algs, FP-Growth, POS tagging, ensemble learning, GLM, 
  * necessaryAudiovisualization: class Visulization Interface
  * necessaryAudiovisualization: subPropertyOf skos:related
  * note: the analysis method might be tightly linked to a visualization Interface
 
- Concept: AudioVisualization
  * subClass: 1D visualizaton, 2D visualization, 3D visualization, audio
  * Auralization subClassOf Audiovisualization
  * Visualization subClassOf Audiovisualization
 
- Concept: Datatype
  * type: linked list, homogeneous and heterogeneous set, homogeneous array, heterogeneous array, dictionary with numbers or other datatypes, compound
  * datatypeChildren: same values as type
  * child: DataType Instance 
  * childs: set, array or dictionary of DataTypes
 
- Concept: Data
  * provenance: audio, social network, temporal/sequential, etc.
  * type: Data Type
  * data: the specific data structure

The interface uses Data, Analysis and Visualization
compatibilities for rendering itself.
An interface might be related to them by:
- dedicatedInterfaceOf
- possibleInterfaceOf
- isInterfaceOf

An interface has sessions, which are subInterfaces (?).

Outras notas:
- Olho mágico para visualizações.
- DoIn sonoro e sons binaurais para audio de acompanhamento.
- https://datadotworld.gitbooks.io/sparql/content/ para aprender SparQL.
- Reler a documentação de RDF(s), SKOS e OWL.
- Encontrar outros trabalhos interessantes e fazer uma lista das classes
e propriedades que usam.

## Data, Analysis and Visualization compatibility
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

- Analysis and Analysis:
An analysis output might be compatible with
another analysis's input.
Other relation among analysis methods
are if they are often used for the same type of
data or visualization.

- Data and Data:
Data can always be merged together.
They are said compatible if their datatypes
match.
Other relations among data types and instances
are if they are often used for the same type of
analysis or visualization.


