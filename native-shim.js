/* Capacitor plugin bridge for the legacy single-file PROTOCOL SAKHA app. */
(function(){
  var C=window.Capacitor;
  if(!C || !C.isNativePlatform || !C.isNativePlatform()) return;
  C.Plugins=C.Plugins||{};
  var P=window.PDRNativePlugins||{};
  ['Filesystem','Share','App'].forEach(function(n){
    try {
      if(P[n]) C.Plugins[n]=P[n];
      else if(!C.Plugins[n] && C.registerPlugin) C.Plugins[n]=C.registerPlugin(n);
    } catch(e) {}
  });
})();
