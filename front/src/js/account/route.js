app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
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