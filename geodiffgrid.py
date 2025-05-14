import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cmcrameri import cm as crameri_cm
import matplotlib.cm as mpl_cm
import argparse


def get_colormap(name):
    """Try to get a colormap from cmcrameri or matplotlib."""
    # Try cmcrameri first
    if hasattr(crameri_cm, name):
        return getattr(crameri_cm, name)
    # Then try matplotlib
    try:
        return mpl_cm.get_cmap(name)
    except ValueError:
        raise ValueError(
            f"Colormap '{name}' not found in cmcrameri or matplotlib."
        )


def create_grid_plot(df, params,output_path, year, variable, unit):
    """Create a grid plot for variable differences between two locations."""
    fig, ax = plt.subplots(figsize=(16, 8))
    plt.title(
        f"{params['title']} - Year {year}\n"
        "Hourly data",
        fontsize=16
    )
    sns.heatmap(
        df,
        cmap=params["cmap"],
        vmin=params["vmin"],
        vmax=params["vmax"],
        cbar_kws={"label": f"{variable} ({unit})"},
        ax=ax
    )
    ax.set_ylabel("Month of the year", fontsize=16)
    ax.set_xlabel("Local time (hours)", fontsize=16)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Generate a grid plot of variable differences between two locations.")
    parser.add_argument("input_file", help="Path to input pivoted CSV file")
    parser.add_argument("output", help="Output file path (.png)")
    parser.add_argument("--location1", default="Location1", help="First location name (e.g., Sydney)")
    parser.add_argument("--location2", default="Location2", help="Second location name (e.g., Hauketo)")
    parser.add_argument("--title", default="Location Comparison", help="Custom title for the plot (e.g., Sydney vs. Hauketo NOx Comparison)")
    parser.add_argument("--year", type=int, default=1950, help="Year of the data (e.g., 1950)")
    parser.add_argument("--variable", default="Difference", help="Name of the variable (e.g., NOx Difference, Temperature Difference)")
    parser.add_argument("--unit", default="units", help="Unit of the variable (e.g., µg/m³, °C)")
    parser.add_argument("--vmin", default=None, help="minimum value for plotting")
    parser.add_argument("--vmax", default=None, help="maximum value for plotting")
    parser.add_argument("--cmap", default="roma_r", help="colormap")

    args = parser.parse_args()

    # Parameters
    params = {
        "location1": args.location1,
        "location2": args.location2,
        "vmin": args.vmin,
        "vmax": args.vmax,
        "cmap": get_colormap(args.cmap),
        "title": args.title
    }

    # Load data, skipping comment line
    df = pd.read_csv(args.input_file, comment="#", index_col="Month of the year")

    # Validate columns (hours 0–23)
    expected_columns = [str(h) for h in range(24)]
    if not all(col in df.columns for col in expected_columns):
        raise ValueError(f"Input CSV must have columns: {expected_columns}")

    # Validate index (month names)
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if not all(idx in month_names for idx in df.index):
        raise ValueError(f"Input CSV index must be: {month_names}")

    # Compute vmin and vmax
    if params["vmin"] == None:
        params["vmin"] = df.values.min() - 0.1
    if params["vmax"] == None:
        params["vmax"] = df.values.max() + 0.1

    # Generate grid plot
    output_path = args.output
    create_grid_plot(df, params, output_path, args.year, args.variable, args.unit)

if __name__ == '__main__':
    main()