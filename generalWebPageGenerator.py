import linecache, pyperclip

columnName = 'Creative Thinking'
description = 'Creative strategies to train your thinking'
current1 = ' class="current"'
current2 = ''
current3 = ''
current4 = ''

"""
columnName = 'Critical Thinking'
description = 'Logical Fallacies that you should avoid in your writing'
current1 = ''
current2 = ' class="current"'
current3 = ''
current4 = ''
"""

"""
columnName = 'The List of Works Cited'
description = 'Cited The List of Works Cited correctly in literature papers'
current1 = ''
current2 = ''
current3 = ' class="current"'
current4 = ''
"""

"""
columnName = 'In-Text Citations'
description = 'Cited In-Text Citations correctly in literature papers'
current1 = ''
current2 = ''
current3 = ' class="current"'
current4 = ''
"""

"""
columnName = 'Experimental Tools'
description = 'Applications that can train your creativity and help you write more easily'
current1 = ''
current2 = ''
current3 = ''
current4 = ' class="current"'
"""

################
frontData = """<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>{columnName} - thinkWrite (beta)</title>
<meta name="description" content="{description} on the Online English Writing Lab of Beijing Foreign Studies University.">
<link href="styles/main.css" rel="stylesheet">
<link href="styles/switch.css" rel="stylesheet">
</head>
<body>

<header>
    <h1>thinkWrite (beta)</h1>
</header>

<nav>
    <a href="index.html">Home</a> &nbsp;
    <a href="Creative Thinking.html"{current1}>Creative Thinking</a> &nbsp;
    <a href="Critical Thinking.html"{current2}>Critical Thinking</a> &nbsp;
    <a href="MLA Style Guide.html"{current3}>MLA Style Guide</a> &nbsp;
    <a href="Experimental Tools.html"{current4}>Experimental Tools</a>
</nav>



<showDetails>
show details<br>
<button class="showhideAndViewWithSwitch switch switchOn"></button>
</showDetails>
"""

frontData = frontData.format(columnName=columnName, description=description, current1=current1, current2=current2, current3=current3, current4=current4)
frontData

endData = """<footer>
Copyright &copy; 2018-2019 thinkWrite (beta) for academic use only
</footer>


<!-- BEGIN JAVASCRIPTS(Load javascripts at bottom, this will reduce page loading time) -->
<!-- BEGIN CORE PLUGINS -->   
<script src="styles/jquery.min.js" type="text/javascript"></script>
<script>
$(".showhideAndViewWithSwitch").on("click",function(){
var smBtn = $(this);
if(smBtn.hasClass("switchOn")){
smBtn.removeClass("switchOn");
$(".hideAndViewWithSwitch").hide();
initMasonry();
}else{
smBtn.addClass("switchOn");
$(".hideAndViewWithSwitch").show();
initMasonry();
}
});
</script>

</body>
</html>"""

"""item sample
<div>
    <h3>What Is Creative Thinking?</h3>

    <dl>
        <dt><strong>What creative thinking is</strong></dt>
        <dd><div class="hideAndViewWithSwitch" style="display: block">Creativity is the ability to suspend judgment, discover new links between familiar things, look at problems or issues from new perspectives, and form new combinations from concepts already in the mind.</div></dd>
    </dl>

    <citation><div class="hideAndViewWithSwitch" style="display: block">Zhang (Unit 1 - Page 2, Book 1)</div></citation>
</div>
"""

################
# Read .txt file.
fo = open('%s.bfsu' % columnName, 'r', encoding='UTF=8')
divList = fo.read()
fo.close()
divList = divList.split('---\n')
divList[-1] = divList[-1] + '\n'

middleData = ''
for div in divList:
    div = div[:-2]
    itemList = div.split('\n')

    # Count the number of lines.
    LINE_COUNT = len(itemList)

    # Formatting.
    for i in range(2, LINE_COUNT, 2):
        itemList[i] = '        <dt><strong>' + itemList[i] + '</strong></dt>'

    for i in range(3, LINE_COUNT, 2):
        itemList[i] = '        <dd><div class="hideAndViewWithSwitch" style="display: block">' + itemList[i] + '</div></dd>'

    frontString = '<div>\n    <h3>' + itemList[0] + '</h3>\n\n    <dl>\n'
    endString = '\n    <dl>\n\n    <citation><div class="hideAndViewWithSwitch" style="display: block">' + itemList[1] + '\n</div></citation>\n'
    middleData += frontString + '\n'.join(itemList[2:]) + endString


# Write to .html file.
data = frontData + middleData + endData
fo = open('%s.html' % columnName, 'w', encoding='UTF=8')
fo.write(data)
fo.close()

print('Done.')