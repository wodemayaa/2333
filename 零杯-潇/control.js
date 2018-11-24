function showtext1() {
  document.getElementById("describetext").innerHTML="<b><span id='movietitle'>《毒液：致命守护者》</span><span id='movietype'>107分钟-动作/科幻/惊悚</span> </b><br>《毒液：致命守护者》改编自漫威漫画。记者埃迪·布洛克（汤姆·哈迪 饰）在调查生命基金会的最新科学实验过程中，受到不明外星物质共生体的入侵与控制，历经挣扎成为亦正亦邪的超级英雄——毒液。他将以毒攻毒，破解生命基金会的惊天阴谋，拯救世界。";
}
function showtext2() {
  document.getElementById("describetext").innerHTML="<b><span id='movietitle'>《神奇动物：格林德沃之罪》</span><span id='movietype'>134分钟-奇幻/冒险/家庭 </span></b><br>为挫败格林德沃的阴谋，阿不思·邓布利多（裘德·洛 饰）向昔日的学生纽特·斯卡曼德寻求帮助。纽特欣然允诺，却没有意识到，他将踏上的会是一段充满艰险的未来征途。此时的魔法世界面临空前的分裂乱局，阶层鸿沟日益加深，爱与忠诚备受考验，至亲好友也可能反目成仇……";
}
function showtext3() {
  document.getElementById("describetext").innerHTML="<b><span id='movietitle'>《名侦探柯南：零的执行人》 </span><span id='movietype'>115分钟-动画/动作/冒险</span></b><br>一场大规模的恐怖袭击，一个牵扯无数内幕的神秘组织，这个关乎整个东京的可怕计划即将拉开帷幕…首脑云集的东京峰会举办在即，会场突然发生超大规模的爆炸事件，不仅在现场发现行踪诡异的安室透，毛利小五郎更是惨遭陷害。面对最危险任务，最烧脑的推理，最艰难的博弈，柯南能否在迷雾中寻找到唯一的真相。";
}
function showtext4() {
  document.getElementById("describetext").innerHTML="<b><span id='movietitle'>《无名之辈》</span><span id='movietype'>108分钟-喜剧/剧情</span> </b><br>在一座山间小城中，一对低配劫匪、一个落魄的泼皮保安、一个身体残疾却性格彪悍的残毒舌女以及一系列生活在社会不同轨迹上的小人物，在一个貌似平常的日子里，因为一把丢失的老枪和一桩当天发生在城中的乌龙劫案，从而被阴差阳错地拧到一起，发生的一幕幕令人啼笑皆非的荒诞喜剧。";
}
function showtext5() {
  document.getElementById("describetext").innerHTML="<b><span id='movietitle'>《飓风奇劫》</span><span id='movietype'>103分钟-动作/灾难/犯罪</span> </b><br>影片讲述财务部女监察探员(格蕾斯饰)负责押运一批6亿美元残旧货币到碎钞厂处理，然而当地罕见的飓风灾难即将来临，一群全副武装的盗贼想在居民全部疏散后“乘风打劫”，而当飓风达到致命的5级之后，所有精心计划都被打乱，他们发现需要一个金库密码，而这个密码只有女监察探员知道，她和所被劫持人质的生命面临威胁。";
}
function hidetext() {
  document.getElementById("describetext").innerHTML="<span style=\"font-size: 40px;color: darkorange\"><b>欢迎来到星影!</b></span><br>将鼠标移至海报上查看电影详细信息";
}
window.onload=function(){

  var container=document.getElementById('container');

  var list=document.getElementById('list');

  var buttons=document.getElementById('buttons').getElementsByTagName('span');

  var pre=document.getElementById('prev');

  var next=document.getElementById('next');

  var index=1;

  var animated=false;

  var timer;

  function showButton(){

    for(var i=0;i<buttons.length;i++){

      if(buttons[i].className=='on'){

        buttons[i].className='';

        break;

      }

    }

    buttons[index-1].className="on";

  }

  function animate(offset){

    animated=true;

    var newleft=parseInt(list.style.left)+offset;

    var time=450;//位移总时间

    var interval=15;//位移间隔时间

    var speed=offset/(time/interval);//每一次的位移量



    function go(){

      if((speed<0&&parseInt(list.style.left)>newleft)||(speed>0&&parseInt(list.style.                  left)<newleft)){

        list.style.left=parseInt(list.style.left)+speed+'px';

        setTimeout(go,interval);

      }

      else{

        animated=false;

        list.style.left=newleft+'px';

        if(newleft>-600){

          list.style.left=-3000+'px';

        }

        if(newleft<-3000){

          list.style.left=-600+'px';

        }

      }

    }

    go();

  }

  function play(){

    timer=setInterval(function(){

      next.onclick();

    },3000);

  }

  function stop(){

    clearInterval(timer);

  }



  next.onclick=function(){

    if(index==5){

      index=1;

    }

    else{

      index+=1;

    }

    showButton();

    if(animated==false){

      animate(-600);

    }

  }

  pre.onclick=function(){

    if(index==1){

      index=5;

    }

    else{

      index-=1;

    }

    showButton();

    if(animated==false){

      animate(600);

    }

  }



  for(var i=0;i<buttons.length;i++){

    buttons[i].onclick=function(){

      if(this.className=='on'){

        return;

      }

      var myIndex=parseInt(this.getAttribute('index'));

      var offset=-600*(myIndex-index);



      index=myIndex;

      showButton();

      if(animated==false){

        animate(offset);

      }

    }

  }

  container.onmouseover=stop;

  container.onmouseout=play;

  play();

}

