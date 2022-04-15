var introGuide = introJs();
introGuide.setOptions({
  exitOnOverlayClick: false,
});
introGuide.addSteps([{
    element: "#selectEmbeddingDiv",
    intro: "Select one Embedding method to show in the scatterplot.",
    position: "right"
  },
  {
    element: "#svg_force",
    intro: "Left Click one point to choose one image. Press CTRL and left click another point to choose another image for comparision.",
    position: "bottom"
  },
  {
    element: "#svg_psImage",
    intro: "This panel shows the persistent image for the first dataset",
    position: "right"
  },
  {
    element: "#webgl_surface",
    intro: "This panel shows the image and cycles for the first dataset",
    position: "right"
  },
  {
    element: "#svg_psImage2",
    intro: "This panel shows the persistent image for the second dataset",
    position: "right"
  },
  {
    element: "#webgl_surface2",
    intro: "This panel shows the image and cycles for the second dataset",
    position: "right"
  },
  {
    element: "#filterCycles",
    intro: "Use the slider to filter cycles by weights to the persistent image",
    position: "bottom"
  },
  {
    element: "#compareRange1",
    intro: "Use the slider to set the min threshold for pixel difference",
    position: "bottom"
  },
  {
    element: "#compareRange2",
    intro: "Use the slider to set the max threshold for pixel difference",
    position: "bottom"
  },
  {
    element: "#compare",
    intro: "The line chart shows sorted pixel difference for two persistent images",
    position: "bottom"
  }]);

// show onboarding when someone opens the page for the first time
function initHelp (elements1, elements2, currentGraph, graphic1, graphic2, svgs) {
  
  

    if (localStorage.getItem("hasLoadBefore") == null) {
        setTimeout(function () {
            introGuide.start()
            .onchange(function(targetElement){
                resetForBackwards(targetElement, elements1, elements2, currentGraph, graphic1, graphic2, svgs);
                openSection(targetElement);
            })
            .onbeforechange(function(targetElement){
                resetSection(targetElement, elements1, elements2, currentGraph, graphic1, graphic2, svgs)})
            .onafterchange(function(targetElement){
                resetFilterBackwards(targetElement, svgs, currentGraph)})
            .onexit(() => foldSection());
      console.log("onboarding");
    }, 2000);
    localStorage.setItem("hasLoadBefore", true);
  }
  ;
}

// when clicking "help" link
function helpOnClick(elements1, elements2, currentGraph, graphic1, graphic2, svgs) {
    console.log("onboarding");

    introGuide.start()
        .onchange(function(targetElement){
            //resetForBackwards(targetElement, elements1, elements2, currentGraph, graphic1, graphic2, svgs);
            openSection(targetElement);
        })
        .onbeforechange(function(targetElement){
            //resetSection(targetElement, elements1, elements2, currentGraph, graphic1, graphic2, svgs);
            })
        .onafterchange(function(targetElement){
           // resetFilterBackwards(targetElement, svgs, currentGraph);
             
            })
        .onexit(() => foldSection());
}

// open folded "Appearance"
function openSection(targetElement)
{

}
function foldSection(targetElement)
{
}
function resetForBackwards(targetElement, elements1, elements2, graph, graphic1, graphic2, svgs)
{

}

function resetFilterBackwards(targetElement, svgs, graph)
{
}
function resetSection(targetElement, elements1, elements2, graph, graphic1, graphic2, svgs)
{
}