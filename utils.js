G = sfig.serverSide ? global : this;
sfig.importAllMethods(G);

// Latex macros
sfig.latexMacro('R', 0, '\\mathbb{R}');
sfig.latexMacro('P', 0, '\\mathbb{P}');
sfig.latexMacro('E', 0, '\\mathbb{E}');
sfig.latexMacro('diag', 0, '\\text{diag}');

sfig.initialize();

G.prez = sfig.presentation();

// Useful functions (not standard enough to put into an sfig library).

G.frameBox = function(a) { return frame(a).bg.strokeWidth(1).fillColor('white').end; }
G.bigFrameBox = function(a) { return frameBox(a).padding(10).scale(1.4); }

G.bigArrow = function(a, b) { return arrow(a, b).strokeWidth(10).color('brown'); }
G.bigLeftArrow = function(s) { return leftArrow(s || 100).strokeWidth(10).color('brown'); }
G.bigRightArrow = function(s) { return rightArrow(s || 100).strokeWidth(10).color('brown'); }
G.bigUpArrow = function(s) { return upArrow(s || 100).strokeWidth(10).color('brown'); }
G.bigDownArrow = function(s) { return downArrow(s || 100).strokeWidth(10).color('brown'); }

G.xseq = function() { return new sfig.Table([arguments]).center().margin(5); }
G.yseq = function() { return ytable.apply(null, arguments).margin(10); }

G.stmt = function(prefix, suffix) {
  var m;
  if (!suffix && (m = prefix.match(/^([^:]+): (.+)$/))) {
    prefix = m[1];
    suffix = m[2];
  }
  return prefix.fontcolor('darkblue') + ':' + (suffix ? ' '+suffix : '');
}
G.headerList = function(title) {
  var contents = Array.prototype.slice.call(arguments).slice(1);
  return ytable.apply(null, [title ? stmt(title) : _].concat(contents.map(function(line) {
    if (line == _) return _;
    if (typeof(line) == 'string') return bulletedText([null, line]);
    if (line instanceof sfig.PropertyChanger) return line;
    return indent(line);
  })));
}

G.node = function(x, shaded) { return overlay(circle(20).fillColor(shaded ? 'lightgray' : 'white') , x).center(); }
G.indent = function(x, n) { return frame(x).xpadding(n != null ? n : 20).xpivot(1); }
G.stagger = function(b1, b2) { b1 = std(b1); b2 = std(b2); return overlay(b1.numLevels(1), pause(), b2); }

G.dividerSlide = function(text) {
  return slide(null, nil(), parentCenter(text)).titleHeight(0);
}

G.moveLeftOf = function(a, b, offset) { return transform(a).pivot(1, 0).shift(b.left().sub(offset == null ? 5 : offset), b.ymiddle()); }
G.moveRightOf = function(a, b, offset) { return transform(a).pivot(-1, 0).shift(b.right().add(offset == null ? 5 : offset), b.ymiddle()); }
G.moveTopOf = function(a, b, offset) { return transform(a).pivot(0, 1).shift(b.xmiddle(), b.top().up(offset == null ? 5 : offset)); }
G.moveBottomOf = function(a, b, offset) { return transform(a).pivot(0, -1).shift(b.xmiddle(), b.bottom().down(offset == null ? 5 : offset)); }
G.moveCenterOf = function(a, b) { return transform(a).pivot(0, 0).shift(b.xmiddle(), b.ymiddle()); }

var nl = greenitalics;
function wl(x) { return tt(x); }

////////////////////////////////////////////////////////////

G.framework = function(opts) {
  return xtable(frameBox('Data'), bigRightArrow(100), frameBox('Model')).center();
}
