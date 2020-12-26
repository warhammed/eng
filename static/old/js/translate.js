yii.t = function (message, params=null){
	if (
        typeof translationList !== 'undefined' &&
        translationList.get(message)
    ) {
		message = translationList.get(message);
    }
    if (params) {
	   return doReplace(message,params)
    }
    return message;
}

function doReplace(message, params){
    Object.keys(params).forEach(function(key)
    {
	    message = message.replace(key, params[key])
    })
    return message;
}
