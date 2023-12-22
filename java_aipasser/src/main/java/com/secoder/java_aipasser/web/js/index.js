(function(){
    const calendar = {
        curDate: new Date(),    /*当前的日期对象*/
        holidays: ['元旦节', '除夕', '春节', '清明节', '劳动节', '端午节', '中秋节', '国庆节'],

        init(){
            this.renderSelect(this.curDate);    /*渲染下拉列表*/
            this.getData(this.curDate); /*获取数据*/
        },

        /*渲染下拉框的数据*/
        renderSelect(d){
            const yearList=document.querySelector('.yearSelect .selectBox ul');
            const monthList=document.querySelector('.monthSelect .selectBox ul');
            const holidayList=document.querySelector('.holidaySelect .selectBox ul');

            const yearSelected = document.querySelector('.yearSelect .selected span');
            const monthSelected = document.querySelector('.monthSelect .selected span');
            const holidaySelected = document.querySelector('.holidaySelect .selected span');


            /*生成年份*/
            let li = '';
            yearList.innerHTML = '';
            for (let i = 1970; i <= 2050; i++) {
                li+=`<li ${i==d.getFullYear() ? 'class="active"': ''}">${i}年</li>`;
            }
            yearList.innerHTML = li;
            yearSelected.innerHTML = d.getFullYear() + "年";

            /*生成月份*/
            let lim = '';
            monthList.innerHTML = '';
            for (let i = 1; i <= 12; i++) {
                lim+=`<li ${i==(d.getMonth() + 1) ? 'class="active"': ''}">${i}月</li>`;
            }
            monthList.innerHTML = lim;
            monthSelected.innerHTML = (d.getMonth() + 1) + "月";

            /*生成假期*/
            let lih = '';
            holidayList.innerHTML = '';
            for (let i = 0; i <= this.holidays.length-1; i++) {
                lih+=`<li ${i == 0 ? 'class="active"': ''}>${this.holidays[i]}</li>`;
            }
            holidayList.innerHTML = lih;
            holidaySelected.innerHTML = this.holidays[0];

            /*dom渲染后执行事件*/
            this.selectBindEvent();
            this.closeSelect();
        },

        /*关闭下拉框*/
        closeSelect(){
            // 类数组，不能使用find方法，...是转成真正的数组
            var selects = [...document.querySelectorAll('.select')];
            // 找到那个元素有active
            var open = selects.find(select => select.classList.contains('active'));
            // 只有找到active元素后才会移除这个class
            open && open.classList.remove('active');
        },

        /*给topBar的日期下拉框添加点击事件*/
        selectBindEvent(){
            // 找到所有的下拉框
            var selects = document.querySelectorAll('.select');

            /*select每一个下拉框*/
            selects.forEach((select, index) =>{
                // 元素身上的集合
                var cl = select.classList;
                // 点击下拉框中里的选中内容
                var selected=select.querySelector('span');

                select.onclick = ev => {
                    if(cl.contains('active')){
                        /*
                        * 点击是自己，看自己身上有没有active，有的话去除掉
                        * */
                        cl.remove('active');
                    }else{
                        /*点击的是别人
                        * 关掉表人的active
                        * 添加自己的active
                        * */
                        this.closeSelect();
                        cl.add('active');

                        // 元素显示的时候，添加滚动条
                        this.scrollBar();
                    }


                    // 事件源
                    // console.log(ev.target)
                    if (ev.target.tagName != 'LI'){
                        // 说明现在点击的不是列表
                        return;
                    }
                    // 代码走到这里，说明点击的是列表
                    var lis2 = [...select.querySelectorAll('ul li')];
                    // 把找到的active删除
                    lis2.find(li => li.classList.contains('active')).classList.remove('active');
                    // 自己身上添加一个active
                    ev.target.classList.add('active');

                    /*通过索引区分年、月、假期不同的下拉框*/
                    switch (index) {
                        case 0: // 点击的是年
                            // 取到点击的年份，把中文去掉，然后把做个年份设置给curDate;
                            this.curDate.setFullYear(parseInt(ev.target.innerHTML));
                            selected.innerHTML = ev.target.innerHTML;
                            break;
                        case 1: // 点击的是月
                            this.curDate.setMonth(parseInt(ev.target.innerHTML)-1);
                            selected.innerHTML = ev.target.innerHTML;
                            break;
                        case 2: // 点击的是假期
                            selected.innerHTML = ev.target.innerHTML;
                            break;
                    }

                    console.log("测试", this.curDate);

                    // 请求数据
                    this.getData(this.curDate);
                };
            });

            /*添加月份切换功能*/
            this.monthChange();

            /*调用返回今天*/
            this.backToday();
        },

        /*滚动条*/
        scrollBar(){
            var scrollWrap = document.querySelector('.yearSelect .selectBox');
            var content = document.querySelector('.yearSelect .selectBox ul');
            var barWrap = document.querySelector('.yearSelect .selectBox .scroll');
            var bar = document.querySelector('.yearSelect .selectBox span');

            /*
            * 滑块初始化
            * */
            bar.style.transform =  content.style.transform = 'translateY(0)';
            // 根据下拉框的内容设置滑块的高度
            var multiple =  (content.offsetHeight + 18)/scrollWrap.offsetHeight;
            // 根据倍数算出滑块的高度，相反的关系
            multiple = multiple > 20 ? 20 : multiple; // 内容于内容父级的倍数不能超过20
            bar.style.height = scrollWrap.offsetHeight / multiple + 'px';

            /*
            * 滑块拖拽
            * */
            var scrollTop=0; //滑块条走的距离
            var maxHeight=barWrap.offsetHeight-bar.offsetHeight;  // 滑块能走的最大距离

            bar.onmousedown = function(ev) {
                var startY = ev.clientY; // 按下时数据的坐标
                var startT = parseInt(this.style.transform.split('(')[1]);  // 按下坐标元素走的距离

                bar.style.transition = content.style.transition = null;

                document.onmousemove = ev => {
                    scrollTop = ev.clientY - startY + startT;   // 滚动条移动的位置
                    scroll();
                }

                document.onmouseup = () => document.onmousemove = null;
            }

            /*滑动滚动条的时候，阻止事件冒泡*/
            barWrap.onclick = ev => ev.stopPropagation();

            function scroll() {
                // 上边走到头
                if (scrollTop < 0){
                    scrollTop=0;
                }
                // 下面走到头
                if (scrollTop>maxHeight){
                    scrollTop=maxHeight;
                }

                // 滚动条走的距离比例
                var scaleY = scrollTop / maxHeight;

                bar.style.transform = 'translateY(' + scrollTop + 'px)';
                content.style.transform = 'translateY(' + (scaleY * (scrollWrap.offsetHeight - content.offsetHeight - 18)) + 'px)';
            }

            /*滑动条滚动的事件*/
            scrollWrap.onwheel = ev =>{
                ev.deltaY > 0 ? scrollTop += 10: scrollTop -= 10;  // ev.deltaY > 0表示向下滚动

                bar.style.transition = content.style.transition = '.2s';
                scroll();

                // 阻止浏览器的默认行为
                ev.preventDefault();
            }

        },


        /*获取数据*/
        getData(d) {
            $.ajax({
                url: `https://www.rili.com.cn/rili/json/pc_wnl/${d.getFullYear()}/${d.getMonth() + 1}.js`,
                dataType: 'jsonp',

            });

            // 一定得把jsonp里的函数定义成全局的
            window.jsonrun_PcWnl = res => {
                console.log(res);

                //渲染日期
                this.renderDate(d, res.data);

                // 渲染农历
                this.renderLunar(res.data.find(item=>item.nian==d.getFullYear() &&  item.yue==d.getMonth()+1 && item.rid == d.getDate()));
            }
        },

        // 获取到某个月的最后一天的日期；月份是几月就传几月
        getEndDay:(year, month) => new Date(year,  month, 0).getDate() ,
        // 获取到某个月的第一天是周几， 月份是几月就传几月
        getFirstWeek:(year, month) => new Date(year, month - 1, 1).getDay(),
        // 删除节日上的超链接
        delTag:str=> str.replace(/<\/?.+?\/?>/g , ''),
        repair:v => v<10 ? '0'+v : v,

        renderDate(d, data){
            console.log(this.getEndDay(2023, 12));
            console.log(this.getFirstWeek(2023, 11));

            var tbody = document.querySelector('.dateWarp tbody');

            // 上个月的最后一天，月份不需要计算
            var lastEndDay = this.getEndDay(d.getFullYear(), d.getMonth());
            // 当前月的最后一天，月份要+1
            var curEndDay = this.getEndDay(d.getFullYear(), d.getMonth() + 1);
            // 当前月的第一天是周几
            var week = this.getFirstWeek(d.getFullYear(), d.getMonth()+1);

            // 上个月占几个格子
            var lastDateNum = week - 1;
            lastDateNum = week == 0 ? 6 : lastDateNum; // 如果当前月的第一天是周日，拿week的值为0，这时候需要给上个月留出6个格子

            // 上个月的起始的日期
            var prevStartDate = lastEndDay - lastDateNum;

            // 下个月起始的日期
            var nextStartDate = 1;
            // 当前月起始的日期
            var curStartDate = 1;


            console.log(lastEndDay, curEndDay, week);
            console.log("data: ", data);

            /*假期标红*/
            var calendar = document.querySelector('#calendar');
            calendar.classList.remove('active');

            var cn = -1; // 记录42次循环走的每 一次

            tbody.innerHTML = '';
            // 生成日期表格6*7
            for (var i=0; i<6; i++){
                var tr = document.createElement('tr');
                var td='';

                for (var j=0; j<7; j++){
                    cn++;

                    /*如果后段返回的数据jie字段有值的时候，需要jie字段来覆盖r2的值*/
                    // console.log("cn: ", cn++)
                    var festival = data[cn].jie ? this.delTag(data[cn].jie) : data[cn].r2;

                    // 休假+调休
                    var weekday = data[cn].jia == 90 ? 'weekday' : '';
                    var holiday = data[cn].jia > 90 ? 'holiday' : '';


                    if (cn < lastDateNum){  // 走上个月的日期
                        td += `<td>
                            <div class="prevMonth ${weekday + ' ' + holiday}">
                                <span>${++prevStartDate}</span>
                                <span>${festival}</span>
                            </div>
                        </td>`
                    } else if (cn >= lastDateNum + curEndDay) {  // 走下个月的日期
                        td += `<td>
                            <div class="nextMonth ${weekday + ' ' + holiday}">
                                <span>${nextStartDate++}</span>
                                <span>${festival}</span>
                            </div>
                        </td>`
                    } else {    // 走当前月的日期
                        var cl = '';
                        if (curStartDate==d.getDate()){ // 格子里的数值（日期）this.curDate里的日期对比
                             cl += 'active';
                        }

                        if (new Date().getFullYear() == d.getUTCFullYear() && new Date().getMonth() == d.getMonth() && new Date().getDate() == d.getDate() && d.getDate() == curStartDate){
                            cl = 'today';
                        }

                        td += `<td>
                            <div class="${'weekday' + '' + 'holiday'}">
                                <span>${curStartDate++}</span>
                                <span>${festival}</span>
                            </div>
                        </td>`;

                        /*
                        * 下面这个条件成立表示是节假日，最外层的父级需要添加红色的class
                        * 添加红色active的条件
                        *   1、当前的格式必需要有active的class，表示激活状态
                        *   2、 当前的格子必需有holiday的class，表示是个节日
                        *   3、节日必需为this.holiday里的某一个
                        * */
                        if (cl.indexOf('active') != -1 && holiday == "holiday"){
                            // 循环到这个dd是否是节日
                            var curDay = this.delTag(data[cn].jie);
                            this.holidays.includes(curDay) && calendar.classList.add('active');
                        }
                    }

                    tr.innerHTML= td;
                }

                tbody.appendChild(tr);
            }

            this.dateBindEvent(data);
        },

        /*切换月份*/
        monthChange() {
            var arrows = document.querySelectorAll('.arrow');

            // 上个月
            arrows[0].onclick = () => {
                // 月份减1
                this.curDate.setMonth(this.curDate.getMonth() - 1);
                // 渲染下拉框
                this.renderSelect(this.curDate);
                // 更新日期内容
                this.getData(this.curDate);
                // 如果下拉框显示的话，让其消失
                this.closeSelect();
            }

            // 下个月
            arrows[1].onclick = () => {
                this.curDate.setMonth(this.curDate.getMonth() + 1);
                this.renderSelect(this.curDate);
                this.getData(this.curDate);
                this.closeSelect();
            }
        },

        /*返回今天日期*/
        backToday(){
            var returnBtn = document.querySelector('#calendar .topBar button');

            returnBtn.onclick=()=>{
                // 今天的日期
                this.curDate=new Date();
                // 渲染下拉框
                this.renderSelect(this.curDate);
                // 更新日期内容
                this.getData(this.curDate);
            }
        },

        /*日期点击的功能，点击后渲染对应的详细信息*/
        dateBindEvent(data){
            console.log("dateBindEvent---data:", data);

            var boxes = [...document.querySelectorAll('.dateWrap tbody td div')];
            var last = boxes.find(box = () => box.classList.contains('active'));

            var curYear = this.curDate.getFullYear();   // 当前的年份
            var curMonth = this.curDate.getMonth(); // 当前的月份

            boxes.forEach((box, index)=> box.onclick= () => {
                // 获取点击的日期
                var date = box.children[0].innerHTML;

                // 选项卡
                var cl = box.classList;

                last && last.classList.remove('active');
                cl.add('active');
                last = box;

                // 如果下拉框显示，点击了需要隐藏
                this.closeSelect();

                if (cl.contains('prevMonth')){ // 点击的是上个月
                    this.curDate = new Date(curYear, curMonth-1, date); // 同时设置年月日

                    this.renderSelect(this.curDate);
                    this.getData(this.curDate);

                } else if (cl.contains('nextMonth')) {  // 点击的是下个月
                    this.curDate = new Date(curYear, curMonth+1, date); // 同时设置年月日

                    this.renderSelect(this.curDate);
                    this.getData(this.curDate);

                } else { // 点击的是当前月
                    var calendar = document.querySelector("#calendar");
                    var curDay = box.children(1).innerHTML; // 点击日期的农历
                    this.holidays.includes(curDay);
                    calendar.className = this.holidays.includes(curDay) ? 'active' : '';

                    this.renderLunar(data[index]);  // 渲染农历
                }
            });
        },

        renderLunar(data) {
            console.log(data);
            var date = document.querySelector('.right .date');
            var day = document.querySelector('.right .day');
            var ps = document.querySelectorAll('.right .lunar p');
            var holiday = document.querySelector('.right .holidayList');

            date.innerHTML = data.nian + '-' + this.repair(data.yue) + '-' + this.repair(data.ri);
            day.innerHTML = data.ri;
            ps[0].innerHTML = data.n_yueri;
            ps[1].innerHTML = data.gz_nian + "年" + data.shengxiao;
            ps[2].innerHTML = data.gz_yue + "月" + data.gz_ri;

            // 节日
            var holidays = this.delTag(data.jieri).split(',');
            holidays = holidays.length > 2 ? holidays.slice(0, 2) : holidays;
            holidayList.innerHTML="";
            holidays.forEach(holiday=>holidayList.innerHTML += `<li>${holiday}</li>`);
            console.log(holidays);

            // 宜忌
            var defaultDl = document.querySelectorAll('.suit .default dl');
            var hoverDl = document.querySelectorAll('.suit .hover dl');

            defaultDl[0].innerHTML='<dt>宜</dt>';
            data.yi.forEach(yi => defaultDl[0].innerHTML += `<dd>${yi}</dd>`);

            defaultDl[0].innerHTML='<dt>忌</dt>';
            data.ji.forEach(ji => defaultDl[1].innerHTML += `<dd>${ji}</dd>`);


            // hover对应的结构
            var str = '';
            data.yi.forEach(yi => str += `${yi}、`);
            hoverDl[0].innerHTML = '<dt>宜</dt><dd>' + str.substring(0, str.length-1) + '</dd>';

            var str = '';
            data.ji.forEach(ji => str += `${ji}、`);
            hoverDl[1].innerHTML = '<dt>忌</dt><dd>' + str.substring(0, str.length-1) + '</dd>';
        }
    };

    calendar.init();
})();