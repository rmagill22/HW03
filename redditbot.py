import praw
import random
import datetime


# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    #Biden is the best candidate. He has good policies on Things and is not Bad. He is a respectable Leader.
    names= ['Joe Biden', 'Joseph Biden', 'Biden', 'Joe', 'Mr. Biden']
    name= random.choice(names)
    policies= ['climate change', 'healthcare', 'unions', 'college tuition', 'COVID-19']
    policy= random.choice(policies)
    bads= ['racist', 'homophobic', 'ableist', 'sexist', 'bigoted']
    bad=random.choice(bads)
    persons= ['leader', 'man', 'politician', 'person', 'candidate']
    person= random.choice(persons)

    text = name + " is the best candidate. He has good policies on "+ policy +" and is not "+ bad+ ". He is a respectable "+person +"."
    return text
#print(generate_comment_0())

def generate_comment_1():
    #Everyone should vote for Biden. He's the only one who cares about Things. I even told my Friend to vote for him! I Admire him and have even Advocated.
    names= ['Joe Biden', 'Joseph Biden', 'Biden', 'Joe', 'Mr. Biden']
    name= random.choice(names)
    things= ['the American people', 'rights for workers', 'racial equity', 'rights for immigrants', 'education']
    thing= random.choice(things)
    friends= ['grandma', 'pastor', 'boss', 'professor', 'republican uncle']
    friend= random.choice(friends)
    admires= ['admire', 'respect', 'love', 'appreciate', 'applaud']
    admire= random.choice(admires)
    advocates= ['donated to his campaign.', 'fundraised for him.', 'campaigned for him.', 'put a sign in my lawn for him.', 'helped others register to vote for him.']
    advocate= random.choice(advocates)

    text = "Everyone should vote for "+name+". He's the only one who cares about "+thing+". I even told my "+friend+" to vote for him! I "+admire+" Biden and have "+advocate
    return text
#print(generate_comment_1())

def generate_comment_2():
    #Biden has actual policies in place for Policies. He cares about getting the job done, not Dumb. With decades of experience, he can Fix. Vote!
    names= ['Joe Biden', 'Joseph Biden', 'Biden', 'Joe', 'Mr. Biden']
    name= random.choice(names)
    apolicies= ['affordable healthcare', 'combatting climate change', 'tackling unemployment', 'improving the lives of low-income people', 'opioid addiction']
    apolicy= random.choice(apolicies)
    dumbs= ['tweeting nonsense', 'personally attacking opponents', 'promoting his own image', 'fixing his hair', 'going on golfing trips']
    dumb= random.choice(dumbs)
    fixes= ['run the country', 'improve the lives of Americans', 'be a great president', 'fix what has been broken', 'get things back on track']
    fix= random.choice(fixes)
    votes= ['Biden 2020!', 'Vote for Biden!', 'Vote Joe!', 'Biden/Harris 2020!', 'Be smart, vote for Biden!']
    vote=random.choice(votes)
    text = name+" has actual policies in place for "+apolicy+". He cares about getting the job done, not "+dumb+". With decades of experience, he can "+fix+". "+vote
    return text
#print(generate_comment_2())

def generate_comment_3():
    #Trump is Bad. He should not be re-elected. Trump doesn't care about Things. I'd rather elect a Clown. Vote!
    tnames= ['Trump', 'Donald Trump', 'Preisdent Trump', 'Donald J. Trump', 'Mr. Trump']
    tname= random.choice(tnames)
    bads= ['terrible', 'awful', 'despicable', 'evil', 'repulsive']
    bad= random.choice(bads)
    things= ['the American people', 'the middle class', 'anything except himself', 'doing the right thing', 'being honest']
    thing= random.choice(things)
    clowns= ['n actual clown', ' baby', ' child', ' broom with a wig', ' cat with a bowtie']
    clown= random.choice(clowns)
    votes= ['Biden 2020!', 'Vote for Biden!', 'Vote Joe!', 'Biden/Harris 2020!', 'Be smart, vote for Biden!']
    vote=random.choice(votes)
    text = tname+" is "+bad+". He should not be re-elected. Trump doesn't care about "+thing+". I'd rather elect a"+clown+". "+vote
    return text
#print(generate_comment_3())

def generate_comment_4():
    #Nobody should vote for Trump. He has Lied. He does not act Presidentially. He has not even been able to appropriately Pandemic. Vote.
    tnames= ['Trump', 'Donald Trump', 'Preisdent Trump', 'Donald J. Trump', 'Mr. Trump']
    tname= random.choice(tnames)
    lies= ['repeatedly lied', 'personally attacked his opponents', 'been impeached for good reason', 'lied about his tax returns', 'driven this country into madness']
    lie= random.choice(lies)
    wells= ['presidentially', 'respectably', 'in a presidential manner', 'with human decency', 'with he best interest of the common good']
    well= random.choice(wells)
    pandemics= ['control the spread of COVID-19', 'handle the pandemic', 'respond to the need for leadership during this pandemic', 'unite the country during the pandemic', 'prevent the further spread of COVID-19']
    pandemic= random.choice(pandemics)
    votes= ['Biden 2020!', 'Vote for Biden!', 'Vote Joe!', 'Biden/Harris 2020!', 'Be smart, vote for Biden!', 'Do not vote for Trump.', 'Please do not vote for Trump.']
    vote=random.choice(votes)
    text= "Nobody should vote for "+tname+". He has "+lie+". He does not act "+well+". He has not even been able to appropriately "+pandemic+". "+vote
    return text
