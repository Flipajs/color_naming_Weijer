# Python implementation of ColorNaming by J. van de Weijer

[J. van de Weijer, C. Schmid, J. Verbeek, D. Larlus Learning Color Names for Real-World Applications , IEEE Transactions in Image Processing, 2009.](http://lear.inrialpes.fr/people/vandeweijer/papers/NamingTIP09.pdf)

For more information see authors web pages [http://lear.inrialpes.fr/people/vandeweijer/color_names.html](http://lear.inrialpes.fr/people/vandeweijer/color_names.html)
## Example
```python
import color_naming
# or any other way how to load image
from scipy.misc import imread


im = imread('path/to/my/img.jpg')


# returns np.array((im.shape[0], im.shape[1]), dtype=np.uint8) with ids of one of 11 colors
out1 = color_naming.im2colors(im, out_type='color_names')

# returns np.array((im.shape[0], im.shape[1], 11), stype=np.float) with probability of each color
out2 = color_naming.im2colors(im, out_type='probability_vector)
```

## Note!
The first call of im2colors will take significantly more time as the lookup table is loaded.