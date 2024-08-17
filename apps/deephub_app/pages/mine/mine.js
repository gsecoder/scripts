//index.js
//获取应用实例
const app = getApp()
/*
* https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html
* */

Page({
  data: {
    image_path: "/static/mine/default_mine.png",
    user_name: "",
    local_address: "请选择",
    phone_number: "",
    phone_code: ""
  },
  /*
  * 绑定获取手机号值
  * */
  bind_phone: function(e) {
    // console.log("e.detail.value_phone_number", e.detail.value);
    this.setData({
      phone_number: e.detail.value
    })
  },
  /*
  * 绑定获取验证码值
  * */
  bind_phone_code: function(e) {
    // console.log("e.detail.value_phone_code", e.detail.value)
    this.setData({
      phone_code: e.detail.value
    })
  },
  /*
  * 点击发送验证码
  * */
  send_phone_code: function () {
    if (this.data.phone_number.length != 11){
      // 弹窗警告
      wx.showToast({
        title: "手机号长度不合法",
        icon: "none", // success/loading/none
      })
    }
    // 手机正则匹配
    const reg = /^1[3|5|6|7|8|9]+\d{9}$/
    // console.log("...........: ", this.data.phone_number)
    if (!reg.test(this.data.phone_number)){
      wx.showToast({
        title: "手机号格式不正确",
        icon: "none"
      })
    }
    wx.request({
      url: "http://127.0.0.1:8000/send_phone_code",
      data:{
        phone_number: this.data.phone_number
      },
      method: "GET",
      success: function (res) {
        console.log(res);
      }
    })
  },
  /*
  * 手机登录
  * */
  phone_login: function(){
      // console.log(this.data.phone_number, this.data.phone_code);
      wx.request({
        url: 'http://127.0.0.1:8000/login',
        // complete: (res) => {},
        data: {
          "phone_number": this.data.phone_number,
          "phone_code": this.data.phone_code
        },
        // dataType: dataType,
        fail: (res) => {},
        // header: header,
        method: "POST",
        // responseType: responseType,
        success: (res) => {
          console.log(res.data)
        },
      })
  },

  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs',
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  /*
  * 获取用户绑定信息
  */
    getUserName: function () {
        // 调用微信提供的接口获取用户信息
        wx.getUserInfo({
            success: function (res) {
                console.log("success: ", res)
            },
            fail: function (res) {
                console.log("fail: ", res)
    
            }
        })
    },
  fetch_userinfo: function () {
    wx.openSetting({});
    const that = this;
    wx.getUserInfo({
      success: function (res) {
        console.log(res)
        that.setData({
          user_name: res.userInfo.nickName,
          image_path: res.userInfo.avatarUrl
        })
      },
      fail: function () {
        console.log(res)
      }
    })
  },
  
  /*获取用户位置信息*/
  fetch_address: function () {
    const that = this;
    wx.chooseLocation({
      success: function (res) {
        console.log(res);
        that.setData({
          local_address: res.address
        });
      }
    })
  }
})
