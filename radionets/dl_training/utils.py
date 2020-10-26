import sys
import click
from pathlib import Path
from dl_framework.data import load_data, DataBunch, get_dls
import dl_framework.architecture as architecture
from dl_framework.inspection import plot_loss
from dl_framework.model import save_model
from dl_framework.inspection import create_inspection_plots


def create_databunch(data_path, fourier, source_list, batch_size):
    # Load data sets
    train_ds = load_data(data_path, "train", source_list=source_list, fourier=fourier)
    valid_ds = load_data(data_path, "valid", source_list=source_list, fourier=fourier)

    # Create databunch with defined batchsize
    bs = batch_size
    data = DataBunch(*get_dls(train_ds, valid_ds, bs))
    return data


def read_config(config):
    train_conf = {}
    train_conf["data_path"] = config["paths"]["data_path"]
    train_conf["model_path"] = config["paths"]["model_path"]
    train_conf["pre_model"] = config["paths"]["pre_model"]
    train_conf["norm_path"] = config["paths"]["norm_path"]

    train_conf["batch_mode"] = config["mode"]["batch_mode"]
    train_conf["telegram_logger"] = config["mode"]["telegram_logger"]

    train_conf["bs"] = config["hypers"]["batch_size"]
    train_conf["lr"] = config["hypers"]["lr"]

    train_conf["fourier"] = config["general"]["fourier"]
    train_conf["arch_name"] = config["general"]["arch_name"]
    train_conf["loss_func"] = config["general"]["loss_func"]
    train_conf["num_epochs"] = config["general"]["num_epochs"]
    train_conf["inspection"] = config["general"]["inspection"]

    train_conf["param_scheduling"] = config["param_scheduling"]["use"]
    train_conf["lr_start"] = config["param_scheduling"]["lr_start"]
    train_conf["lr_max"] = config["param_scheduling"]["lr_max"]
    train_conf["lr_stop"] = config["param_scheduling"]["lr_stop"]

    train_conf["source_list"] = config["general"]["source_list"]
    return train_conf


def check_outpath(model_path, train_conf):
    path = Path(model_path)
    exists = path.exists()
    if exists:
        if train_conf["batch_mode"]:
            click.echo("Overwriting existing model file!")
            path.unlink()
        else:
            if click.confirm(
                "Do you really want to overwrite existing model file?", abort=False
            ):
                click.echo("Overwriting existing model file!")
                path.unlink()

    return None


def define_arch(arch_name, img_size):
    if (
        arch_name == "filter_deep"
        or arch_name == "filter_deep_amp"
        or arch_name == "filter_deep_phase"
    ):
        arch = getattr(architecture, arch_name)(img_size)
    else:
        arch = getattr(architecture, arch_name)()
    return arch


def pop_interrupt(learn, train_conf):
    if click.confirm("KeyboardInterrupt, do you want to save the model?", abort=False):
        model_path = train_conf["model_path"]
        # save model
        print("Saving the model after epoch {}".format(learn.epoch))
        save_model(learn, model_path)

        # plot loss
        plot_loss(learn, model_path)

        # Plot input, prediction and true image if asked
        if train_conf["inspection"]:
            create_inspection_plots(learn, train_conf)
    else:
        print("Stopping after epoch {}".format(learn.epoch))
    sys.exit(1)


def end_training(learn, train_conf):
    # Save model
    save_model(learn, Path(train_conf["model_path"]))

    # Plot loss
    plot_loss(learn, Path(train_conf["model_path"]))