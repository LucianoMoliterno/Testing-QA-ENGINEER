/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 98.83786250965522, "KoPercent": 1.1621374903447792};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.7415209606066989, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.991, 500, 1500, "Forms"], "isController": false}, {"data": [0.9985, 500, 1500, "AlertsWindows-1"], "isController": false}, {"data": [0.00175, 500, 1500, "Index"], "isController": false}, {"data": [0.986, 500, 1500, "Elements"], "isController": false}, {"data": [1.0, 500, 1500, "Logout-1"], "isController": false}, {"data": [0.99, 500, 1500, "Logout-0"], "isController": false}, {"data": [0.10880829015544041, 500, 1500, "DemoQA-1"], "isController": false}, {"data": [0.0, 500, 1500, "DemoQA-0"], "isController": false}, {"data": [0.997, 500, 1500, "Widgets"], "isController": false}, {"data": [0.89, 500, 1500, "Authenticate"], "isController": false}, {"data": [0.472, 500, 1500, "Inicio"], "isController": false}, {"data": [0.99, 500, 1500, "Logout"], "isController": false}, {"data": [1.0, 500, 1500, "Interaction-1"], "isController": false}, {"data": [0.14082041020510255, 500, 1500, "Index-0"], "isController": false}, {"data": [0.9995, 500, 1500, "AlertsWindows-0"], "isController": false}, {"data": [0.08829414707353676, 500, 1500, "Index-1"], "isController": false}, {"data": [1.0, 500, 1500, "Interaction-0"], "isController": false}, {"data": [0.9504504504504504, 500, 1500, "Inicio-0"], "isController": false}, {"data": [0.9965, 500, 1500, "Elements-0"], "isController": false}, {"data": [0.9985, 500, 1500, "Books"], "isController": false}, {"data": [0.4864864864864865, 500, 1500, "Inicio-1"], "isController": false}, {"data": [0.9975, 500, 1500, "Elements-1"], "isController": false}, {"data": [0.0, 500, 1500, "DemoQA"], "isController": false}, {"data": [0.999, 500, 1500, "Forms-1"], "isController": false}, {"data": [0.998, 500, 1500, "Forms-0"], "isController": false}, {"data": [1.0, 500, 1500, "Widgets-1"], "isController": false}, {"data": [0.994, 500, 1500, "Interaction"], "isController": false}, {"data": [1.0, 500, 1500, "Widgets-0"], "isController": false}, {"data": [0.5225, 500, 1500, "Login"], "isController": false}, {"data": [0.935, 500, 1500, "Authenticate-0"], "isController": false}, {"data": [0.95, 500, 1500, "Authenticate-1"], "isController": false}, {"data": [1.0, 500, 1500, "Secure"], "isController": false}, {"data": [0.995, 500, 1500, "AlertsWindows"], "isController": false}, {"data": [0.9995, 500, 1500, "Books-1"], "isController": false}, {"data": [1.0, 500, 1500, "Books-0"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 28482, 331, 1.1621374903447792, 2210.025560002808, 145, 35621, 221.0, 452.0, 1100.0, 1107.0, 91.83624116928216, 419.2379484229249, 16.103118531126366], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["Forms", 1000, 0, 0.0, 446.1499999999999, 436, 1876, 440.0, 441.0, 443.0, 597.98, 3.432133002018094, 12.81687167941132, 0.7842960180392912], "isController": false}, {"data": ["AlertsWindows-1", 1000, 0, 0.0, 223.68300000000005, 219, 1879, 221.0, 222.0, 223.0, 236.99, 3.434573099736568, 11.524602705756688, 0.4192594115889366], "isController": false}, {"data": ["Index", 2000, 162, 8.1, 12170.368999999986, 976, 35621, 11531.5, 18771.4, 21559.85, 28416.88, 53.831453718407666, 986.9742338690685, 12.606890131685194], "isController": false}, {"data": ["Elements", 1000, 0, 0.0, 475.54200000000014, 437, 24447, 440.0, 442.0, 447.94999999999993, 612.6900000000003, 3.424188467333242, 12.797235609847965, 0.8025441720312285], "isController": false}, {"data": ["Logout-1", 100, 0, 0.0, 150.0899999999999, 146, 292, 148.0, 151.0, 153.0, 290.6799999999993, 3.6384805705137535, 13.867159074370543, 2.561859854824625], "isController": false}, {"data": ["Logout-0", 100, 0, 0.0, 199.14, 146, 5123, 148.0, 153.0, 154.95, 5073.649999999975, 3.6383481899217753, 5.216197471348008, 2.4480682645079135], "isController": false}, {"data": ["DemoQA-1", 193, 0, 0.0, 4953.3419689119155, 666, 19216, 3877.0, 10945.6, 13170.9, 19170.88, 7.8166133408934435, 26.228401796201045, 0.8549420841602203], "isController": false}, {"data": ["DemoQA-0", 193, 0, 0.0, 7849.699481865283, 1525, 20228, 6267.0, 16782.0, 20224.3, 20227.06, 9.357575757575757, 3.4999526515151516, 1.0234848484848484], "isController": false}, {"data": ["Widgets", 1000, 0, 0.0, 441.09799999999984, 437, 621, 440.0, 441.0, 443.0, 481.8700000000001, 3.4318032066769164, 12.82234284057215, 0.7976261359268614], "isController": false}, {"data": ["Authenticate", 100, 0, 0.0, 820.7799999999997, 293, 11823, 297.0, 1260.6000000000015, 5874.799999999999, 11800.879999999988, 3.6189924724956573, 17.167030073827444, 5.43909122575275], "isController": false}, {"data": ["Inicio", 1000, 1, 0.1, 1443.987, 1097, 21040, 1104.0, 1111.9, 2219.8999999999714, 11903.2, 3.3243686192899817, 12.394291570814037, 0.7264784298342136], "isController": false}, {"data": ["Logout", 100, 0, 0.0, 349.36000000000007, 293, 5416, 297.0, 303.9, 306.95, 5365.209999999974, 3.6187305493232973, 18.979959017876528, 4.982822338423681], "isController": false}, {"data": ["Interaction-1", 1000, 0, 0.0, 222.3240000000002, 219, 397, 221.0, 222.0, 223.0, 315.7800000000002, 3.4343136009121538, 11.523731965560705, 0.41252009073456536], "isController": false}, {"data": ["Index-0", 1999, 0, 0.0, 5100.906453226629, 355, 31700, 2719.0, 15307.0, 16614.0, 19032.0, 59.605808510003875, 13.34029742336822, 7.276099671631333], "isController": false}, {"data": ["AlertsWindows-0", 1000, 0, 0.0, 219.7670000000002, 217, 838, 219.0, 220.0, 220.0, 221.0, 3.43462028555433, 1.3282320635542137, 0.4192651715764563], "isController": false}, {"data": ["Index-1", 1999, 161, 8.054027013506753, 7058.100550275141, 268, 33476, 5234.0, 16483.0, 17516.0, 23727.0, 54.33541723294374, 984.4761070008834, 6.098538580456646], "isController": false}, {"data": ["Interaction-0", 1000, 0, 0.0, 219.12200000000013, 218, 231, 219.0, 220.0, 220.0, 223.0, 3.4343136009121538, 1.3214058191009654, 0.41252009073456536], "isController": false}, {"data": ["Inicio-0", 999, 0, 0.0, 640.7727727727724, 438, 16564, 441.0, 444.0, 764.0, 6899.0, 3.3283469210292225, 1.2448797565958907, 0.36403794448757115], "isController": false}, {"data": ["Elements-0", 1000, 0, 0.0, 248.65300000000013, 218, 24222, 219.0, 220.0, 220.0, 293.9000000000001, 3.4267699266671237, 1.3084639075457474, 0.4015746007813035], "isController": false}, {"data": ["Books", 1000, 0, 0.0, 440.9679999999998, 437, 1123, 440.0, 441.0, 442.0, 462.99, 3.43147347471004, 12.814408757120306, 0.7841453057442865], "isController": false}, {"data": ["Inicio-1", 999, 0, 0.0, 783.4114114114111, 658, 16819, 663.0, 667.0, 741.0, 4622.0, 3.328868184817162, 11.169913167023212, 0.36409495771437717], "isController": false}, {"data": ["Elements-1", 1000, 0, 0.0, 226.86200000000028, 218, 3539, 221.0, 222.0, 225.0, 320.94000000000005, 3.4346438789494114, 11.52484020319353, 0.4024973295643841], "isController": false}, {"data": ["DemoQA", 200, 7, 3.5, 13091.249999999995, 4311, 26329, 12629.5, 19324.0, 21054.75, 26217.140000000047, 7.583225904299689, 27.968995862402366, 1.6007715932357625], "isController": false}, {"data": ["Forms-1", 1000, 0, 0.0, 222.97899999999993, 218, 828, 221.0, 222.0, 223.0, 272.74000000000024, 3.4347146610795307, 11.525077710419207, 0.3924429837366261], "isController": false}, {"data": ["Forms-0", 1000, 0, 0.0, 223.14000000000013, 217, 1657, 219.0, 220.0, 220.0, 224.0, 3.434738255771219, 1.3014437922258135, 0.392445679614485], "isController": false}, {"data": ["Widgets-1", 1000, 0, 0.0, 221.98200000000008, 218, 400, 221.0, 222.0, 224.0, 257.9200000000001, 3.434384369429858, 11.523969427110343, 0.3991130273067901], "isController": false}, {"data": ["Interaction", 1000, 0, 0.0, 441.4650000000003, 437, 623, 440.0, 441.0, 443.0, 535.8000000000002, 3.4317325444924123, 12.835484028716737, 0.8244201229932944], "isController": false}, {"data": ["Widgets-0", 1000, 0, 0.0, 219.09000000000015, 217, 229, 219.0, 220.0, 220.0, 223.0, 3.434384369429858, 1.3080174844508248, 0.3991130273067901], "isController": false}, {"data": ["Login", 200, 0, 0.0, 3582.4499999999994, 146, 27208, 539.5, 13246.300000000003, 15323.849999999995, 20840.430000000044, 6.03974149906384, 20.350389940810533, 2.303241265023857], "isController": false}, {"data": ["Authenticate-0", 100, 0, 0.0, 377.81, 147, 9270, 149.0, 296.9, 1269.1999999999978, 9234.679999999982, 3.6384805705137535, 5.331226804686363, 2.803477705210304], "isController": false}, {"data": ["Authenticate-1", 100, 0, 0.0, 442.83999999999986, 145, 10545, 148.0, 311.9, 763.5999999999999, 10497.069999999974, 3.638612960739366, 11.928680911836407, 2.664999727104028], "isController": false}, {"data": ["Secure", 100, 0, 0.0, 156.37999999999997, 146, 375, 148.0, 153.0, 223.39999999999986, 374.3399999999997, 3.638612960739366, 9.241934786959211, 2.4482464159662336], "isController": false}, {"data": ["AlertsWindows", 1000, 0, 0.0, 443.4799999999996, 437, 2098, 440.0, 441.0, 442.0, 485.8000000000002, 3.432003432003432, 12.843200343200342, 0.8378914628914629], "isController": false}, {"data": ["Books-1", 1000, 0, 0.0, 221.89399999999995, 219, 904, 221.0, 222.0, 223.0, 243.0, 3.434054141297592, 11.522861356932152, 0.39236751419122873], "isController": false}, {"data": ["Books-0", 1000, 0, 0.0, 219.04200000000003, 218, 231, 219.0, 220.0, 220.0, 220.99, 3.434195659863525, 1.3012381992451636, 0.39238368379300037], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["Non HTTP response code: java.net.SocketException/Non HTTP response message: Connection reset", 132, 39.879154078549846, 0.46345060037918684], "isController": false}, {"data": ["Non HTTP response code: org.apache.http.conn.HttpHostConnectException/Non HTTP response message: Connect to demoqa.com:80 [demoqa.com/176.58.101.124] failed: Connection timed out: connect", 8, 2.416918429003021, 0.028087915174496172], "isController": false}, {"data": ["Non HTTP response code: java.net.SocketException/Non HTTP response message: Se produjo un error durante el intento de conexi&oacute;n ya que la parte conectada no respondi&oacute; adecuadamente tras un periodo de tiempo, o bien se produjo un error en la conexi&oacute;n establecida ya que el host conectado no ha podido responder", 1, 0.3021148036253776, 0.0035109893968120216], "isController": false}, {"data": ["Non HTTP response code: org.apache.http.NoHttpResponseException/Non HTTP response message: demoblaze.com:443 failed to respond", 166, 50.151057401812686, 0.5828242398707956], "isController": false}, {"data": ["Non HTTP response code: javax.net.ssl.SSLHandshakeException/Non HTTP response message: Remote host terminated the handshake", 24, 7.2507552870090635, 0.08426374552348852], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 28482, 331, "Non HTTP response code: org.apache.http.NoHttpResponseException/Non HTTP response message: demoblaze.com:443 failed to respond", 166, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Connection reset", 132, "Non HTTP response code: javax.net.ssl.SSLHandshakeException/Non HTTP response message: Remote host terminated the handshake", 24, "Non HTTP response code: org.apache.http.conn.HttpHostConnectException/Non HTTP response message: Connect to demoqa.com:80 [demoqa.com/176.58.101.124] failed: Connection timed out: connect", 8, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Se produjo un error durante el intento de conexi&oacute;n ya que la parte conectada no respondi&oacute; adecuadamente tras un periodo de tiempo, o bien se produjo un error en la conexi&oacute;n establecida ya que el host conectado no ha podido responder", 1], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["Index", 2000, 162, "Non HTTP response code: org.apache.http.NoHttpResponseException/Non HTTP response message: demoblaze.com:443 failed to respond", 83, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Connection reset", 66, "Non HTTP response code: javax.net.ssl.SSLHandshakeException/Non HTTP response message: Remote host terminated the handshake", 12, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Se produjo un error durante el intento de conexi&oacute;n ya que la parte conectada no respondi&oacute; adecuadamente tras un periodo de tiempo, o bien se produjo un error en la conexi&oacute;n establecida ya que el host conectado no ha podido responder", 1, "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["Inicio", 1000, 1, "Non HTTP response code: org.apache.http.conn.HttpHostConnectException/Non HTTP response message: Connect to demoqa.com:80 [demoqa.com/176.58.101.124] failed: Connection timed out: connect", 1, "", "", "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["Index-1", 1999, 161, "Non HTTP response code: org.apache.http.NoHttpResponseException/Non HTTP response message: demoblaze.com:443 failed to respond", 83, "Non HTTP response code: java.net.SocketException/Non HTTP response message: Connection reset", 66, "Non HTTP response code: javax.net.ssl.SSLHandshakeException/Non HTTP response message: Remote host terminated the handshake", 12, "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["DemoQA", 200, 7, "Non HTTP response code: org.apache.http.conn.HttpHostConnectException/Non HTTP response message: Connect to demoqa.com:80 [demoqa.com/176.58.101.124] failed: Connection timed out: connect", 7, "", "", "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
