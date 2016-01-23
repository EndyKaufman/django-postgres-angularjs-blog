app.factory('AuthSvc', function ($http, AppConst, $rootScope, $routeParams, NavbarSvc) {
    var service={};
    service.init=function(reload){
        NavbarSvc.init();

        service.reg=AppConst.reg;
        service.login=AppConst.login;
        service.recovery=AppConst.recovery;
    }

    service.actionLogin=function(email, password){
        return $http.post(AppConst.auth.login.action, {
            email: email,
            password: password,
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionLogout=function(){
        return $http.post(AppConst.auth.logout.action,{
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

	service.doLogin=function(email,password){
	    service.actionLogin(email,password).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    var data=angular.copy(response.data.data);
                    AppConfig=angular.extend(AppConfig, data);
                	$rootScope.$broadcast('login', data);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
            }
        );
	}
	service.doLogout=function(){
		 service.actionLogout().then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    var data={
                      "userId": false,
                      "userData": {}
                    }
                    AppConfig=angular.extend(AppConfig, data);
                    $rootScope.$broadcast('logout', data);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
            }
        );
    }

    return service;
  });