<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seznam {{ tip }}</title>
</head>
<body>
<h1>Seznam: {{tip}}</h1>
<ul>
% for element in elementi:
    % if tip == "žanri":
        <li><a href="/igre/zanr/{{element['naziv']}}">{{element['naziv']}}</a></li>
    % elif tip == "izdajatelji":
        <li><a href="/igre/izdajatelj/{{element['ime']}}">{{element['ime']}}</a></li>
    % elif tip == "konzole":
        <li><a href="/igre/konzola/{{element['ime']}}">{{element['ime']}}</a></li>
    % end
% end
</ul>
    <a href="/">Nazaj na glavno stran</a>
</body>
</html>