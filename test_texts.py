from options import test_options
from dataloader import data_loader
from model import create_model
from util import visualizer
from itertools import islice
import os

if __name__=='__main__':
    # get testing options
    opt = test_options.TestOptions().parse()
    # creat a dataset
    dataloader = data_loader.dataloader(opt)
    dataset_size = len(dataloader) * opt.batchSize
    print('testing images = %d' % dataset_size)
    # create a model
    model = create_model(opt)
    model.eval()
    # create a visualizer
    visualizer = visualizer.Visualizer(opt)

    for t in range(opt.ncaptions):
        for i, data in enumerate(dataloader):
            dataloader.dataset.epoch = t
            if i > opt.how_many:
                break
            model.set_input(data)
            model.test(t)
    os.system('ls '+opt.results_dir+'/*_truth.png > eval_'+opt.name+'_texts.flist')