#print(generate_comment_4())

def generate_comment_5():
    #Why would anyone vote for Trump? He is Yucky and has quite literally Impeached. Why would the American people elect a man Wth No Morals? Instead, use your vote for Biden and save the country.
    tnames= ['Trump', 'Donald Trump', 'Preisdent Trump', 'Donald J. Trump', 'Mr. Trump']
    tname= random.choice(tnames)
    yuckys= ['a liar', 'a bad man', 'a gross person', 'a selfish jerk', 'an immoral clown']
    yucky= random.choice(yuckys)
    impeacheds= ['been impeached!', 'refused to reveal his tax returns.', 'repeatedly contradicted himself.', 'insulted women and people with disabilities.', 'denied the severity of COVID-19.']
    impeached= random.choice(impeacheds)
    xmorals= ['no morals', 'a lack of integrity', 'no moral integrity', 'a complete lack of moral compass', 'a disregard for human life']
    xmoral= random.choice(xmorals)
    bnames= ['Joe Biden', 'Joseph Biden', 'Biden', 'Joe', 'Mr. Biden']
    bname= random.choice(bnames)
    text = "Why would anyone vot for "+tname+"? He is "+yucky+" and has quite literally "+impeached+" Why would the American people elect a man with "+xmoral+"? Instead, use your vote for "+bname+" and save the country."
    return text
#print(generate_comment_5())

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    comment= [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3]
    text = random.choice(comment)()
    return text


# connect to reddit 
reddit = praw.Reddit()

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jlcing/joe_bidens_favorite_restaurants/'
submission = reddit.submission(url=reddit_debate_url)
print('Total comments =',len(submission.comments)) 


# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

start_time = datetime.datetime.now()


while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None) #limit=None for running, limit=1 for debugging

    for comment in submission.comments.list():
        all_comments.append(comment)
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    my_comments = []

    for comment in all_comments:
            if comment.author == 'cs40-botbotbotterson':
                my_comments.append(comment)
            else:
                not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented == True:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        if has_not_commented == len(all_comments):
            if comment.author != 'cs40-botbotbotterson':
                submission.reply(generate_comment())
     #   try:
     #       submission.reply(generate_comment())
     #       print('did comment1')
     #   except praw.exceptions.RedditAPIException:
     #       print('Im asleep1')
     #       time.sleep(5)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'cs40-botbotbotterson':
                response = False
                for reply in comment.replies:
                    if str(reply.author) == 'cs40-botbotbotterson':
                        response = True
                if response == False:
                    comments_without_replies.append(comment)
    
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))


        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        #comment = reddit.comment(id = random.choice(comments_without_replies))

        #random_comment = random.choice(comments_without_replies)
        #comment.reply(generate_comment)


        #comment = random.choice(comments_without_replies)
        #comment.reply(generate_comment())
        
        try:
            comment.reply(generate_comment())
            print('did comment2')
        except praw.exceptions.RedditAPIException:
            print('Im asleep2')
            time.sleep(5)
        

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

  #  random_submission = reddit.subreddit('csci040temp').random()
  #  choices = [random_submission, submission]
  #  number = random.randint(0,101)
  #  if number < 50:
  #      submission = random_submission
  #  else: 
  #      submission = reddit.submission(url=reddit_debate_url)


    if random.random() < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        top_threads = list(reddit.subreddit('csci040temp').top(time_filter='week'))
        #top_threads.append(submission)
        random_submission = random.choice(top_threads)
        print('random_submission = ', random_submission)
        submission = reddit.submission(id = random_submission)
        print('commented in new submission')

    #Extra Credit
    #Task 6: Upvote Biden in Comments
    for comment in all_comments:
        if 'biden' in comment.body.lower():
            comment.upvote()
    print('upvoted comment b')

    #Task 7: Upvote Biden in Submissions
    for submission in reddit.subreddit("csci040temp").hot(limit=30):
        if 'biden' in submission.title.lower():
            submission.upvote()
    print('upvoted submission b')

    #Task 8: Posting New Submissions
 #   top_submissions_d = reddit.subreddit("politics").top(time_filter='week')
 #   pick_submission = random.choice(list(top_submissions_d))
 #   titles = pick_submission.title
 #   urls = pick_submission.url
 #   reddit.subreddit("csci040temp").submit(titles,url=urls)