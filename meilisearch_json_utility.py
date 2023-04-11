import meilisearch
import json
import click
import subprocess


@click.command()
@click.option('--json_file', prompt='enter path to json file',
              help='upload json file to meilisearch')
@click.option('--index', prompt='enter index name',
              help='index for meilisearch')
def main(json_file, index):

    start_meilisearch = subprocess.run('./meilisearch', cwd="/home/asante/")

    if start_meilisearch.returncode == 0:

        client = meilisearch.Client('http://localhost:7700')

        opened_json_file = open(json_file)
        json_content = json.load(opened_json_file)
        client.index(index).add_documents(json_content)
        client.get_indexes({'limit': 3})

    else:
        print("you must install meilisearch")


if __name__ == '__main__':
    main()
