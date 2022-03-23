def read_file(file_path):
    with open(file_path) as f:
        data = [line.strip() for line in f.readlines()]

    return data

def convert_units(data):
    all_trees = []
    for d in data[1:]:
        index, girth_in, height_ft, volume_ft3 = d.split(',')
        
        index = int(index)
        girth_cm = round(float(girth_in) * 0.0254, 3)
        height_m = int(height_ft) * 0.3048
        volume_l = round(float(volume_ft3) * 0.028, 3)

        all_trees.append([index, girth_cm, height_m, volume_l])

    return all_trees

def get_biggest_trees(trees):
    max_girth = max(trees, key=lambda tree: tree[1])
    max_height = max(trees, key=lambda tree: tree[2])
    max_volume = max(trees, key=lambda tree: tree[3])
    return ['Tree number {0} has the largest girth. Girth: {1}m'.format(*max_girth), 'Tree number {0} has the largest height. Height: {2}m'.format(*max_height), 'Tree number {0} has the largest volume. Volume: {3}m\u00B3'.format(*max_volume)]

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        sentence = '\n'.join(content)
        f.write(sentence)