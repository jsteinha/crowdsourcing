// For node.js
require('./sfig/internal/sfig.js');
require('./sfig/internal/Graph.js');
require('./sfig/internal/RootedTree.js');
require('./sfig/internal/metapost.js');
require('./sfig/internal/seedrandom.js');
require('./utils.js');

Text.defaults.setProperty('font', 'Times New Roman');  // For the paper

prez.addSlide(framework().id('framework'));

// For node.js: output PDF (you must have Metapost installed).
prez.writePdf({outPrefix: 'figures', combine: false});
