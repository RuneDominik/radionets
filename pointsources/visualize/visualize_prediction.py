import click
import pandas as pd
from mnist_cnn.visualize.utils import eval_model
from mnist_cnn.utils import get_h5_data
import matplotlib.pyplot as plt
import torch
from mpl_toolkits.axes_grid1 import make_axes_locatable
import dl_framework.architectures as architecture
from dl_framework.model import load_pre_model
from dl_framework.data import do_normalisation
from mnist_cnn.utils import split_real_imag, combine_and_swap_axes


@click.command()
@click.argument('arch', type=str)
@click.argument('pretrained_path', type=click.Path(exists=True, dir_okay=True))
@click.argument('in_path', type=click.Path(exists=False, dir_okay=True))
@click.argument('norm_path', type=click.Path(exists=False, dir_okay=True))
@click.argument('out_path', type=click.Path(exists=False, dir_okay=True))
@click.option('-index', type=int, required=False)
@click.option('-log', type=bool, required=False)
def main(arch, pretrained_path, in_path, norm_path,
         out_path, index=None, log=False):
    i = index
    x_valid, y_valid = get_h5_data(in_path, columns=['x_valid', 'y_valid'])
    
    img = torch.tensor(x_valid[i])
    if log is True:
        img = torch.log(img)
    img_reshaped = img.view(1, 1, 64, 64)
    norm = pd.read_csv(norm_path)
    img_normed = do_normalisation(img_reshaped, norm)

    # get arch
    arch = getattr(architecture, arch)()

    # load pretrained model
    load_pre_model(arch, pretrained_path)

    # predict image
    prediction = eval_model(img_normed, arch)

    # print(prediction)
    # print(prediction.shape)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))

    inp = img_normed.numpy()

    inp_real = inp[0, 0, :]
    im1 = ax1.imshow(inp_real)
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im1, cax=cax, orientation='vertical')

    inp_imag = inp[0, 0, :]
    im2 = ax2.imshow(inp_imag, cmap='RdBu', vmin=-inp_imag.max(),
                     vmax=inp_imag.max())
    divider = make_axes_locatable(ax2)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im2, cax=cax, orientation='vertical')

    pred_img = prediction.reshape(64, 64).numpy()
    im3 = ax3.imshow(pred_img)
    divider = make_axes_locatable(ax3)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im3, cax=cax, orientation='vertical')

    im4 = ax4.imshow(y_valid[i].reshape(64, 64))
    divider = make_axes_locatable(ax4)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im4, cax=cax, orientation='vertical')

    plt.savefig(str(out_path), bbox_inches='tight', pad_inches=0.01)


if __name__ == '__main__':
    main()
