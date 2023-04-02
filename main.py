import openai
import config
import typer
from rich import print
from rich.table import Table


def main():

    # Key
    openai.api_key = config.api_key

    print("💬 [bold green]Welcome to your Smart Chat[/bold green]")
    table = Table("Commands", "Description")
    table.add_row("--exit", "Go out of the chat")
    table.add_row("--new", "Create a new chat")

    print(table)

    # Assistant context
    context = {"role": "system",
               "content": "You are the most useful and intelligent assistant in the universe. I would be glad if you could help me to solve my requests in the most accurate way"}
    messages = [context]

    while True:

        content = __prompt()

        if content == "-new":
            print("💬 [bold green]New chat[/bold green]")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                                messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green][green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\nHow can I assist you today?")

    if prompt == "-exit":
        exit = typer.confirm("Do you want finish the app execution?")
        if exit:
            print("Bye!👋")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)
