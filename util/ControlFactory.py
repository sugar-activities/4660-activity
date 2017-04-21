##########################Control Factory########################################
# Control Factory extracted from Abacus, an activity by Walter Bender published #
# under the GNU General Public License v3                                       #
# Copyright (c) 2010-11, Walter Bender                                          #
# http://activities.sugarlabs.org/es-ES/sugar/addon/4293                        #
#################################################################################

import gtk
from sugar.graphics.toolbutton import ToolButton

def buttonFactory(icon_name, toolbar, callback, cb_arg=None, tooltip=None,
                    accelerator=None):
    '''Factory for making toolbar buttons'''
    button = ToolButton(icon_name)
    if tooltip is not None:
        button.set_tooltip(tooltip)
    button.props.sensitive = True
    if accelerator is not None:
        button.props.accelerator = accelerator
    if cb_arg is None:
        button.connect('clicked', callback)
    else:
        button.connect('clicked', cb_arg)
    if hasattr(toolbar, 'insert'):  # the main toolbar
        toolbar.insert(button, -1)
    else:  # or a secondary toolbar
        toolbar.props.page.insert(button, -1)
    button.show()
    return button


def radioFactory(icon_name, toolbar, callback, cb_arg=None,
                          tooltip=None, group=None):
    ''' Add a radio button to a toolbar '''
    button = RadioToolButton(group=group)
    button.set_named_icon(icon_name)
    if tooltip is not None:
        button.set_tooltip(tooltip)
    if cb_arg is None:
        button.connect('clicked', callback)
    else:
        button.connect('clicked', callback, cb_arg)
    if hasattr(toolbar, 'insert'):  # the main toolbar
        toolbar.insert(button, -1)
    else:  # or a secondary toolbar
        toolbar.props.page.insert(button, -1)
    button.show()
    return button


def labelFactory(label_text, toolbar):
    ''' Factory for adding a label to a toolbar '''
    label = gtk.Label(label_text)
    label.set_line_wrap(True)
    label.show()
    toolitem = gtk.ToolItem()
    toolitem.add(label)
    toolbar.insert(toolitem, -1)
    toolitem.show()
    return label


def spinFactory(default, min, max, callback, toolbar):
    spin_adj = gtk.Adjustment(default, min, max, 1, 32, 0)
    spin = gtk.SpinButton(spin_adj, 0, 0)
    spin_id = spin.connect('value-changed', callback)
    spin.set_numeric(True)
    spin.show()
    toolitem = gtk.ToolItem()
    toolitem.add(spin)
    toolbar.insert(toolitem, -1)
    toolitem.show()
    return spin


def separatorFactory(toolbar, expand=False, visible=True):
    ''' add a separator to a toolbar '''
    separator = gtk.SeparatorToolItem()
    separator.props.draw = visible
    separator.set_expand(expand)
    toolbar.insert(separator, -1)
    separator.show()