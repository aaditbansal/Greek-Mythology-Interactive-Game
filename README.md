# Greek-Mythology-Interactive-Game

An AI-based website where you can interact with characters from popular Greek myths.

Keep in mind while using, it may actually take a while for the responses to generate. When you first open it, there'll be a blank screen. Wait for the text to automatically generate. Then type in your prompt, click Submit/Enter, and wait for the text to pop up on the screen again.

Keep something else in mind: some of the characters may not be ready in the backend. If that is the case, the AI chooses a random character from Greek Mythology (bias towards Gods/Famous Heroes), and behaves like that character.

\*as of the current version, the myths of Atalanta, Achilles, Odysseus, and Jason are incomplete, and Heracles will generate random characters

This is currently developer-based and can therefore only be used on localhost. Follow the installation instructions below to download and use:

1. Clone/Download the repository onto your laptop. You can download by selecting the green 'Code' dropdown button and selecting download ZIP.

2. Open the folder Greek-Mythology-Interactive-Game in VS Code

3. Right click on '.env.example', and rename '.env.example' to '.env'

4. Generate an API Key from OpenAI API. Signing up is required, and you can find it at this page: https://platform.openai.com/api-keys

5. Copy this API Key and paste it in .env in the same line as OPENAI_API_KEY =

6. It may be necessary to add $5 in credit to use the API. This can be done here: https://platform.openai.com/settings/organization/billing/overview. Make sure auto-recharge is off, you will not need more than the minimum amount (unless you absolutely grind for some reason)

7. Click 'Terminal' at the top of VS Code and select 'New Terminal'. Do this a second time so that you have two terminals.

8. Run all the following commands into either terminal: `pip install openai`, `pip install python-dotenv`, `pip install flask`, `pip install flask-cors`

9. Type `cd src` in both terminals

10. In the first terminal, run `python3 app.py` and in the second terminal, run `python3 -m http.server 8000`

11. Type into your browser (Chrome works well on Windows, not sure about others): `http://localhost:8000/src/`

12. Welcome to my Greek Mythology Interactive Game!
