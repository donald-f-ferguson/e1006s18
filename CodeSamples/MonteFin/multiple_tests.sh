#!/bin/bash
echo "About to run simulations."
./stock_main.py --ticker AAPL --trading_days 252 --trading_years 100 --bins 20 --plot_to_file Y --simulation_label command_line_test_aapl
./stock_main.py --ticker GOOG --trading_days 252 --trading_years 100 --bins 20 --plot_to_file Y --simulation_label command_line_test_goog
./stock_main.py --ticker AMZN --trading_days 252 --trading_years 100 --bins 20 --plot_to_file Y --simulation_label command_line_test_amzn

