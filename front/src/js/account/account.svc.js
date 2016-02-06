app.factory('AccountSvc', function ($q, $http, AppConst, AccountRes, MessageSvc, $rootScope, $routeParams, NavbarSvc) {
    var service={};

    $rootScope.$on('account.update',function(event, data){
        MessageSvc.info('account/update/success');
    });

    $rootScope.$on('account.login',function(event, data){
        MessageSvc.info('account/login/success');
        NavbarSvc.init();
        NavbarSvc.goBack();
    });

    $rootScope.$on('account.logout',function(event, data){
        MessageSvc.info('account/logout/success');
        NavbarSvc.init();
        NavbarSvc.goHome();
    });

    $rootScope.$on('navbar.change',function(event, eventRoute, current, previous){
        if (current.params!=undefined && current.params.navId=='logout'){
            if (eventRoute!=false)
                eventRoute.preventDefault();
            service.doLogout();
        }
    });

    service.init=function(reload){
        NavbarSvc.init($routeParams.navId);
        if ($routeParams.navId=='logout'){
            service.doLogout();
            return;
        }
        $q.all([
            service.load()
        ]).then(function(responseList) {

        });
    }


    service.load=function(){
        var deferred = $q.defer();
        service.item=AppConfig.user;
        deferred.resolve(service.item);
        return deferred.promise;
    }

	service.doUpdate=function(item){
	    $rootScope.$broadcast('show-errors-check-validity');
		 AccountRes.actionUpdate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=angular.copy(response.data.data[0]);
                    AppConfig.user=service.item;
                    $rootScope.$broadcast('account.update', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
    }

	service.doLogin=function(email, password){
	    AccountRes.actionLogin(email,password).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=angular.copy(response.data.data[0]);
                    AppConfig.user=service.item;
                	$rootScope.$broadcast('account.login', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
	}
	service.doLogout=function(){
         MessageSvc.confirm('account/logout/confirm', {},
         function(){
             AccountRes.actionLogout().then(
                function (response) {
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                        service.item={}
                        AppConfig.user=service.item;
                        $rootScope.$broadcast('account.logout', service.item);
                    }
                },
                function (response) {
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                        MessageSvc.error(response.data.code, response.data);
                }
            );
        },
        function(){
            if ($routeParams.navId=='logout')
                NavbarSvc.goHome();
        });
    }

    service.isLogged=function(){
        return AppConfig.user.id!=undefined;
    }

    service.isAdmin=function(){
        return AppConfig.user!=undefined && AppConfig.user.roles!=undefined && AppConfig.user.roles.indexOf('admin')!=-1
    }

    service.isAuthor=function(){
        return AppConfig.user!=undefined && AppConfig.user.roles!=undefined && AppConfig.user.roles.indexOf('author')!=-1
    }

    service.isUser=function(){
        return AppConfig.user!=undefined && AppConfig.user.roles!=undefined && AppConfig.user.roles.indexOf('user')!=-1
    }

    return service;
  });