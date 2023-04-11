import meilisearch
import json
import click


@click.command()
@click.option('--json_file', prompt='enter path to json file',
              help='upload json file to meilisearch')
@click.option('--index', prompt='enter index name',
              help='index for meilisearch')
def main(json_file, index):

    client = meilisearch.Client('http://localhost:7700')
    opened_json_file = open(json_file)
    json_content = json.load(opened_json_file)
    client.index(index).add_documents(json_content)
    client.get_indexes({'limit': 3})


if __name__ == '__main__':
    main()
