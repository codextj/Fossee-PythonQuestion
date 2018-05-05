<p>Watson has started feeling dizzy, pain in his abdominal has become unbearable and his lips have turned bluish; Sherlock is having uncontrollable spasms of laughter. You must be thinking what the hell is going on ??<br />can you guess whose devil mind has set up such a trap well this challenge is not about guessing the name of the villain but helping Sherlock to save Watson and its none other than Moriarty he loves inflicting pain and putting Sherlock in ironical and inescapable situations like this remember "The Reichenbach Fall" episode of Sherlock?</p>
<p><a title="combination lock" href="https://en.wikipedia.org/wiki/Combination_lock">https://en.wikipedia.org/wiki/Combination_lock</a></p>
<p><strong>Objectives</strong>:-<br />1) OPEN NUMERIC/COMBINATION* LOCK BRIEFCASE <br />unlock briefcase it contains an antidote for the poison which can save Watson but on the flip side failing to unlock it in minimum possible time Sherlock will himself become the victim of the same poison as the briefcase has a mini poison bomb which gets activated once you start rotating a dial with the timer being set to the minimum possible unlock time for the briefcase, if briefcase is not unlocked in minimum possible time (ie you have to turn/rotate dial and unlock briefcase optimally), bomb will get triggered.</p>
<p>2) Escape from Room<br />unlock the door which also has Number lock but this one looks strange.<br />key of the combination lock of Door is formed by (appending from leftmost to rightmost dial)number of times you have rotated the dial in order to make it read the corresponding digit in the number key of the briefcase.</p>
<p><em>INPUT FORMAT</em><br />line 1: key, current_numbers_that_each_dials_are_showing,&nbsp; time_required_to_rotate_dial_once combinationLock_briefcase<br />line 2: what are dials of door_number_lock&nbsp; is showing currently, time_required_to_rotate_dial_once combinationLock_door<br />line 3: special number pattern which is used in dials of number lock of door.</p>
<p><em>OUTPUT</em><br />print instructions<br />time taken to unlock the briefcase<br />number key to the door lock<br />&lt;instruction<br />state after rotation&gt; for each dial<br />total time taken to rotate dials of the door_number_lock&nbsp;&nbsp;</p>
<hr />
<p>&nbsp;</p>
<p>1905 6998 622<br />3523 354<br />7 1 9 2 0 4 8 6 5 3</p>
<hr />
<p>&nbsp;</p>
<p>rotate dial in any direction by 5<br />already set<br />rotate dial towards left by 1<br />rotate dial towards right by 3<br />5598 milliseconds<br />Door lock key 5013<br />rotate dial towards right by 1<br />5 3 7 1 9 2 0 4 8 6<br />rotate dial towards right by 4<br />0 4 8 6 5 3 7 1 9 2<br />rotate dial towards right by 2<br />1 9 2 0 4 8 6 5 3 7<br />already set<br />3 7 1 9 2 0 4 8 6 5<br />4354 milliseconds</p>
<hr />
<p>&nbsp;</p>
<p><strong>EXPLANATION</strong></p>
<p>number lock on briefcase reads from leftmost dial to rightmost dial as<br /><span style="color: #000080;">6998</span> to unlock briefcase change this to <span style="color: #00ff00;">1905</span> <br />|6| |9| |9| |8| (current _configuration_of_lock)<br />{1}{9}{0}{5} (key)</p>
<p>|<span style="color: #003366;">6</span>| 7 8 9 0 {<span style="color: #00ff00;">1</span>} 2 3 4 5 [initially dial will be in this config]<br />{1} 2 3 4 5 6 7 8 9 0 [after rotation dial should be in this config]<br />each time you rotate a dial it cost you some time and you have to turn each of the four dials in minimum time.</p>
<p>622 (time in milliseconds to rotate once, combinationLock_briefcase)<br />354 (time in milliseconds to rotate once, combinationLock_door)</p>
<p><br />-combinationLock_briefcase<br />|6| 7 8 9 0 {1} 2 3 4 5 (currently dial reads 6)<br />&lt;--- rotating left 1 time<br />|7| 8 9 0 {1} 2 3 4 5 6(now dial reads 7)<br />it cost you 622 ms and you have to rotate 4 more times to make dial read {1} so add 4*622ms more to totalTimeSpentToUnlock this briefcase.</p>
<blockquote>
<p>YOU CAN ROTATE DIAL EITHER TO THE LEFT OR RIGHT</p>
<p><span style="color: #000000;">| |</span> number shown at dial</p>
<p>{ } number that we want dial to show</p>
<p><br />|<span style="color: #333399;">8</span>| 9 0 1 2 3 4 {<span style="color: #00ff00;">5</span>} 6 7<br />&lt;--- rotating 7 times to left<br />|<span style="color: #00ff00;">5<span style="color: #000000;">|</span></span> 6 7 8 9 0 1 2 3 4</p>
<p><br />or you can do <br />|<span style="color: #003366;">8</span>| 9 0 1 2 3 4 {<span style="color: #00ff00;">5</span>} 6 7<br />rotating 3 time to right--&gt;<br />1) |<span style="color: #003366;">7</span>| 8 9 0 1 2 3 4 {<span style="color: #00ff00;">5</span>} 6 <br />2) |<span style="color: #003366;">6</span>| 7 8 9 0 1 2 3 4 {<span style="color: #00ff00;">5</span>}<br />3) |<span style="color: #00ff00;">5</span>| 6 7 8 9 0 1 2 3 4<br />so you should do right rotate to save time</p>
<p>5+0+1+3 = 9*622 =&gt;&nbsp; 5598ms</p>
</blockquote>
<p>&nbsp;</p>
<p>7 1 9 2 0 4 8 6 5 3(unique pattern used in door combination lock)</p>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>
<p>SAMPLE INPUT <br />5974 1612 458<br />7070 354<br />2 4 5 7 6 1 9 3 0 8</p>
<hr />
<p>&nbsp;</p>
<p>SAMPLE OUTPUT<br />rotate dial towards left by 4<br />rotate dial towards left by 3<br />rotate dial towards right by 4<br />rotate dial towards left by 2<br />5954 milliseconds<br />Door lock key 4342<br />rotate dial towards right by 2<br />4 5 7 6 1 9 3 0 8 2<br />rotate dial towards right by 1<br />3 0 8 2 4 5 7 6 1 9<br />rotate dial towards right by 2<br />4 5 7 6 1 9 3 0 8 2<br />rotate dial towards left by 2<br />2 4 5 7 6 1 9 3 0 8<br />3206 milliseconds</p>
<hr />
<p><br />wondering where did Sherlock get the password from to unlock the briefcase in the first place?<br />[add a link here to Q5 ]</p>
