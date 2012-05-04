#!/Library/Scala/latest/bin/scala
#scala.cgi
!#
import System._
import scala.io.Source._
println("Content-Type: text/html; charset=UTF-8\r\n\r\n")
println("<html>")
println("REQUEST_METHOD :" + getenv("REQUEST_METHOD"))
println("<br/>")
println("SCRIPT_NAME:" + getenv("SCRIPT_NAME"))
println("<br/>")
fromFile("./alphabet.txt").getLines.toList.foreach(s => println(s + "<br/>"))
fromFile("./japanese.txt", "UTF-8").getLines.toList.foreach(s => println(s + "<br/>"))
println("</html>")
