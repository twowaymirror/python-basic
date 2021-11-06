import logging

logging.basicConfig(level=logging.INFO)

def mark_test():
    tag_list = ["first", "second", "third"]

    mark_string = " -m"

    for number, tag in enumerate(tag_list):
        if number == 0:
            mark_string += f" {tag}"
        else:
            mark_string += f" or {tag}"


    logging.info([mark_string])

if __name__ == "__main__":
    mark_test()
