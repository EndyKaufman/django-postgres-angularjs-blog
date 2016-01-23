app.factory('TagRes', function ($http, AppConst) {
    var service={};

    service.getList=function(){
        return $http({
                  method: 'GET',
                  url: AppConst.tag.urls.getData+'/list'
               });
    };

    return service;
  });