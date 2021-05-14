import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk
import os
import sqlite3
import numpy

conn = sqlite3.connect('stu3.db')
c = conn.cursor()



             
c.execute("select * from NP")

software_list = c.fetchall()




class WB_Window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="Write Blocker")
        self.set_border_width(10)
        self.set_position(gtk.WindowPosition.CENTER)
        self.set_default_size(300, 450)

        #self.outter_box = gtk.Box(gtk.Orientation.HORIZONTAL, spacing=10)
        self.outter_box = gtk.VBox(False,spacing=10)
        self.add(self.outter_box)
        
        self.software_liststore = gtk.ListStore(str, str, str)
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        tree = gtk.TreeView(self.software_liststore)
        
        #SELECTION EMITTER START#
        
	def onSelectionChanged(tree_selection) :
		(model, pathlist) = tree_selection.get_selected_rows()
		for path in pathlist :
			tree_iter = model.get_iter(path)
			value = model.get_value(tree_iter,0)
			value2 = model.get_value(tree_iter,1)
			print value
			self.entry.set_text(value)
			self.entry2.set_text(value2)
        
        tree_selection = tree.get_selection()
        tree_selection.connect("changed", onSelectionChanged)
        #SELECTION EMITTER ENDS#
        
        for i, column_title in enumerate(["User", "License Plate", ""]):
            renderer = gtk.CellRendererText()
            column = gtk.TreeViewColumn(column_title, renderer, text=i)
            tree.append_column(column)

        self.scrollable_treelist = gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.set_hexpand(True)
        self.outter_box.pack_start(self.scrollable_treelist, False, True, 0)
        self.scrollable_treelist.add(tree)
        
        
        hbox2 = gtk.Box(gtk.Orientation.HORIZONTAL)
        self.outter_box.pack_start(hbox2, False, False, 0)
        #hbox2.set_layout(gtk.CENTER)
        self.entry = gtk.Entry()
        self.entry2 = gtk.Entry()
        hbox2.add(self.entry)
        hbox2.add(self.entry2)
        
          
        

        hbox = gtk.ButtonBox.new(gtk.Orientation.HORIZONTAL)
        hbox.set_layout(gtk.ButtonBoxStyle.CENTER) 
        self.outter_box.pack_start(hbox, False, True, 0)
        

        # Add CSS "linked" class
        hbox.get_style_context().add_class("linked")
        
        button_mount = gtk.Button(label="Add")
        hbox.add(button_mount)
        
        button_ro = gtk.Button(label="Update")
        hbox.add(button_ro)
        
        button_rw = gtk.Button(label="Remove")
        hbox.add(button_rw)
        
        button_quit = gtk.Button(label="Quit",stock=gtk.STOCK_QUIT)
        button_quit.show()
        hbox.add(button_quit)
        
        


        
        
        
        

win = WB_Window()
win.connect("delete-event",gtk.main_quit)
win.show_all()
gtk.main()
