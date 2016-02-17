app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/reg', {
        templateUrl: 'views/account/reg.html',
        controller: 'AccountCtrl',
        navId: 'reg'
      })
      .when('/recovery', {
        templateUrl: 'views/account/recovery.html',
        controller: 'AccountCtrl',
        navId: 'recovery'
      })
      .when('/login', {
        templateUrl: 'views/account/login.html',
        controller: 'AccountCtrl',
        navId: 'login'
      })
      .when('/profile', {
        templateUrl: 'views/account/profile.html',
        controller: 'AccountCtrl',
        navId: 'profile'
      });
});