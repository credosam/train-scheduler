import sys
from PyQt4 import QtGui, QtWebKit

class Example(QtWebKit.QWebView):
    
    def __init__(self):
        super(Example, self).__init__()
        html = """<head>
    <title>Train-Scheduler</title>
    <link href="jquery-ui-1.8.20.custom.css" rel="stylesheet" type="text/css">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js"></script>

    <script src="eRailText_11.js" type="text/javascript"></script>
    <script src="erail_mobile.js" type="text/javascript"></script>
    <script src="train.js" type="text/javascript"></script>
    <script src="station.js" type="text/javascript"></script>

    <style type="text/css">
    html,
    body {
        height: 100%;
        width: 100%;
        margin: 0;
        padding: 0;
    }
    body {
        font-family: arial, sans-serif;
        font-size: 12px;
        margin: 0 auto;
        background: url('main-bg.gif') scroll center top;
        color: #222222;
    }
    TR {
        background-color: White;
    }
    TABLE {
        background-color: #c0c0c0;
        text-indent: 3px;
    }
    </style>
    <script type="text/javascript" src="chrome-extension://bfbmjmiodbnnpllbbbfblcplfjjepjdn/js/injected.js"></script>
    <style type="text/css"></style>
</head>

<body>
    <table style="border-spacing: 0px">
        <tbody>
            <tr>
                <td>
                    <table style="border-spacing: 0px;width:100%">
                        <tbody>
                            <tr>
                                <td style="width:60px">
                                    <div id="divTime" style="width:100%;height:18px;overflow:hidden">06:36:23 GMT+0530 (IST)</div>
                                </td>
                                <td>
                                    <div id="slider" class="ui-slider ui-slider-horizontal ui-widget ui-widget-content ui-corner-all">
                                        <a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 27.5%;"></a>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td>
                    <select id="selectStation" onchange="GetTrains($(this).val())">
                        <option value="NDLS">NDLS- New Delhi</option>
                        <option value="DLI">DLI- Delhi</option>
                        <option value="NZM">NZM - H Nizamuddin</option>

                    </select>
                    <option value="1">Speed 1x</option>
                    <option value="10">Speed 10x</option>
                    <option value="50" selected="selected">Speed 50x</option>
                    <option value="100">Speed 100x</option>

                </td>
            </tr>
            <tr>
                <td>
                    <div style="width: 800px; height: 550px;">
                        <canvas id="canvas0" style="width: 800px; border: 1px solid black; height: 550px; z-index: 0; position:absolute " width="800" height="550">Sorry! Your browser doesn't support "Canvas".</canvas>
                        <canvas id="canvas1" style="width: 800px; border: 1px solid black; height: 550px; z-index: 1; position:absolute " width="800" height="550">Sorry! Your browser doesn't support "Canvas".</canvas>
                    </div>
                </td>
                <td>
                    <div id="divTrainsList" style="height: 550px; overflow: auto;">
                        <table style="border-spacing: 1px">
                            <tbody>
                                <tr>
                                    <td>No</td>
                                    <td>Name</td>
                                    <td>A/D</td>
                                    <td>Time</td>
                                    <td>P/F</td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>12446</td>
                                    <td>UTTAR S KRANTI</td>
                                    <td>D</td>
                                    <td>06.30</td>
                                    <td>1</td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>64908</td>
                                    <td>SSB PWL MEMU</td>
                                    <td>D</td>
                                    <td>06.35</td>
                                    <td>9</td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12037</td>
                                    <td>NDLS LDH SHTBDI</td>
                                    <td>A</td>
                                    <td>06.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>12451</td>
                                    <td>SHRAM SHKTI EXP</td>
                                    <td>D</td>
                                    <td>06.40</td>
                                    <td>6</td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>12497</td>
                                    <td>SHANE PUNJAB</td>
                                    <td>D</td>
                                    <td>06.40</td>
                                    <td>2</td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>12615</td>
                                    <td>GRAND TRUNK EXP</td>
                                    <td>D</td>
                                    <td>06.40</td>
                                    <td>7</td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12820</td>
                                    <td>ORISSA S KRNTI</td>
                                    <td>A</td>
                                    <td>06.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64437</td>
                                    <td>GZB DLI EMU</td>
                                    <td>A</td>
                                    <td>06.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>12017</td>
                                    <td>DEHRADUN SHTBDI</td>
                                    <td>D</td>
                                    <td>06.50</td>
                                    <td>3</td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12229</td>
                                    <td>LUCKNOW MAIL</td>
                                    <td>A</td>
                                    <td>06.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#F3F781">
                                    <td>12553</td>
                                    <td>VAISHALI EXP</td>
                                    <td>D</td>
                                    <td>06.50</td>
                                    <td>8</td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12417</td>
                                    <td>PRAYAG RAJ EXP</td>
                                    <td>A</td>
                                    <td>06.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12029</td>
                                    <td>SWARNA SHTBDI</td>
                                    <td>A</td>
                                    <td>07.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12621</td>
                                    <td>TAMIL NADU EXP</td>
                                    <td>A</td>
                                    <td>07.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>13008</td>
                                    <td>U A TOOFAN EXP</td>
                                    <td>A</td>
                                    <td>07.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12011</td>
                                    <td>KALKA SHTBDI</td>
                                    <td>A</td>
                                    <td>07.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12381</td>
                                    <td>POORVA EXPRESS</td>
                                    <td>A</td>
                                    <td>07.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>51902</td>
                                    <td>DELHI AGRA PASS.</td>
                                    <td>A</td>
                                    <td>07.23</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64011</td>
                                    <td>PWL SSB EMU</td>
                                    <td>A</td>
                                    <td>07.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12271</td>
                                    <td>NDLS DURONTO EX</td>
                                    <td>A</td>
                                    <td>07.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12957</td>
                                    <td>SWARNA J RAJ EX</td>
                                    <td>A</td>
                                    <td>07.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12309</td>
                                    <td>RJPB RAJDHANI</td>
                                    <td>A</td>
                                    <td>07.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64464</td>
                                    <td>PNP NDLS MEMU</td>
                                    <td>A</td>
                                    <td>07.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12559</td>
                                    <td>SHIV GANGA EXP</td>
                                    <td>A</td>
                                    <td>07.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64053</td>
                                    <td>PWL GZB EMU</td>
                                    <td>A</td>
                                    <td>07.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64465</td>
                                    <td>NDLS KKDE MEMU</td>
                                    <td>A</td>
                                    <td>07.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64417</td>
                                    <td>GZB DLI EMU</td>
                                    <td>A</td>
                                    <td>08.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64905</td>
                                    <td>MTJ NDLS EMU</td>
                                    <td>A</td>
                                    <td>08.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>04201</td>
                                    <td>LKO NDLS SPL</td>
                                    <td>A</td>
                                    <td>08.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>04205</td>
                                    <td>LKO NDLS SPL</td>
                                    <td>A</td>
                                    <td>08.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64078</td>
                                    <td>NDLS PWL EMU</td>
                                    <td>A</td>
                                    <td>08.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54474</td>
                                    <td>SRE DLI PASS</td>
                                    <td>A</td>
                                    <td>08.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12951</td>
                                    <td>MUMBAI RAJDHANI</td>
                                    <td>A</td>
                                    <td>08.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54002</td>
                                    <td>ROK TKJ PASS</td>
                                    <td>A</td>
                                    <td>08.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64472</td>
                                    <td>PNP GZB MEMU</td>
                                    <td>A</td>
                                    <td>08.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12393</td>
                                    <td>S KRANTI SUP EX</td>
                                    <td>A</td>
                                    <td>08.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64424</td>
                                    <td>NDLS GZB EMU</td>
                                    <td>A</td>
                                    <td>08.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54012</td>
                                    <td>RE TKJ PASS</td>
                                    <td>A</td>
                                    <td>08.53</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64075</td>
                                    <td>PWL NDLS EMU</td>
                                    <td>A</td>
                                    <td>08.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64439</td>
                                    <td>GZB DLI EMU</td>
                                    <td>A</td>
                                    <td>08.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54021</td>
                                    <td>BSC TKJ PASS</td>
                                    <td>A</td>
                                    <td>08.58</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64470</td>
                                    <td>PNP NDLS LADIES SPL</td>
                                    <td>A</td>
                                    <td>09.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64903</td>
                                    <td>MTJ GZB EMU</td>
                                    <td>A</td>
                                    <td>09.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12723</td>
                                    <td>A P EXP</td>
                                    <td>A</td>
                                    <td>09.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54412</td>
                                    <td>MUT RE PASS</td>
                                    <td>A</td>
                                    <td>09.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64071</td>
                                    <td>BVH SSB EMU</td>
                                    <td>A</td>
                                    <td>09.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64095</td>
                                    <td>NDLS SSB EMU</td>
                                    <td>A</td>
                                    <td>09.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64426</td>
                                    <td>NDLS GZB EMU</td>
                                    <td>A</td>
                                    <td>09.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64093</td>
                                    <td>DBSI SSB EMU</td>
                                    <td>A</td>
                                    <td>09.21</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64091</td>
                                    <td>NZM HNZM EMU</td>
                                    <td>A</td>
                                    <td>09.21</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64462</td>
                                    <td>KKDE NZM MEMU</td>
                                    <td>A</td>
                                    <td>09.23</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64077</td>
                                    <td>PWL NDLS EMU</td>
                                    <td>A</td>
                                    <td>09.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64105</td>
                                    <td>ALJN NDLS EMU</td>
                                    <td>A</td>
                                    <td>09.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64094</td>
                                    <td>SSB NZM SSB EMU</td>
                                    <td>A</td>
                                    <td>09.34</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64090</td>
                                    <td>NZM HNZM EMU</td>
                                    <td>A</td>
                                    <td>09.34</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64428</td>
                                    <td>NDLS GZB EMU</td>
                                    <td>A</td>
                                    <td>09.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64449</td>
                                    <td>GZB NDLS LADIES SPL</td>
                                    <td>A</td>
                                    <td>09.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64411</td>
                                    <td>SBB DLI EMU</td>
                                    <td>A</td>
                                    <td>09.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14086</td>
                                    <td>SIRSA EXP</td>
                                    <td>A</td>
                                    <td>09.43</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64031</td>
                                    <td>GZB SSB EMU</td>
                                    <td>A</td>
                                    <td>09.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64055</td>
                                    <td>PWL GZB EMU</td>
                                    <td>A</td>
                                    <td>09.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12301</td>
                                    <td>KOLKATA RJDHNI</td>
                                    <td>A</td>
                                    <td>09.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64491</td>
                                    <td>PWL NDLS LADIES EMU</td>
                                    <td>A</td>
                                    <td>09.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>11078</td>
                                    <td>JHELUM EXPRESS</td>
                                    <td>A</td>
                                    <td>10.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14315</td>
                                    <td>INTERCITY EXP</td>
                                    <td>A</td>
                                    <td>10.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12423</td>
                                    <td>DBRT RAJDHANI E</td>
                                    <td>A</td>
                                    <td>10.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14323</td>
                                    <td>NDLS ROK EXP</td>
                                    <td>A</td>
                                    <td>10.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12313</td>
                                    <td>SDAH RAJDHANIEX</td>
                                    <td>A</td>
                                    <td>10.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14211</td>
                                    <td>INTERCITY EXP</td>
                                    <td>A</td>
                                    <td>10.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12006</td>
                                    <td>KALKA SHTBDI</td>
                                    <td>A</td>
                                    <td>10.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12627</td>
                                    <td>KARNATAKA EXP</td>
                                    <td>A</td>
                                    <td>10.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64430</td>
                                    <td>NDLS GZB EMU</td>
                                    <td>A</td>
                                    <td>10.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64423</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>10.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>22823</td>
                                    <td>BBS RAJDHANI EX</td>
                                    <td>A</td>
                                    <td>10.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64012</td>
                                    <td>SSB PWL EMU</td>
                                    <td>A</td>
                                    <td>10.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12925</td>
                                    <td>PASCHIM EXPRESS</td>
                                    <td>A</td>
                                    <td>10.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12441</td>
                                    <td>BSP NDLS RAJ EX</td>
                                    <td>A</td>
                                    <td>10.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64901</td>
                                    <td>KSV GZB EMU</td>
                                    <td>A</td>
                                    <td>10.48</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>04024</td>
                                    <td>DEE DBG SPL</td>
                                    <td>A</td>
                                    <td>10.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12249</td>
                                    <td>HWH NDLS YUVA E</td>
                                    <td>A</td>
                                    <td>10.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12259</td>
                                    <td>SDAH DURONTO EX</td>
                                    <td>A</td>
                                    <td>11.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12056</td>
                                    <td>NDLS JANSHATABD</td>
                                    <td>A</td>
                                    <td>11.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12626</td>
                                    <td>KERALA EXPRESS</td>
                                    <td>A</td>
                                    <td>11.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12014</td>
                                    <td>AMRITSAR SHTBDI</td>
                                    <td>A</td>
                                    <td>11.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12033</td>
                                    <td>CNB NDLS SHT</td>
                                    <td>A</td>
                                    <td>11.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14258</td>
                                    <td>KASHI V EXPRESS</td>
                                    <td>A</td>
                                    <td>11.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12192</td>
                                    <td>JBP NDLS SUP EX</td>
                                    <td>A</td>
                                    <td>11.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12401</td>
                                    <td>MAGADH EXPRESS</td>
                                    <td>A</td>
                                    <td>11.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64434</td>
                                    <td>DLI GZB EMU</td>
                                    <td>A</td>
                                    <td>11.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12058</td>
                                    <td>NDLS JANSHTBDI</td>
                                    <td>A</td>
                                    <td>12.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12420</td>
                                    <td>GOMTI EXPRESS</td>
                                    <td>A</td>
                                    <td>12.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12715</td>
                                    <td>SACHKHAND EXP</td>
                                    <td>A</td>
                                    <td>12.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64057</td>
                                    <td>PWL GZB EMU</td>
                                    <td>A</td>
                                    <td>12.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12561</td>
                                    <td>SWATANTRA S EXP</td>
                                    <td>A</td>
                                    <td>12.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>19024</td>
                                    <td>FZR BCT JANTA</td>
                                    <td>A</td>
                                    <td>12.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64052</td>
                                    <td>GZB PWL EMU</td>
                                    <td>A</td>
                                    <td>12.38</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>19023</td>
                                    <td>FZR JANATA EXP</td>
                                    <td>A</td>
                                    <td>12.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14682</td>
                                    <td>JUC NDLS EXPRES</td>
                                    <td>A</td>
                                    <td>12.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12392</td>
                                    <td>SHRAMJEVI N EXP</td>
                                    <td>A</td>
                                    <td>12.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12716</td>
                                    <td>ASR NED EXPRESS</td>
                                    <td>A</td>
                                    <td>13.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12459</td>
                                    <td>NDLSASR EXPRESS</td>
                                    <td>A</td>
                                    <td>13.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>16688</td>
                                    <td>NAVYUG EXPRESS</td>
                                    <td>A</td>
                                    <td>13.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64432</td>
                                    <td>NDLS GZB EMU</td>
                                    <td>A</td>
                                    <td>13.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64425</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>13.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64014</td>
                                    <td>SSB PWL EMU</td>
                                    <td>A</td>
                                    <td>13.33</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12424</td>
                                    <td>DBRT RAJDHANI</td>
                                    <td>A</td>
                                    <td>13.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12625</td>
                                    <td>KERALA EXPRESS</td>
                                    <td>A</td>
                                    <td>13.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12191</td>
                                    <td>NDLS JBP SUP EX</td>
                                    <td>A</td>
                                    <td>13.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12203</td>
                                    <td>GARIB RATH EXP</td>
                                    <td>A</td>
                                    <td>13.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12398</td>
                                    <td>MAHABODHI EXP</td>
                                    <td>A</td>
                                    <td>13.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12419</td>
                                    <td>GOMTI EXP</td>
                                    <td>A</td>
                                    <td>14.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12566</td>
                                    <td>BIHAR S KRANTI</td>
                                    <td>A</td>
                                    <td>14.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64013</td>
                                    <td>PWL SSB EMU</td>
                                    <td>A</td>
                                    <td>14.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12057</td>
                                    <td>UHL JANSHATABDI</td>
                                    <td>A</td>
                                    <td>14.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12460</td>
                                    <td>ASR NDLS EXP</td>
                                    <td>A</td>
                                    <td>14.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14681</td>
                                    <td>NDLS JUC EXPRES</td>
                                    <td>A</td>
                                    <td>14.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12483</td>
                                    <td>AMRITSAR EXP</td>
                                    <td>A</td>
                                    <td>14.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>51901</td>
                                    <td>AGC DLI PASS</td>
                                    <td>A</td>
                                    <td>15.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12055</td>
                                    <td>DDN JANSHTBDI</td>
                                    <td>A</td>
                                    <td>15.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64016</td>
                                    <td>SSB PWL EMU</td>
                                    <td>A</td>
                                    <td>15.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12034</td>
                                    <td>NDLS CNB SHT</td>
                                    <td>A</td>
                                    <td>15.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64032</td>
                                    <td>SSB GZB EMU</td>
                                    <td>A</td>
                                    <td>15.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12440</td>
                                    <td>NDLS RNC RAJDHANI</td>
                                    <td>A</td>
                                    <td>15.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64427</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>15.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12382</td>
                                    <td>POORVA EXPRESS</td>
                                    <td>A</td>
                                    <td>16.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14324</td>
                                    <td>ROK NDLS EXP</td>
                                    <td>A</td>
                                    <td>16.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64015</td>
                                    <td>PWL SSB EMU</td>
                                    <td>A</td>
                                    <td>16.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64902</td>
                                    <td>GZB KSV EMU</td>
                                    <td>A</td>
                                    <td>16.03</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64419</td>
                                    <td>NZM GZB EMU</td>
                                    <td>A</td>
                                    <td>16.08</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12013</td>
                                    <td>AMRITSAR SHTBDI</td>
                                    <td>A</td>
                                    <td>16.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12314</td>
                                    <td>SEALDAH RJDHANI</td>
                                    <td>A</td>
                                    <td>16.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12952</td>
                                    <td>MUMBAI RAJDHANI</td>
                                    <td>A</td>
                                    <td>16.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14316</td>
                                    <td>INTERCITY EXP</td>
                                    <td>A</td>
                                    <td>16.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12926</td>
                                    <td>PASCHIM EXPRESS</td>
                                    <td>A</td>
                                    <td>16.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>22926</td>
                                    <td>PASCHIM EXPRESS</td>
                                    <td>A</td>
                                    <td>16.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12306</td>
                                    <td>KOLKATA RJDHNI</td>
                                    <td>A</td>
                                    <td>16.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64080</td>
                                    <td>NDLS PWL EMU</td>
                                    <td>A</td>
                                    <td>16.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>22812</td>
                                    <td>BUBNESWR RJDHNI</td>
                                    <td>A</td>
                                    <td>16.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12005</td>
                                    <td>KALKA SHTBDI</td>
                                    <td>A</td>
                                    <td>16.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12310</td>
                                    <td>RJPB RAJDHANI</td>
                                    <td>A</td>
                                    <td>17.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12815</td>
                                    <td>NANDAN KANAN EX</td>
                                    <td>A</td>
                                    <td>17.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64017</td>
                                    <td>PWL SSB EMU</td>
                                    <td>A</td>
                                    <td>17.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64904</td>
                                    <td>GZB MTC EMU</td>
                                    <td>A</td>
                                    <td>17.07</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12394</td>
                                    <td>SAMPOORN K EXP</td>
                                    <td>A</td>
                                    <td>17.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12724</td>
                                    <td>A P EXPRESS</td>
                                    <td>A</td>
                                    <td>17.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14212</td>
                                    <td>INTERCITY EXP</td>
                                    <td>A</td>
                                    <td>17.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64110</td>
                                    <td>NDLS ALJN EMU</td>
                                    <td>A</td>
                                    <td>17.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64429</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>17.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64431</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>17.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64450</td>
                                    <td>NDLS GZB EMU</td>
                                    <td>A</td>
                                    <td>17.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64469</td>
                                    <td>NDLS PNP LADIES SPL</td>
                                    <td>A</td>
                                    <td>17.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64492</td>
                                    <td>NDLS PWL LADIES SPL</td>
                                    <td>A</td>
                                    <td>17.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54411</td>
                                    <td>RE MUT PASS</td>
                                    <td>A</td>
                                    <td>17.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64082</td>
                                    <td>NDLS PWL EMU</td>
                                    <td>A</td>
                                    <td>17.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64114</td>
                                    <td>NDLS ALJN EMU</td>
                                    <td>A</td>
                                    <td>17.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64433</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>17.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64089</td>
                                    <td>NZM HNZM EMU</td>
                                    <td>A</td>
                                    <td>17.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64441</td>
                                    <td>GZB DLI EMU</td>
                                    <td>A</td>
                                    <td>17.48</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64018</td>
                                    <td>SSB NDLS EMU</td>
                                    <td>A</td>
                                    <td>17.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54011</td>
                                    <td>TKJ RE PASS</td>
                                    <td>A</td>
                                    <td>17.58</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64471</td>
                                    <td>GZB PNP MEMU</td>
                                    <td>A</td>
                                    <td>18.08</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64906</td>
                                    <td>GZB PWL EMU</td>
                                    <td>A</td>
                                    <td>18.13</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>14085</td>
                                    <td>SIRSA EXPRESS</td>
                                    <td>A</td>
                                    <td>18.18</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12616</td>
                                    <td>G T EXPRESS</td>
                                    <td>A</td>
                                    <td>18.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54022</td>
                                    <td>TKJ BSC PASS</td>
                                    <td>A</td>
                                    <td>18.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12560</td>
                                    <td>SHIV GANGA EXP</td>
                                    <td>A</td>
                                    <td>18.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54473</td>
                                    <td>DELHI SRE PASS</td>
                                    <td>A</td>
                                    <td>18.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64461</td>
                                    <td>NZM KKDE MEMU</td>
                                    <td>A</td>
                                    <td>18.38</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64910</td>
                                    <td>SSB MTJ EMU</td>
                                    <td>A</td>
                                    <td>18.48</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>54001</td>
                                    <td>TKJ ROK PASS</td>
                                    <td>A</td>
                                    <td>18.53</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12920</td>
                                    <td>MALWA EXPRESS</td>
                                    <td>A</td>
                                    <td>19.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64418</td>
                                    <td>DLI GZB MEMU</td>
                                    <td>A</td>
                                    <td>19.03</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64061</td>
                                    <td>PWL DLI EMU</td>
                                    <td>A</td>
                                    <td>19.08</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64097</td>
                                    <td>NDLS SSB EMU</td>
                                    <td>A</td>
                                    <td>19.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64443</td>
                                    <td>GZB DLI EMU</td>
                                    <td>A</td>
                                    <td>19.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64092</td>
                                    <td>NZM HNZM EMU</td>
                                    <td>A</td>
                                    <td>19.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64098</td>
                                    <td>SSB NZM SSB EMU</td>
                                    <td>A</td>
                                    <td>19.25</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12554</td>
                                    <td>VAISHALI EXP</td>
                                    <td>A</td>
                                    <td>19.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64087</td>
                                    <td>NZM NDLS EMU</td>
                                    <td>A</td>
                                    <td>19.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12958</td>
                                    <td>ADI SJ RAJDHANI</td>
                                    <td>A</td>
                                    <td>19.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>13007</td>
                                    <td>U ABHATOOFAN EX</td>
                                    <td>A</td>
                                    <td>19.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12260</td>
                                    <td>SDAH DURONTO EX</td>
                                    <td>A</td>
                                    <td>19.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12402</td>
                                    <td>MAGADH EXPRESS</td>
                                    <td>A</td>
                                    <td>19.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64445</td>
                                    <td>GZB DLI EMU</td>
                                    <td>A</td>
                                    <td>19.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64534</td>
                                    <td>PNP GZB EMU</td>
                                    <td>A</td>
                                    <td>20.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64064</td>
                                    <td>DELHI PALWAL EMU</td>
                                    <td>A</td>
                                    <td>20.04</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12556</td>
                                    <td>GORAKDAM EXPRES</td>
                                    <td>A</td>
                                    <td>20.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>11058</td>
                                    <td>ASR DR EXPRESS</td>
                                    <td>A</td>
                                    <td>20.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12425</td>
                                    <td>JAMMU RAJDHANI</td>
                                    <td>A</td>
                                    <td>20.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12562</td>
                                    <td>SWATANTRTA S EX</td>
                                    <td>A</td>
                                    <td>20.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12445</td>
                                    <td>UTTAR S KRANTI</td>
                                    <td>A</td>
                                    <td>20.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>11077</td>
                                    <td>JHELUM EXPRESS</td>
                                    <td>A</td>
                                    <td>20.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12825</td>
                                    <td>JHRKHND S KRANT</td>
                                    <td>A</td>
                                    <td>20.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12628</td>
                                    <td>KARNATAKA EXP</td>
                                    <td>A</td>
                                    <td>20.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64034</td>
                                    <td>SSB GZB EMU</td>
                                    <td>A</td>
                                    <td>21.03</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12418</td>
                                    <td>PRAYAG RAJ EXP</td>
                                    <td>A</td>
                                    <td>21.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64084</td>
                                    <td>NDLS PWL EMU</td>
                                    <td>A</td>
                                    <td>21.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64088</td>
                                    <td>NZM NDLS EMU</td>
                                    <td>A</td>
                                    <td>21.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12137</td>
                                    <td>PUNJAB MAIL</td>
                                    <td>A</td>
                                    <td>21.15</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12472</td>
                                    <td>SWARAJ EXPRESS</td>
                                    <td>A</td>
                                    <td>21.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64113</td>
                                    <td>KRJ SSB EMU</td>
                                    <td>A</td>
                                    <td>21.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12230</td>
                                    <td>LUCKNOW MAIL</td>
                                    <td>A</td>
                                    <td>21.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12012</td>
                                    <td>KALKA SHTBDI</td>
                                    <td>A</td>
                                    <td>21.55</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12802</td>
                                    <td>PURSHOTTAM EXP</td>
                                    <td>A</td>
                                    <td>22.00</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12003</td>
                                    <td>LKO SWRAN SHTBD</td>
                                    <td>A</td>
                                    <td>22.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12038</td>
                                    <td>LDH NDLS SHTBDI</td>
                                    <td>A</td>
                                    <td>22.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12622</td>
                                    <td>TAMIL NADU EXP</td>
                                    <td>A</td>
                                    <td>22.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64073</td>
                                    <td>KSV NDLS EMU</td>
                                    <td>A</td>
                                    <td>22.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12276</td>
                                    <td>ALD DURONTO EXP</td>
                                    <td>A</td>
                                    <td>22.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12016</td>
                                    <td>AJMER SHTBDI</td>
                                    <td>A</td>
                                    <td>22.40</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12018</td>
                                    <td>DEHRADUN SHTBDI</td>
                                    <td>A</td>
                                    <td>22.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12001</td>
                                    <td>NDLS SHATABDI E</td>
                                    <td>A</td>
                                    <td>22.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12498</td>
                                    <td>SHANE PUNJAB</td>
                                    <td>A</td>
                                    <td>22.50</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12030</td>
                                    <td>SWARNA SHTBDI</td>
                                    <td>A</td>
                                    <td>23.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64036</td>
                                    <td>SSB GZB EMU</td>
                                    <td>A</td>
                                    <td>23.05</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12272</td>
                                    <td>LKO DURONTO EXP</td>
                                    <td>A</td>
                                    <td>23.10</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12486</td>
                                    <td>SGNR NED EXPRES</td>
                                    <td>A</td>
                                    <td>23.20</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12452</td>
                                    <td>SHRAM SHKTI EXP</td>
                                    <td>A</td>
                                    <td>23.30</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>04206</td>
                                    <td>NDLS LKO SPL</td>
                                    <td>A</td>
                                    <td>23.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>04202</td>
                                    <td>NDLS LKO SPL</td>
                                    <td>A</td>
                                    <td>23.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>12205</td>
                                    <td>NDLS DDN AC EXP</td>
                                    <td>A</td>
                                    <td>23.35</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64415</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>23.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64409</td>
                                    <td>GZB NDLS EMU</td>
                                    <td>A</td>
                                    <td>23.45</td>
                                    <td></td>
                                </tr>
                                <tr style="background-color:#CEF6CE">
                                    <td>64466</td>
                                    <td>PNP NDLS MEMU</td>
                                    <td>A</td>
                                    <td>23.55</td>
                                    <td></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                </td>
            </tr>
            <tr>
                <td colspan="2">
                    Platform number of the train arrival/departure are not actual</td>
            </tr>



</body>

</html>
"""
        self.setHtml(html)
        self.show()
       

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()