#! /usr/bin/env python3

from f1_2019_telemetry_packets import TeamIDs, DriverIDs, TrackIDs, NationalityIDs, SurfaceTypes, ButtonFlags, ButtonFlagsDescription

def dump_table(items, labels, num_rows, num_cols=None):

	if num_cols is None:
		num_cols = (len(items) + num_rows - 1) // num_rows

	labels = [str(label) for label in labels]
	items = [(str(k), str(v)) for (k, v) in items]

	# determine column widths
	column_widths = []
	for col in range(num_cols):
		width_k_column = len(labels[0])
		width_v_column = len(labels[1])
		for row in range(num_rows):
			idx = num_rows * col + row
			if idx < len(items):
				width_k_column = max(width_k_column, len(items[idx][0]))
				width_v_column = max(width_v_column, len(items[idx][1]))
		column_widths.append((width_k_column, width_v_column))

	# Ready to print
	separator_line_1 = "+" + "+".join((wk + 2) * "-" + "+" + (wv + 2) *  "-"  for (wk, wv) in column_widths) + "+"
	separator_line_2 = "+" + "+".join((wk + 2) * "=" + "+" + (wv + 2) *  "="  for (wk, wv) in column_widths) + "+"

	print(separator_line_1)

	print("|", end='')
	for (col, widths) in enumerate(column_widths):
		for (label, width) in zip(labels, widths):
			print(" " + label + (width - len(label) + 1) * " ", end='')
			print("|", end='')
	print()

	print(separator_line_2)

	for row in range(num_rows):

		print("|", end='')
		for (col, widths) in enumerate(column_widths):
			idx = num_rows * col + row
			values = items[idx] if idx < len(items) else ("", "")
			for (value, width) in zip(values, widths):
				print(" " + value + (width - len(value) + 1) * " ", end='')
				print("|", end='')
		print()

		print(separator_line_1)

def main():

	TypesAndDescriptions = [
		( "uint8"  , "Unsigned 8-bit integer"  ),
		( "int8"   , "Signed 8-bit integer"    ),
		( "uint16" , "Unsigned 16-bit integer" ),
		( "int16"  , "Signed 16-bit integer"   ),
		( "float"  , "Floating point (32-bit)" ),
		( "uint64" , "Unsigned 64-bit integer" )
	]

	dump_table(TypesAndDescriptions, ["Type", "Description"], len(TypesAndDescriptions))
	print()

	if False:
		dump_table(sorted(TeamIDs.items()), ["ID", "Team"], 20)
		print()
		dump_table(sorted(DriverIDs.items()), ["ID", "Driver"], 30)
		print()
		dump_table(sorted(TrackIDs.items()), ["ID", "Track"], 25)
		print()
		dump_table(sorted(NationalityIDs.items()), ["ID", "Nationality"], 30)
		print()
		dump_table(sorted(SurfaceTypes.items()), ["ID", "Surface"], 12)
		print()

		ButtonFlagsTableEntries = [("0x{:04x}".format(k), v) for (k,v) in sorted((bf.value, ButtonFlagsDescription[bf]) for bf in ButtonFlags)]
		dump_table(ButtonFlagsTableEntries, ["Bit flags", "Button"], len(ButtonFlagsTableEntries))
		print()

if __name__ == "__main__":
    main()
