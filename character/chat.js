const CharacterAI = require('node_characterai');

const WebSocket = require('ws')


const port = 40102

const wss = new WebSocket.Server({ port: port });


wss.on('connection', (ws) => {
    console.log('A client connected');
    // ws.send('Connected to Kirua Kinagi!')

    ws.on('error', console.error);

    ws.on('message', async function (message) {
        let chatMessage = message.toString('utf8');
        let response = await sendMessage(chatMessage)
        ws.send(response);
    });

});

var chat = '';

setConnection = async () => {
    try{
        var characterAI = new CharacterAI();
        await characterAI.authenticateAsGuest();
        var characterId = "RBBe-dNXx-2DxcllP4XYw4d48xVrquRUCVwYRYLTO4c" // Discord moderator
        chat = await characterAI.createOrContinueChat(characterId);
        console.log("Kirua Kinagi is Running!")
    }catch(err){
        console.log(err);
        console.log("waiting 5 second to connect server")
        await sleep(5 * 1000);
        await setConnection();
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

sendMessage = async(message) => {
    var result = {text: "Maaf, saya tidak paham. bisa ulangi lagi?"};
    try{
        console.log(`Received message: ${message}`);
        result = await chat.sendAndAwaitResponse(message, true);
        console.log(`Response message: ${result.text}`);

    }catch(err){
        console.log(err);
        await setConnection();
    }
    return result.text;
}


(async() => {
    await setConnection();
    // const characterId = "8_1NyR8w1dOXmI1uWaieQcd147hecbdIK7CeEAIrdJw" // Discord moderator
    
    // await sendMessage('Hello Kirua Kinagi!')
    // await sendMessage('siapa namamu?')
    
    // use response.text to use it in a string.
})();