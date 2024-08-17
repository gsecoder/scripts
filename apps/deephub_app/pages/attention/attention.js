// pages/attention.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    attention_ups: [
        "小明",
        "小红",
        "小王"
    ],
    up_xiaoming:{
      name: "小明",
      age: 25,
      sex: "男"
    },
    imageList: [
      "/static/index/more.png",
      "/static/index/more.png",
    ]
  },
  upload_image: function() {
    const that = this;
    wx.chooseImage({
      count: 9,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success: function(res){
        that.setData({
          imageList: that.data.imageList.concat(res.tempFilePaths)
        })
      },
      fail: function(res){
        console.log(res)
      },
      complete: function (res) {
        console.log(res)
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})