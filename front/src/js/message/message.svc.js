app.factory('MessageSvc', function (AppConst, $rootScope, $modalBox, $alert) {
    var service={};

    service.list=false;

    service.error=function(message, data, callbackOk){
        if (data===undefined)
            data={values:[]};

        if (data.title===undefined)
            data.title='Error';

        if (callbackOk===undefined)
            callbackOk=function(){
            }
        if (service.list[message]!==undefined)
            message=service.list[message];

        var boxOptions = {
            title: data.title,
            content: vsprintf(message, data.values),
            theme: 'danger',
            effect: false,
            afterOk: callbackOk
        }

        $modalBox(boxOptions);
        $rootScope.$broadcast('message.error', message, data, callbackOk);
    }

    service.alert=function(message, data, callbackOk){
        if (data===undefined)
            data={values:[]};

        if (data.title===undefined)
            data.title='Info';

        if (callbackOk===undefined)
            callbackOk=function(){
            }
        if (service.list[message]!==undefined)
            message=service.list[message];

        var boxOptions = {
            title: data.title,
            content: vsprintf(message, data.values),
            theme: 'alert',
            effect: false,
            afterOk: callbackOk
        }

        $modalBox(boxOptions);
        $rootScope.$broadcast('message.info', message, data, callbackOk);
    }

    service.confirm=function(message, data, callbackOk, callbackCancel){
        if (data===undefined)
            data={values:[]};

        if (data.title===undefined)
            data.title='Message';

        if (callbackOk===undefined)
            callbackOk=function(){
            }
        if (callbackCancel===undefined)
            callbackCancel=function(){
            }
        if (service.list[message]!==undefined)
            message=service.list[message];

        var boxOptions = {
            title: data.title,
            content: vsprintf(message, data.values),
            boxType: 'confirm',
            theme: 'alert',
            effect: false,
            confirmText: 'Yes',
            cancelText: 'No',
            afterConfirm: callbackOk,
            afterCancel: callbackCancel
        }

        $modalBox(boxOptions);
        $rootScope.$broadcast('message.alert', message, data, callbackOk);
    }


    service.info=function(message, data, type){
        if (data===undefined)
            data={values:[]};

        if (data.title===undefined)
            data.title='';
        if (data.alertType===undefined)
            data.alertType='info';
        if (data.placement===undefined)
            data.placement='center';

        if (service.list[message]!==undefined)
            message=service.list[message];

        $alert(vsprintf(message, data.values), data.title, data.alertType, data.placement)
    }

    service.init=function(){
        service.list={};
        for (var key in AppConst){
            if (AppConst[key]['message']!==undefined){
                angular.extend(service.list, AppConst[key]['message']);
            }
        }
    }

    if (service.list===false)
        service.init();

    return service;
  });