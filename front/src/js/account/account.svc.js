app.factory('AccountSvc', function ($q, $http, $location, AppConst, AccountRes, MessageSvc, $rootScope, $routeParams, NavbarSvc) {
    var service={};

    $rootScope.$on('account.update',function(event, data){
        MessageSvc.info('account/update/success');
        AppConfig.user=service.item;
    });

    $rootScope.$on('account.create',function(event, data){
        MessageSvc.info('account/create/success');
        AppConfig.user=service.item;
        NavbarSvc.init();
        NavbarSvc.goBack();
    });

    $rootScope.$on('account.login',function(event, data){
        MessageSvc.info('account/login/success');
        AppConfig.user=service.item;
        NavbarSvc.init();
        NavbarSvc.goHome();
    });

    $rootScope.$on('account.logout',function(event, data){
        MessageSvc.info('account/logout/success');
        AppConfig.user=service.item;
        NavbarSvc.init();
        NavbarSvc.goHome();
    });

    $rootScope.$on('account.delete',function(event, data){
        MessageSvc.info('account/delete/success');
        AppConfig.user=service.item;
        NavbarSvc.init();
        NavbarSvc.goHome();
    });

    $rootScope.$on('account.recovery',function(event, data){
        service.goResetpassword();
        MessageSvc.info('account/recovery/checkemail', {values:[data.email]});
    });

    $rootScope.$on('navbar.change',function(event, eventRoute, current, previous){
        if (current.params!=undefined && current.params.navId=='logout'){
            if (eventRoute!=false)
                eventRoute.preventDefault();
            service.doLogout();
        }
    });

    service.goResetpassword=function(){
        $location.path('/resetpassword');
    }
    service.init=function(reload){
        NavbarSvc.init($routeParams.navId);
        if (($routeParams.navId=='login' || $routeParams.navId=='reg' || $routeParams.navId=='resetpassword' || $routeParams.navId=='recovery') && service.isLogged()){
            NavbarSvc.goHome();
            return;
        }
        if ($routeParams.navId=='profile' && !service.isLogged()){
            NavbarSvc.goHome();
            return;
        }
        if ($routeParams.navId=='logout'){
            service.doLogout();
            return;
        }
        if ($routeParams.navId=='resetpassword'){
            if ($routeParams.code!==undefined)
                service.resetpasswordCode=$routeParams.code;
            else
                service.resetpasswordCode='';
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

	service.doReg=function(item){
	    $rootScope.$broadcast('show-errors-check-validity');
		 AccountRes.actionReg(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=angular.copy(response.data.data[0]);
                    $rootScope.$broadcast('account.create', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
    }

	service.doRecovery=function(email){
	    $rootScope.$broadcast('show-errors-check-validity');
		 AccountRes.actionRecovery(email).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    $rootScope.$broadcast('account.recovery', {email:email});
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
    }

	service.doResetpassword=function(code, password){
	    $rootScope.$broadcast('show-errors-check-validity');
		 AccountRes.actionResetpassword(code, password).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=angular.copy(response.data.data[0]);
                    $rootScope.$broadcast('account.resetpassword', {code:code});
                	$rootScope.$broadcast('account.login', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
    }

	service.doUpdate=function(item){
	    $rootScope.$broadcast('show-errors-check-validity');
		 AccountRes.actionUpdate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=angular.copy(response.data.data[0]);
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
	service.doDelete=function(){
         MessageSvc.confirm('account/delete/confirm', {},
         function(){
             AccountRes.actionDelete().then(
                function (response) {
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                        service.item={}
                        $rootScope.$broadcast('account.delete', service.item);
                    }
                },
                function (response) {
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                        MessageSvc.error(response.data.code, response.data);
                }
            );
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