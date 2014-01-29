var page = require('webpage').create();
page.open('http://localhost:9911/', function() {

  setTimeout(function(){
    var clipRect = page.evaluate(function () {
        return document.getElementById('paper').getBoundingClientRect();
    });

    page.clipRect = {
        top:    clipRect.top,
        left:   clipRect.left,
        width:  clipRect.width,
        height: clipRect.height
    };

    page.render('page/capture.png');
    phantom.exit();
  }, 300); /* wait 300 ms for ajax to complete */
});