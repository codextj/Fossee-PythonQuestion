<p>In James high school there is this maths exhibition going on and one of his classmates has made this lottery game where the participant will be presented with some buckets and each bucket has a name and contains as many chits as there are ways of rearranging the name of the bucket each chit will have one word written on it which is one of the possible rearrangement of letters of bucket name they have to select a bucket then say which word they think they are going to pick out.</p>
<p>James is kinda of Math Whiz He always chooses to pickup chit from one of those buckets which have the highest probability of winning (fewer the chits bucket have better are chances for picking a word of your choice) and the word that he always bets on is the name of the bucket itself as its just easier to remember and no need of finding rearranged word formed using letters of bucket name.</p>
<p>James is responsible for ensuring that no one at the exhibition is scamming other students If he wins a game he doesn't care about an investigation as James gets to eat ice creme but if he doesn't win then he does a complete investigation and makes a report.</p>
<blockquote>
<p>|&nbsp; &nbsp; cei&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |</p>
<p>|eic&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;cie&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp; &nbsp;|&nbsp; <span style="color: #000080;">yay</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|</p>
<p>|&nbsp; &nbsp;&nbsp;iec&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp; |&nbsp; &nbsp; &nbsp; yya&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |</p>
<p>|&nbsp; &nbsp; &nbsp; &nbsp;eci &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #000080;">ice</span>&nbsp; &nbsp; &nbsp; &nbsp;|&nbsp; |&nbsp;ayy&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|</p>
<p>&nbsp;\_______________/&nbsp; &nbsp; \______________/</p>
<p>&nbsp; bucket: ice&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; bucket: yay</p>
<p><strong>Sample Input Format</strong></p>
<p>5 bucket names<br />chits in bucket 1<br />chits in bucket 2<br />..<br />chits in bucket 5<br />outcome ie result whether James Won or not</p>
<p><strong>Sample Output Format</strong><br />name all the buckets from which if James picks then he will have the best chance of winning.<br />(If James doesn't Win he thinks it is because the game might be rigged<br />so if any of the conditions givens below becomes true then that bucket was rigged.)<br />Investigation report on bucket_name<br /><strong>&gt;</strong>probability miscalculation this bucket contains more number of chits than the actual number of ways we can rearrange the word.<br /><strong>&gt;</strong>probability miscalculation this bucket contains fewer chits than the actual number of ways we can rearrange the word.<br /><strong>&gt;</strong>chosen word is not present in bucket ie bucket doesn't have chit with the name bucket_name in it.&nbsp;<br /><strong>&gt;</strong>chits in this bucket have biased towards some words ie multiple chits have the same&nbsp;word written on them.</p>
<p>bucket bucket_name was rigged True/False.</p>
</blockquote>
<p>Note:</p>
<p>remember chosen word is always bucket_name ie when your doing&nbsp;investigation on ice bucket your bucket_name is ice and chosen word is ice similarly when you are doing it on pool&nbsp;bucket bucket_name is pool&nbsp;and word James will be betting on will be pool.</p>
<p>print statements exactly.<br /><br /></p>
<hr />
<p>&nbsp;</p>
<p><em>(actual input will have 5 bucket names)</em></p>
<p>SAMPLE INPUT 0</p>
<p>pop push<br />opp ppo pop<br />puhs hpus phus uphs shup husp push hups suhp suph sphu hsup hpsu spuh shpu ushp uhps hspu pshu psuh uhsp usph phsu upsh<br />True</p>
<p>SAMPLE OUTPUT 0</p>
<p>pop</p>
<hr />
<p>&nbsp;</p>
<p>SAMPLE INPUT 1<br />good evil pool<br />ogdo dgoo dogo oodg odog odgo godo ogod doog oogd gdoo good<br />leiv levi eilv ievl lvie evli eivl lvei viel veil vlie elvi live ielv ivel liev ilve evil veli vile vlei ivle ilev eliv<br />poool ploo oplo oolp olop polo opol lopo lpoo oopl olpo loop<br />False</p>
<p>SAMPLE OUTPUT 1<br />good pool<br />Investigation Report on bucket good<br />bucket good was rigged False.<br />Investigation Report on bucket evil<br />bucket evil was rigged False.<br />Investigation Report on bucket pool<br />chosen word is not present in bucket ie bucket doesn't have chit with the name pool in it.<br />bucket pool was rigged True.</p>
<hr />
<p>&nbsp;</p>
<p>SAMPLE INPUT 2<br />wow girl<br />wwo oww wow cow meow www<br />lrig kid rgil kid glri kid rigl kid rlig rgli rlgi glir ilgr irlg iglr gril grli igrl lirg ilrg<br />False</p>
<p>SAMPLE OUTPUT 2<br />wow<br />Investigation Report on bucket wow<br />probability miscalculation this bucket contains more number of chits than the actual number of ways we can rearrange the word.<br />bucket wow was rigged True.<br />Investigation Report on bucket girl<br />chosen word is not present in bucket ie bucket doesn't have chit with the name girl in it.<br />chits in this bucket have biased towards some words ie multiple chits have the same word written on them.<br />probability miscalculation this bucket contains fewer chits than the actual number of ways we can rearrange the word.<br />bucket girl was rigged True.</p>
<hr />
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
