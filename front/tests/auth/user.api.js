describe('Auth API (user):', function() {
  var helpers = require('./../helpers.js');

  var logoutResponse = undefined, userResponse = undefined, profileResponse = undefined;

  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        helpers.executeAndReturnJson(
            'callback(window.AppConfig);',
            function(data){

                helpers.postJson('/auth/login', {
                    email:'user@email.com',
                    password:'user@email.com'
                }, function(response){
                    userResponse = response;

                    helpers.postJson('/auth/update', {
                        firstname:'New Name',
                        email:'user@email.com'
                    }, function(response){
                        profileResponse = response;

                        helpers.postJson('/auth/logout', {
                        }, function(response){
                            logoutResponse = response;

                            done();

                        });

                    });

                });

            }
        );
    })
  });

  it('POST /auth/login as user role & check structure', function() {
    expect(typeof userResponse).toEqual('object');
    expect(userResponse.data[0].userData).toBeDefined();
    expect(userResponse.data[0].userId).toBeDefined();
    var userData = userResponse.data[0].userData;
    var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
    for (var i=0; i<fields.length; i++)
        expect(userData[fields[i]]).toBeDefined();
    if (userData.roles.length>0)
        expect(userData.roles[0]).toEqual('user');
  });

  it('POST /auth/update & check structure', function() {
    expect(typeof profileResponse).toEqual('object');
    expect(profileResponse.data[0].userData).toBeDefined();
    expect(profileResponse.data[0].userId).toBeDefined();
    var userData = profileResponse.data[0].userData;
    var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
    for (var i=0; i<fields.length; i++)
        expect(userData[fields[i]]).toBeDefined();
    if (userData.roles.length>0)
        expect(userData.roles[0]).toEqual('user');

    expect(userData.firstname).toEqual('New Name');
  });

  it('POST /auth/logout & check structure', function() {
    expect(logoutResponse.code).toEqual('ok');
  });

});