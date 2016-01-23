app.controller('NavbarCtrl', function ($scope, $rootScope, NavbarSvc) {
	$scope.NavbarSvc=NavbarSvc;

	$rootScope.$on('$routeChangeSuccess',function(event, current, previous){
	    NavbarSvc.init();
	    $rootScope.$broadcast('navbar.change', current, previous);
	});

	$rootScope.$on('auth.login',function(data){
	    NavbarSvc.init();
	    NavbarSvc.goHome();
	});

	$rootScope.$on('auth.logout',function(data){
	    NavbarSvc.init();
	    NavbarSvc.goHome();
	});

    NavbarSvc.init();
});