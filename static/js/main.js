 var vishy = vishy || {};


 vishy.isSticky = function() {
    return document.getElementById("nav").className.indexOf('sticky-fixed') != -1
      }

window.onscroll = function(){
  var sTop = document.body.scrollTop;
  var d = document.getElementById("nav");

  if (sTop >= 100 && !vishy.isSticky()) {
    d.className = d.className + " sticky-fixed";
  } else if(sTop < 100 && vishy.isSticky()) {
    d.className = d.className.replace(/\b sticky-fixed\b/,'')
  }
};