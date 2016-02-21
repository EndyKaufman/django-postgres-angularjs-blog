app.factory('MessageSvc', function (AppConst, $rootScope, $modalBox, $alert) {
    var service={};

    service.list=false;

    var extVSprintF=function(message, data){
        var new_data=[]
        var new_message=message;

        if (Array.isArray(data)){
            for (var key in data){
                if (typeof data[key] !== 'object' && !Array.isArray(data[key]))
                    new_data.push(data[key]);
            }
        }
        else
        if (typeof data === 'object'){
            for (var key in data){
                if (typeof data[key] !== 'object' && !Array.isArray(data[key]))
                    new_message=new_message.replace(new RegExp('%'+key, 'ig'),data[key]);
            }
        }
        else
        if (data!=undefined)
            new_data.push(data);
        return vsprintf(new_message, new_data);
    }

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
            content: extVSprintF(message, data.values),
            theme: 'danger',
            effect: false,
            afterOk: callbackOk,
            html: true
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
            content: extVSprintF(message, data.values),
            theme: 'alert',
            effect: false,
            afterOk: callbackOk,
            html: true
        }

        $modalBox(boxOptions);
        $rootScope.$broadcast('message.alert', message, data, callbackOk);
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
            content: extVSprintF(message, data.values),
            boxType: 'confirm',
            theme: 'alert',
            effect: false,
            confirmText: 'Yes',
            cancelText: 'No',
            afterConfirm: callbackOk,
            afterCancel: callbackCancel,
            html: true
        }

        $modalBox(boxOptions);
        $rootScope.$broadcast('message.confirm', message, data, callbackOk);
    }


    service.info=function(message, data, type){
        service.alert(message, data);
/*
        if (data===undefined)
            data={values:[]};

        if (data.title===undefined)
            data.title='';
        if (data.alertType===undefined)
            data.alertType='info';
        if (data.placement===undefined)
            data.placement='top-right';

        if (service.list[message]!==undefined)
            message=service.list[message];
        $alert({
            content: extVSprintF(message, data.values),
            title: data.title,
            type: data.alertType,
            placement: data.placement,
            show: false,
            container: '.layout-content>.container'
        });*/
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