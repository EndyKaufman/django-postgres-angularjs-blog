describe('Auth API (user):', function() {
  var mytools = require('./../tools.js');

  var logoutData = undefined, userData = undefined;

  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        mytools.executeAndReturnJson(
            'callback(window.AppConfig);',
            function(data){

                mytools.postJson('/auth/login', {
                    email:'user@email.com',
                    password:'user@email.com'
                }, function(response){
                    userData = response.data;

                    mytools.postJson('/auth/logout', {
                    }, function(response){
                        logoutData = response;

                        done();

                    });

                });

            }
        );
    })
  });

  it('try post /auth/login as user role and check structure', function() {
    expect(typeof userData).toEqual('object');
    expect(typeof userData.userData).toEqual('object');
    expect(typeof userData.userId).toEqual('number');
    var data = userData.userData;
    var fields = ['userName', 'userEmail', 'firstName', 'lastName', 'roles'];
    for (var i=0; i<fields.length; i++)
        expect(data[fields[0]] != undefined ? true : false).toEqual(true);
    if (data.roles.length>0)
        expect(data.roles[0]).toEqual('user');
  });

  it('try post /auth/logout and check structure', function() {
    expect(logoutData.code).toEqual('ok');
  });

});