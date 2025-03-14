<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Igre v kategoriji {{ kategorija }}</title>
</head>
<body>
<h1>Igre za kategorijo: {{kategorija}}</h1>

% if igre:
    <table border="1">
        <tr>
            <th>Ime</th>
            <th>Opis</th>
            <th>Starostna omejitev</th>
            <th>Datum izida</th>
        </tr>
        % for igra in igre:
            <tr>
                <td>{{igra["ime"]}}</td>
                <td>{{igra["opis"]}}</td>
                <td>{{igra["starostna_omejitev"]}}</td>
                <td>{{igra["datum_izida"]}}</td>
            </tr>
        % end
    </table>
% else:
    <p>Ni iger za to kategorijo.</p>
% end

    <a href="/">Nazaj na glavno stran</a>
</body>
</html>
