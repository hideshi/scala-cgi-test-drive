#!/Library/Scala/latest/bin/scala
#scalaview.cgi
!#
import System._
import java.net.URLDecoder
import cgilib.CGI
val params = CGI.params(getenv("QUERY_STRING"))
println("Content-Type: text/html; charset=UTF-8\r\n\r\n")
val html1 =
"""
<html>
	<head>
		<title>テストページ</title>
	</head>
	<body>
"""
val html2 =
"""
	</body>
</html>
"""
println(html1)
for(param <- params) {
	param match {
		case (k, v) => println(k + " : " + URLDecoder.decode(v) + "<br/>")
	}
}
println(html2)
