app.factory('ProjectRes', function ($http, AppConst) {
    var service={};

    service.getItem=function(name){
        return $http({
                  method: 'GET',
                  url: '/project/item/'+name
               });
    };
    service.getList=function(){
        return $http({
                  method: 'GET',
                  url: '/project/list'
               });
    };
    service.getSearch=function(searchText){
        return $http({
                  method: 'GET',
                  url: '/project/search/'+searchText
               });
    };
    service.getListByTag=function(tagText){
        return $http({
                  method: 'GET',
                  url: '/project/listbytag/'+tagText
               });
    };
    service.actionUpdate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post('/project/update/'+item.id, item);
    }
    service.actionCreate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post('/project/create', item);
    }
    service.actionDelete=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post('/project/delete/'+item.id, item);
    }

    return service;
  });