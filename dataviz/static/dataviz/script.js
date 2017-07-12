$(function() {

    var margin = {top: 50, right: 50, bottom: 50, left: 50},
        width = 1000 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

    var parseTime = d3.timeParse('%Y-%m-%d');

    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);

    var xdate = function() {
        return function(d) { return x(d.date)};
    };

    var xtemp = function(varname) {
        return function(d) { return y(d[varname])};
    }

    var lines = [];

    var temps = ['temp1', 'temp2', 'temp3', 'temp4'];


    for(var i = 0; i < temps.length; i++) {
        var line = d3.line()
            .x(xdate())
            .y(xtemp(temps[i]))
            .curve(d3.curveMonotoneX);
        lines.push(line);
    }

    var svg = d3.select("#plot").attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var datap = $.get('/dataviz/data');
    datap.then(function(data) {

        var parseddata = JSON.parse(data);

        var plotdata = [];

        parseddata.forEach(function(d) {
            var obj = {
                date: parseTime(d.fields.date),
                temp1: +d.fields.temp1,
                temp2: +d.fields.temp2,
                temp3: +d.fields.temp3,
                temp4: +d.fields.temp4,
            };
            plotdata.push(obj);
        });

        x.domain(d3.extent(plotdata, function(d) { return d.date; }));
        y.domain([-100, 100]);

        for(var i = 0; i < lines.length; i++) {
            svg.append('path')
                .data([plotdata])
                .attr('class', 'line ' + 'color' + (i + 1))
                .attr('d', lines[i]);
        }

        svg.append('g')
            .attr('transform', 'translate(0,' + height + ')')
            .call(d3.axisBottom(x));

        svg.append('g')
            .call(d3.axisLeft(y));

    });


});

