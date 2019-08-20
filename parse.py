#!/usr/bin/python

import xml.sax

class WikiHandler(xml.sax.ContentHandler):
   def __init__(self):
      self.CurrentData = ""
      self.page = ""
      self.title = ""
      self.ns = ""
      self.id = ""
      self.redirect = ""
      self.format = ""
      self.text = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "page":
        pass

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "title":
         print("Title", self.title)
     # elif self.CurrentData == "ns":
     #    self.ns = ns
     # elif self.CurrentData == "id":
     #    self.id = id
     # elif self.CurrentData == "redirect":
     #    self.redirect = redirect
     # elif self.CurrentData == "format":
     #    self.format = format
      elif self.CurrentData == "text":
          print("Text: ", self.text)
      self.CurrentData = ""


   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "ns":
         self.ns = content
      elif self.CurrentData == "id":
         self.id = content
      elif self.CurrentData == "redirect":
         self.redirect = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "text":
         self.text = content

if ( __name__ == "__main__"):

   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )

   parser.parse("movies.xml")
