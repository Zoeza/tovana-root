var moment = require('moment');
var STAR = '&#9733;';
var SCALE_METABOLIZER = ['ULTRARAPID METABOLIZER','RAPID METABOLIZER','NORMAL METABOLIZER','INTERMEDIATE METABOLIZER','POOR METABOLIZER'];
var SCALE_ACTIVITY = ['INCREASED ACTIVITY','NORMAL ACTIVITY','DECREASED ACTIVITY'];
var SCALE_RESPONSE = ['INCREASED RESPONSE','DECREASED RESPONSE'];

function addAsset (name) {
    return `{#asset ${name}}`
}
function metabolizerTable(selectedItem) {
    return scaleTable(SCALE_METABOLIZER, selectedItem);
}
function activityTable(selectedItem) {
    return scaleTable(SCALE_ACTIVITY, selectedItem);
}
function responseTable(selectedItem) {
    return scaleTable(SCALE_RESPONSE, selectedItem);
}

function scaleTable(scales, selectedItem) {
    var str='<table class="scale"><tbody>'
    for (var i=0; i<scales.length; i++) {
        if (scales[i] == selectedItem.toUpperCase())
            str+='<tr class="selected"><td><img src="{#asset /Users/macbook/software-projects/django-projects/pdfgenerator/site/public/static/tovana_health_reports/assets/TovanaHealth/Icons/ScaleTriangle.png @encoding=dataURI}" />'+scales[i]+'</td></tr>';
        else
            str+="<tr><td>"+scales[i]+"</td></tr>";
    }
    str+="</tbody></table>";
    return str;
}