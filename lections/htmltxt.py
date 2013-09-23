from sgmllib import SGMLParser

class html2txt(SGMLParser):
  """html2txt()
  """
  def reset(self):
    """reset() --> initialize the parser"""
    SGMLParser.reset(self)
    self.pieces = []

  def handle_data(self, text):
    """handle_data(text) --> appends the pieces to self.pieces
    handles all normal data not between brackets "<>"
    """
    self.pieces.append(text)

  def handle_entityref(self, ref):
    """called for each entity reference, e.g. for "&copy;", ref will be
"copy"
    Reconstruct the original entity reference.
    """
    if ref=='amp':
      self.pieces.append("&")

  def output(self):
    """Return processed HTML as a single string"""
    return " ".join(self.pieces)

if __name__=="__main__":
  html="""<h1>just a piece of html</h1>
          <div class="toc">
            <ul>
               <li><span class="section"><a
href="index.html#install.choosing">1.1. Which Python is right for
you?</a></span></li>
               <li><span class="section"><a href="windows.html">1.2. Python
on Windows</a></span></li>
               <li><span class="section"><a href="macosx.html">1.3. Python
on Mac OS X</a></span></li>
               <li><span class="section"><a href="macos9.html">1.4. Python
on Mac OS 9</a></span></li>
               <li><span class="section"><a href="redhat.html">1.5. Python
on RedHat Linux</a></span></li>
               <li><span class="section"><a href="debian.html">1.6. Python
on Debian GNU/Linux</a></span></li>
               <li><span class="section"><a href="source.html">1.7. Python
Installation from Source</a></span></li>
               <li><span class="section"><a href="shell.html">1.8. The
Interactive Shell</a></span></li>
               <li><span class="section"><a href="summary.html">1.9.
Summary</a></span></li>
               <li><span class="section"><a href="summary.html">1.10.
Привіт всім !!!</a></span></li>
            </ul>
         </div>
  """
  parser = html2txt()
  parser.reset()
  parser.feed(html)
  parser.close()
  print parser.output()

