var speech_to_text = require('watson-developer-cloud/speech-to-text/v1')
const fs = require('fs')

const speech2Text = new speech_to_text({
    iam_apikey: 'OcmOFrlXavEQezn-UI9oI8o8mqnPdfP8eozevkLmIXvK',
    iam_apikey_name: 'auto-generated-apikey-322db84f-429f-443e-8f8a-74a2277c25c8',
    url: 'https://stream.watsonplatform.net/speech-to-text/api'

});



const parametros = {
    audio: fs.createReadStream('audio.mp3'),
    content_type: 'audio/mp3',
    word_alternatives_threshold: 0.9
}
function fala(speech2Text,parametros){
    var imprimir;
    speech2Text.recognize(parametros, function(err, res){
        var imprimir1;
        if(err){
            console.log(err)
        }else{
            imprimir1 = (res.results[0].alternatives[0].transcript)
            imprimir = (res.results[0].alternatives[0].transcript)
            console.log(imprimir1)

            fs.writeFile('conversao.txt',imprimir, (err)=>{
                if(err) throw err;

            })
            console.log(imprimir)
            
                
        }
        
    }); 
   
   
}
 
fala(speech2Text,parametros)
 






