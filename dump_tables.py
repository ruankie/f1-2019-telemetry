#! /usr/bin/env python3

"""This script dumps the F1 2019 telemetry tables in RST markup format."""

from f1_2019_telemetry_packets import PacketID, TeamIDs, DriverIDs, TrackIDs, NationalityIDs, SurfaceTypes, ButtonFlag, EventStringCode

def dump_table(items, labels, num_rows=None, num_cols=None):

	if num_rows is None:
		num_rows = len(items)

	if num_cols is None:
		num_cols = (len(items) + num_rows - 1) // num_rows

	labels = [str(label) for label in labels]
	items  = [tuple(str(x) for x in item) for item in items]

	# Determine column widths
	column_widths = []
	for col in range(num_cols):
		widths = (len(x) for x in labels)
		for row in range(num_rows):
			idx = num_rows * col + row
			if idx < len(items):
				widths = tuple(max(w, len(x)) for (w, x) in zip(widths, items[idx]))
		column_widths.append(widths)

	# Ready to print
	separator_line_1 = "+" + "+".join("+".join((w + 2) * "-" for w in widths) for widths in column_widths) + "+"
	separator_line_2 = "+" + "+".join("+".join((w + 2) * "=" for w in widths) for widths in column_widths) + "+"

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

	# This table is in the spec as given on the CodeMaster forum, but not in the module.
	# Note that we added the 'uint32' type which is missing from the spec.
	TypesAndDescriptions = [
		( "uint8"  , "Unsigned 8-bit integer"  ),
		( "int8"   , "Signed 8-bit integer"    ),
		( "uint16" , "Unsigned 16-bit integer" ),
		( "int16"  , "Signed 16-bit integer"   ),
		( "uint32" , "Unsigned 32-bit integer" ),
		( "float"  , "Floating point (32-bit)" ),
		( "uint64" , "Unsigned 64-bit integer" )
	]

	dump_table(TypesAndDescriptions, ["Type", "Description"], len(TypesAndDescriptions))
	print()

	PacketIDTable = [(PacketID.short_description[p], p.value, PacketID.long_description[p]) for p in PacketID]
	dump_table(PacketIDTable, ["Packet Name", "Value", "Description"])
	print()

	EventStringCodeTable = [(EventStringCode.short_description[e], e.value.decode(), EventStringCode.long_description[e]) for e in EventStringCode]
	dump_table(EventStringCodeTable, ["Event", "Code", "Description"])
	print()

	dump_table(sorted(TeamIDs.items()), ["ID", "Team"], 20)
	print()

	dump_table(sorted(DriverIDs.items()), ["ID", "Driver"], 30)
	print()

	dump_table(sorted(TrackIDs.items()), ["ID", "Track"])
	print()

	dump_table(sorted(NationalityIDs.items()), ["ID", "Nationality"], 30)
	print()

	dump_table(sorted(SurfaceTypes.items()), ["ID", "Surface"])
	print()

	ButtonFlagTable = [("0x{:04x}".format(k), v) for (k,v) in sorted((bf.value, ButtonFlag.description[bf]) for bf in ButtonFlag)]
	dump_table(ButtonFlagTable, ["Bit flags", "Button"])
	print()


if __name__ == "__main__":
    main()
