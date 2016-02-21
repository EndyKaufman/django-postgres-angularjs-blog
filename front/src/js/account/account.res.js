app.factory('AccountRes', function ($http, AppConst) {
    var service={};

    service.actionLogin=function(email, password){
        return $http.post('/account/login', {
            email: email,
            password: password,
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionLogout=function(){
        return $http.post('/account/logout',{
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionReg=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post('/account/reg', item);
    }

    service.actionRecovery=function(email){
        var item={email:email};
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post('/account/recovery', item);
    }

    service.actionResetpassword=function(code, password){
        return $http.post('/account/resetpassword', {
            code: code,
            password: password,
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionDelete=function(){
        return $http.post('/account/delete',{
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    }

    service.actionUpdate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post('/account/update', item);
    }

    return service;
  });