import numpy as np
from pkg_resources import resource_filename, Requirement
import cPickle as pickle


class ColorNaming:
    w2c = None

    def __init__(self):
        pass

    @staticmethod
    def __load_w2c_pkl():
        with open(resource_filename(__name__, "data/w2c.pkl")) as f:
            return pickle.load(f)

    @staticmethod
    def im2colors(im, out_type='color_names'):
        """
        out_type:
            'color_names': returns np.array((im.shape[0], im.shape[1]), dtype=np.uint8) with ids of one of 11 colors
            'probability_vector': returns np.array((im.shape[0], im.shape[1], 11), stype=np.float) with probability
                of each color

        NOTE: first call might take a while as the lookup table is being loaded...

        :param im:
        :param w2c:
        :param out_type:
        :return:
        """

        # color_values = {[0 0 0], [0 0 1], [.5 .4 .25], [.5 .5 .5], [0 1 0], [1 .8 0], [1 .5 1], [1 0 1], [1 0 0], [1 1 1],
        #               q  [1 1 0]};

        if ColorNaming.w2c is None:
            ColorNaming.w2c = ColorNaming.__load_w2c_pkl()

        im = np.asarray(im, dtype=np.float)

        h, w = im.shape[0], im.shape[1]

        RR = im[:,:, 0].ravel()
        GG = im[:,:, 1].ravel()
        BB = im[:,:, 2].ravel()

        index_im = np.asarray(np.floor(RR / 8)+32 * np.floor(GG / 8)+32 * 32 * np.floor(BB / 8), dtype=np.uint)

        if out_type == 'colored_image':
            pass
        elif out_type == 'probability_vector':
            out = ColorNaming.w2c[index_im].reshape((h, w, 11))
        else:
            w2cM = np.argmax(ColorNaming.w2c, axis=1)
            out = np.asarray(w2cM[index_im], dtype=np.uint8)
            out.shape = (h, w)

        return out


def __mat2pkl(path, name):
    from scipy.io import loadmat
    import cPickle as pickle

    w2c = loadmat(path+'/'+name+'.mat')['w2c']
    with open(path+'/'+name+'.pkl', 'w') as f:
        pickle.dump(w2c, f)


def im2colors(im, out_type='color_names'):
    return ColorNaming.im2colors(im, out_type)

if __name__ == '__main__':
    import cPickle as pickle
    from scipy.misc import imread

    # __mat2pkl('data', 'w2c')

    im = imread('data/car.jpg')

    # load lookup table
    with open('data/w2c.pkl') as f:
        w2c = pickle.load(f)

    import time

    time1 = time.time()
    ColorNaming.im2c(im, out_type='probability_vector')
    print time.time() - time1

    time1 = time.time()
    ColorNaming.im2c(im, out_type='probability_vector')
    print time.time() - time1

    time1 = time.time()
    ColorNaming.im2c(im, out_type='probability_vector')
    print time.time() - time1