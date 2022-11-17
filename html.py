template = """<!DOCTYPE html>
<html lang = "en">
<head>
    <title> Office Hour </title>
    <meta HTTP-EQUIV = "CACHE-CONTROL" CONTENT = "NO-CACHE">
    <meta HTTP-EQUIV = "PRAGMA" CONTENT = "NO-CACHE">
    <meta charset = "utf-8">
    <meta name = "viewport" content = "width=device-width, initial-scale=1">
    <link rel = "stylesheet" href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"> </script>
    <script src = "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"> </script>
</head>
<body>
   <div class="container-fluid p-0">
       <div class="row no-gutters">
           <div class="col-xs-12">
            </div>
        </div>
    </div>
    <div class="container-fluid">
       <div class="row">
            <div class ="col-sm-4" style="height:800px">
                <iframe src="{0}" width=100% height=100% frameborder="0" marginheight="0"
                    marginwidth = "0"> Loading…</iframe>
            </div>
            <div class = "col-sm-8" style="height:800px; padding-top:16px;">
              <iframe name = "testFrame"
                 src = "https://docs.google.com/spreadsheets/d/{1}/htmlembed/sheet?gid={2}&amp;single=true&amp;widget=true&amp;headers=false"
                    width=100% height=100%></iframe>
            </div>
        </div>
        <script>
         window.setInterval("reloadIFrame();", 3000)
          function reloadIFrame() {{
               document.getElementsByName("testFrame")[0].src="https://docs.google.com/spreadsheets/d/{1}/htmlembed/sheet?gid={2}&amp;single=true&amp;widget=true&amp;headers=false"
               }}
        </script>
</body>
</html>"""
