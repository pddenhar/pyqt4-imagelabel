# qt4ImageLabel
Subclass of QLabel that takes a pixmap and draws it H+V centered and at the correct aspect ratio.

## Installation
To install the latest version from pip use `sudo pip install qt4ImageLabel`

## Usage
Use an ImageLabel just like you would a normal QLabel, except initialize it with a QPixmap to be draw.
The QPixmap will be scaled to fit the ImageLabel (which will depend on your layout just like a normal
 QLabel) and drawn automatically.

```
from qt4ImageLabel import ImageLabel

... snip ...

def setupUi():
	image1 = QtGui.QPixmap()
	label = ImageLabel(self.mainWindow.centralwidget, image1)
	self.mainWindow.horizontalLayout.addWidget(label)
```

You can also use the `setPixmap` method to replace an ImageLabel's pixmap.