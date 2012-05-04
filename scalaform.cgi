#!/Library/Scala/latest/bin/scala
#scalaform.cgi
!#
import System._
println("Content-Type: text/html; charset=UTF-8\r\n\r\n")
val html =
"""
<html>
	<head>
		<title>テストページ</title>
	</head>
	<body>
		<form method="GET" action="scalaview.cgi">
			<label>入力フォーム</label><br/>
			<input type="text" name="input_text1"/><br/>
			<input type="text" name="input_text2"/><br/>
			<input type="submit"/>
		</form>
	</body>
</html>
"""
println(html)
