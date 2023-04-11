import meilisearch
import json
import click
import subprocess


@click.command()
@click.option('--json', prompt='enter path to json file',  help='upload json file to meilisearch')
@click.option('--index', prompt='enter index name',help='index for meilisearch')

def main(json, index_name):

    start_meilisearch = subprocess.run(["cd ~ && ./meilisearch"], check=True)

    if start_meilisearch.returncode == 0:

        client = meilisearch.Client('http://localhost:7700')

        json_file = open(json)
        json_content = json.load(json_file)
        client.index(index).add_documents(json_content)

    else:
        print("you must install meilisearch")


if __name__ == '__main__':
    main()