def scan_image(image):
    with open(image, "rb") as file:
        data = file.read()

        # Danh sách các loại marker
        markers = [b"\xFF\xD8\xFF\xE0"] # [b"\xFF\xDB\x00\x84", b"\xFF\xDB\x00\x43"]
        end_marker = b"\xFF\xD9"
        count = 0

        for marker in markers:
            start_offset = data.find(marker)

            while start_offset != -1:
                end_offset = data.find(end_marker, start_offset)
                if end_offset != -1:

                    # print(f"{str(start_offset)}x{str(end_offset)}")
                    count += 1
                    #Save
                    with open(f"./IMG/IMG_{count}.JPG", "wb") as w:
                        w.write(data[start_offset:end_offset + 2])

                    start_offset = data.find(marker, end_offset)
                else:
                    break