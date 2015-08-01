
<%def name="title()">${c.main.title}</%def>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/base.css">
        <title>${self.title()}</title>
        <style>
        body {
            background-image: url("${c.main.image}");
        }
        </style>
    </head>
    <body>
        <div class="text-overlay">
            <h1>${self.title()}</h1>
            ${next.body()}
        </div>
    </body>
</html>