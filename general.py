import os


def create_project_dir(dir_path):
    if not os.path.exists(dir_path):
        print("Creating project " + dir_path)
        os.makedirs(dir_path)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()


def append_to_file(file, data):
    with open(file, 'a') as f:
        f.write(data + '\n')
        f.close()


def delete_file_contents(file):
    with open(file, 'w'):
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(urls, file):
    delete_file_contents(file)
    for url in sorted(urls):
        append_to_file(file, url)
















