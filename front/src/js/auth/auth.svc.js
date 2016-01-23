app.factory('AuthSvc', function ($http, AppConst, AuthRes, $rootScope, $routeParams, NavbarSvc) {
    var service={};
    service.init=function(reload){
        NavbarSvc.init();

        service.reg=AppConst.reg;
        service.login=AppConst.login;
        service.recovery=AppConst.recovery;
    }

	service.doLogin=function(email,password){
	    AuthRes.actionLogin(email,password).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    var data=angular.copy(response.data.data);
                    AppConfig=angular.extend(AppConfig, data);
                	$rootScope.$broadcast('auth.login', data);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
            }
        );
	}
	service.doLogout=function(){
		 AuthRes.actionLogout().then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    var data={
                      "userId": false,
                      "userData": {}
                    }
                    AppConfig=angular.extend(AppConfig, data);
                    $rootScope.$broadcast('auth.logout', data);
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