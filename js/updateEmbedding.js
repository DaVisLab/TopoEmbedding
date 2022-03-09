function changeEmbedding(embedding) {

    d3.json("data/mnist_embeddings/embeddings_" + embedding + ".json").then(function (data) {

        var height = document.body.clientHeight - 100;
        var width = height


        var names = data.name
        var xcoords = data.x
        var ycoords = data.y

        var scaleX = d3.scaleLinear()
            .domain(d3.extent(xcoords))
            .range([0, width])

        var scaleY = d3.scaleLinear()
            .domain(d3.extent(ycoords))
            .range([0, height])

        var svg = d3.select("#svg_force")


        svg.selectAll('circle')
            .transition()
            .duration(2000)
            .attr("cx", (d, i) => scaleX(xcoords[i]))
            .attr("cy", (d, i) => scaleY(ycoords[i]))

        svg.selectAll('text')
            .transition()
            .duration(2000)
            .attr("x", (d, i) => scaleX(xcoords[i]))
            .attr("y", (d, i) => scaleY(ycoords[i]))

    })

}