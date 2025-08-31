#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.1),
    on August 21, 2025, at 12:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.1'
expName = 'standardStroop'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s' % (expInfo['participant'], expName)
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\github\\study2\\stroop-task\\stroop(NON-AD)_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
    # return log file
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instruction" ---
    instImage = visual.ImageStim(
        win=win,
        name='instImage', 
        image='inst_stroop_1.JPG', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    instText = visual.TextStim(win=win, name='instText',
        text='Press bar to continue',
        font='Open Sans',
        pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    moveOn = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instruction2" ---
    instImage_2 = visual.ImageStim(
        win=win,
        name='instImage_2', 
        image='inst_stroop_2.JPG', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    instText_2 = visual.TextStim(win=win, name='instText_2',
        text='Press bar to continue',
        font='Open Sans',
        pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    moveOn_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "starttask" ---
    startText = visual.TextStim(win=win, name='startText',
        text='Press bar to start \nthe experimental task',
        font='Open Sans',
        pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    moveOn_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "sequenceGeneration" ---
    waitScreen = visual.TextStim(win=win, name='waitScreen',
        text='Generating stimuli...',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from fetchPracticeData
    import pandas as pd
    import numpy as np
    
    # folder containing the data (user dependent)
    #data_files = 'F:/work/2024 Bangor - ExFunc Workload within/tasks/data/' # Germano's folder
    data_files = 'D:/github/study2/stroop-task/data/' # New's folder
    
    # find file name based on this participant information
    csv_name = expInfo['participant'] + '_PracticeStroop.csv'
    
    # open this participant's practice data
    practiceData = pd.read_csv(f"{data_files}{csv_name}")
    
    # find rows corresponding to the last practice block
    rowIdx = practiceData["practiceRepetition.thisN"]==max(practiceData["practiceRepetition.thisN"])
    
    # find list of reaction times
    rt_correct = practiceData["myPract.RT_correctTrials"][rowIdx]
    
    # define initial duration
    Practice_correctTrials_MdnRT  = np.nanmedian(rt_correct)
    Practice_correctTrials_3qrtRT = np.nanpercentile(rt_correct, 75)
    
    # --- Initialize components for Routine "experimentalTrial" ---
    stroopStim = visual.TextStim(win=win, name='stroopStim',
        text='',
        font='Open Sans',
        units='deg', pos=(0, 0), height=5.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    stroopResp = keyboard.Keyboard()
    progressBar = visual.Progress(
        win, name='progressBar',
        progress=0.0,
        pos=(-0.9, 0.5), size=(1.8, 0.03), anchor='top-left', units='height',
        barColor='white', backColor=None, borderColor=None, colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-3
    )
    
    # --- Initialize components for Routine "blank" ---
    blankPeriod = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='blankPeriod')
    progressBar_2 = visual.Progress(
        win, name='progressBar_2',
        progress=0.0,
        pos=(-0.9, 0.5), size=(1.8, 0.03), anchor='top-left', units='height',
        barColor='white', backColor=None, borderColor=None, colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-2
    )
    fbSound = sound.Sound('600', secs=0.050, stereo=True, hamming=False,
        name='fbSound')
    fbSound.setVolume(1.0)
    
    # --- Initialize components for Routine "End" ---
    endImage = visual.ImageStim(
        win=win,
        name='endImage', 
        image='end slide.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    endText = visual.TextStim(win=win, name='endText',
        text='Press bar to submit',
        font='Open Sans',
        pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    moveOn_4 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction.started', globalClock.getTime())
    moveOn.keys = []
    moveOn.rt = []
    _moveOn_allKeys = []
    # keep track of which components have finished
    InstructionComponents = [instImage, instText, moveOn]
    for thisComponent in InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instImage* updates
        
        # if instImage is starting this frame...
        if instImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instImage.frameNStart = frameN  # exact frame index
            instImage.tStart = t  # local t and not account for scr refresh
            instImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instImage.started')
            # update status
            instImage.status = STARTED
            instImage.setAutoDraw(True)
        
        # if instImage is active this frame...
        if instImage.status == STARTED:
            # update params
            pass
        
        # *instText* updates
        
        # if instText is starting this frame...
        if instText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instText.frameNStart = frameN  # exact frame index
            instText.tStart = t  # local t and not account for scr refresh
            instText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instText, 'tStartRefresh')  # time at next scr refresh
            # update status
            instText.status = STARTED
            instText.setAutoDraw(True)
        
        # if instText is active this frame...
        if instText.status == STARTED:
            # update params
            pass
        
        # *moveOn* updates
        
        # if moveOn is starting this frame...
        if moveOn.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moveOn.frameNStart = frameN  # exact frame index
            moveOn.tStart = t  # local t and not account for scr refresh
            moveOn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moveOn, 'tStartRefresh')  # time at next scr refresh
            # update status
            moveOn.status = STARTED
            # keyboard checking is just starting
            moveOn.clock.reset()  # now t=0
        if moveOn.status == STARTED:
            theseKeys = moveOn.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _moveOn_allKeys.extend(theseKeys)
            if len(_moveOn_allKeys):
                moveOn.keys = _moveOn_allKeys[-1].name  # just the last key pressed
                moveOn.rt = _moveOn_allKeys[-1].rt
                moveOn.duration = _moveOn_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction.stopped', globalClock.getTime())
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction2.started', globalClock.getTime())
    moveOn_2.keys = []
    moveOn_2.rt = []
    _moveOn_2_allKeys = []
    # keep track of which components have finished
    Instruction2Components = [instImage_2, instText_2, moveOn_2]
    for thisComponent in Instruction2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instImage_2* updates
        
        # if instImage_2 is starting this frame...
        if instImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instImage_2.frameNStart = frameN  # exact frame index
            instImage_2.tStart = t  # local t and not account for scr refresh
            instImage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instImage_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instImage_2.started')
            # update status
            instImage_2.status = STARTED
            instImage_2.setAutoDraw(True)
        
        # if instImage_2 is active this frame...
        if instImage_2.status == STARTED:
            # update params
            pass
        
        # *instText_2* updates
        
        # if instText_2 is starting this frame...
        if instText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instText_2.frameNStart = frameN  # exact frame index
            instText_2.tStart = t  # local t and not account for scr refresh
            instText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instText_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instText_2.status = STARTED
            instText_2.setAutoDraw(True)
        
        # if instText_2 is active this frame...
        if instText_2.status == STARTED:
            # update params
            pass
        
        # *moveOn_2* updates
        
        # if moveOn_2 is starting this frame...
        if moveOn_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moveOn_2.frameNStart = frameN  # exact frame index
            moveOn_2.tStart = t  # local t and not account for scr refresh
            moveOn_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moveOn_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            moveOn_2.status = STARTED
            # keyboard checking is just starting
            moveOn_2.clock.reset()  # now t=0
        if moveOn_2.status == STARTED:
            theseKeys = moveOn_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _moveOn_2_allKeys.extend(theseKeys)
            if len(_moveOn_2_allKeys):
                moveOn_2.keys = _moveOn_2_allKeys[-1].name  # just the last key pressed
                moveOn_2.rt = _moveOn_2_allKeys[-1].rt
                moveOn_2.duration = _moveOn_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction2" ---
    for thisComponent in Instruction2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction2.stopped', globalClock.getTime())
    # the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "starttask" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('starttask.started', globalClock.getTime())
    moveOn_3.keys = []
    moveOn_3.rt = []
    _moveOn_3_allKeys = []
    # keep track of which components have finished
    starttaskComponents = [startText, moveOn_3]
    for thisComponent in starttaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "starttask" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *startText* updates
        
        # if startText is starting this frame...
        if startText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startText.frameNStart = frameN  # exact frame index
            startText.tStart = t  # local t and not account for scr refresh
            startText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startText.started')
            # update status
            startText.status = STARTED
            startText.setAutoDraw(True)
        
        # if startText is active this frame...
        if startText.status == STARTED:
            # update params
            pass
        
        # *moveOn_3* updates
        waitOnFlip = False
        
        # if moveOn_3 is starting this frame...
        if moveOn_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moveOn_3.frameNStart = frameN  # exact frame index
            moveOn_3.tStart = t  # local t and not account for scr refresh
            moveOn_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moveOn_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'moveOn_3.started')
            # update status
            moveOn_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(moveOn_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(moveOn_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if moveOn_3.status == STARTED and not waitOnFlip:
            theseKeys = moveOn_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _moveOn_3_allKeys.extend(theseKeys)
            if len(_moveOn_3_allKeys):
                moveOn_3.keys = _moveOn_3_allKeys[-1].name  # just the last key pressed
                moveOn_3.rt = _moveOn_3_allKeys[-1].rt
                moveOn_3.duration = _moveOn_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in starttaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "starttask" ---
    for thisComponent in starttaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('starttask.stopped', globalClock.getTime())
    # check responses
    if moveOn_3.keys in ['', [], None]:  # No response was made
        moveOn_3.keys = None
    thisExp.addData('moveOn_3.keys',moveOn_3.keys)
    if moveOn_3.keys != None:  # we had a response
        thisExp.addData('moveOn_3.rt', moveOn_3.rt)
        thisExp.addData('moveOn_3.duration', moveOn_3.duration)
    thisExp.nextEntry()
    # the Routine "starttask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sequenceGeneration" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('sequenceGeneration.started', globalClock.getTime())
    # keep track of which components have finished
    sequenceGenerationComponents = [waitScreen]
    for thisComponent in sequenceGenerationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sequenceGeneration" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waitScreen* updates
        
        # if waitScreen is starting this frame...
        if waitScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waitScreen.frameNStart = frameN  # exact frame index
            waitScreen.tStart = t  # local t and not account for scr refresh
            waitScreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waitScreen, 'tStartRefresh')  # time at next scr refresh
            # update status
            waitScreen.status = STARTED
            waitScreen.setAutoDraw(True)
        
        # if waitScreen is active this frame...
        if waitScreen.status == STARTED:
            # update params
            pass
        
        # if waitScreen is stopping this frame...
        if waitScreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waitScreen.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                waitScreen.tStop = t  # not accounting for scr refresh
                waitScreen.frameNStop = frameN  # exact frame index
                # update status
                waitScreen.status = FINISHED
                waitScreen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sequenceGenerationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sequenceGeneration" ---
    for thisComponent in sequenceGenerationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('sequenceGeneration.stopped', globalClock.getTime())
    # Run 'End Routine' code from stimuliCode
    """
    This script generates sequences of stroop stimuli
    """
    
    import numpy as np
    import pandas as pd
    
    trialAll_num = 216 # number of trials (must be even)
    trialCongruent_proportion = 1/2 # proportion of congruent trials
    trialCongruent_num_expected = trialAll_num * trialCongruent_proportion # num of match trials
    
    # create trial column
    trial = 1+np.arange(0,trialAll_num)
    
    # %% create congruence column (list of "congruent" and "incongruent") 
    # in the correct proportion and no more than 2 of the same condition (congruent, incongruent) consecutively
    
    # fill congruent column
    congruent = np.ones(np.int64(trialAll_num))
    toggleSwitch3 = 1
    while toggleSwitch3==1:
        for trialIdx in np.arange(0,trialAll_num):
            if trial[trialIdx]<=2:  # first two trials: random between 0 and 1
                congruent[trialIdx] = np.random.randint(0,2)
            else:
                if congruent[trialIdx-1]==congruent[trialIdx-2]:
                    congruent[trialIdx]=np.abs(congruent[trialIdx-1]-1)  # either 1 = abs(0-1)   or  0 = abs(1-1)
                else:
                    congruent[trialIdx] = np.random.randint(0,2)    
        # check that 50% congruent and 50% incongruent
        if sum(congruent)==(trialCongruent_num_expected):
            toggleSwitch3 = 0   
    
    # %% create word and color columns (combinations of words and colors)
    
    # pool of words and colors
    pool = ["yellow", "green", "red", "blue"]
    
    # initialize word and color columns
    word = np.empty(trialAll_num,dtype="<U6")
    color = np.empty(trialAll_num,dtype="<U6")
    
    toggleSwitch2 = 1
    while toggleSwitch2==1:
        
        # fill word and color columns
        for trialIdx in np.arange(0,trialAll_num):
            # for first trial, no need to worry about the preceding trial (because it does not exist)
            if trialIdx==0:  
                if congruent[trialIdx]==1:
                    word[trialIdx] = np.random.choice(pool,1)[0]
                    color[trialIdx] = word[trialIdx]
                else:
                    word[trialIdx] = np.random.choice(pool,1)[0]
                    pool_red = np.delete(pool, pool.index(word[trialIdx]) )  # reduce color pool 
                    color[trialIdx] = np.random.choice(pool_red,1)[0]
                
            # from second trial onwards
            else:   
                if congruent[trialIdx]==1:   
                    # reduce the pool so that not the same color is picked again
                    pool_red = np.delete(pool, pool.index(word[trialIdx-1]) )  # reduce color pool 
                    word[trialIdx] = np.random.choice(pool_red,1)[0]
                    color[trialIdx] = word[trialIdx]
                else:
                    toggleSwitch = 1
                    while toggleSwitch==1:
                        word[trialIdx] = np.random.choice(pool,1)[0]
                        pool_red = np.delete(pool, pool.index(word[trialIdx]) )  # reduce color pool 
                        color[trialIdx] = np.random.choice(pool_red,1)[0]
                        if word[trialIdx]!=word[trialIdx-1]  and  color[trialIdx]!=color[trialIdx-1]:
                            toggleSwitch = 0
                            
        # check that each color is picked at least 20% of the times in the word and color columns                    
        wordProportion = np.empty(len(pool),dtype=float)     
        colorProportion = np.empty(len(pool),dtype=float)     
        for poolIdx in np.arange(0,len(pool)):
            wordProportion[poolIdx] = sum(word==pool[poolIdx])/trialAll_num
            colorProportion[poolIdx] = sum(color==pool[poolIdx])/trialAll_num
        if np.min(wordProportion)>=0.20 and np.min(colorProportion)>=0.20:
            toggleSwitch2 = 0    
    
    # %% create expectedResponse
    # S= yellow, C= green, M= red, L= blue 
    expectedResponse = np.array(['key2press' for _ in np.arange(trialAll_num)])
    expectedResponse[color=="yellow"] = "s"
    expectedResponse[color=="green"]  = "c"
    expectedResponse[color=="red"]    = "m"
    expectedResponse[color=="blue"]   = "l"
    
    
    # %% create dataset
    # build a dataframe from dictionary
    
    sequenceDataset= pd.DataFrame({'trial': trial,
                                   'word': word,
                                   'color': color,
                                   'congruent': congruent,
                                   'expectedResponse': expectedResponse,
                                   'observedResponse': np.nan,
                                   'Accuracy': np.nan,
                                   'RT_allTrials': np.nan,
                                   'RT_correctTrials': np.nan,
                                   'trialDuration': np.nan,
                                   'step': np.nan})
    sequenceDataset
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # set up handler to look after randomisation of conditions etc
    experimentalBlock = data.TrialHandler(nReps=len(sequenceDataset), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='experimentalBlock')
    thisExp.addLoop(experimentalBlock)  # add the loop to the experiment
    thisExperimentalBlock = experimentalBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExperimentalBlock.rgb)
    if thisExperimentalBlock != None:
        for paramName in thisExperimentalBlock:
            globals()[paramName] = thisExperimentalBlock[paramName]
    
    for thisExperimentalBlock in experimentalBlock:
        currentLoop = experimentalBlock
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisExperimentalBlock.rgb)
        if thisExperimentalBlock != None:
            for paramName in thisExperimentalBlock:
                globals()[paramName] = thisExperimentalBlock[paramName]
        
        # --- Prepare to start Routine "experimentalTrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('experimentalTrial.started', globalClock.getTime())
        # Run 'Begin Routine' code from addData
        # adaptive duration
        if sequenceDataset.trial[experimentalBlock.thisN]==1:
            #sequenceDataset.trialDuration[experimentalBlock.thisN] = 0.5 + Practice_correctTrials_MdnRT   # for first 1 trial, use Median RT from practice block + 500 ms
            sequenceDataset.trialDuration[experimentalBlock.thisN] = 0.5 + Practice_correctTrials_3qrtRT  # for first 1 trial, use 3rd qrt RT from practice block + 500 ms
            
        else:
            sequenceDataset.trialDuration[experimentalBlock.thisN] = sequenceDataset.trialDuration[experimentalBlock.thisN-1] + sequenceDataset.step[experimentalBlock.thisN-1]   # for all other trials add a value depending on previous trial accuracy
        
        
        # add data about the sequence
        thisExp.addData('myExp.trial',            sequenceDataset.trial[experimentalBlock.thisN])
        thisExp.addData('myExp.word',           sequenceDataset.word[experimentalBlock.thisN])
        thisExp.addData('myExp.color',           sequenceDataset.color[experimentalBlock.thisN])
        thisExp.addData('myExp.congruent',      sequenceDataset.congruent[experimentalBlock.thisN])
        thisExp.addData('myExp.expectedResponse', sequenceDataset.expectedResponse[experimentalBlock.thisN])
        stroopStim.setColor(sequenceDataset.color[experimentalBlock.thisN], colorSpace='rgb')
        stroopStim.setText(sequenceDataset.word[experimentalBlock.thisN])
        stroopResp.keys = []
        stroopResp.rt = []
        _stroopResp_allKeys = []
        progressBar.setProgress(sequenceDataset.trial[experimentalBlock.thisN]/trialAll_num)
        # keep track of which components have finished
        experimentalTrialComponents = [stroopStim, stroopResp, progressBar]
        for thisComponent in experimentalTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "experimentalTrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stroopStim* updates
            
            # if stroopStim is starting this frame...
            if stroopStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stroopStim.frameNStart = frameN  # exact frame index
                stroopStim.tStart = t  # local t and not account for scr refresh
                stroopStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroopStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stroopStim.started')
                # update status
                stroopStim.status = STARTED
                stroopStim.setAutoDraw(True)
            
            # if stroopStim is active this frame...
            if stroopStim.status == STARTED:
                # update params
                pass
            
            # if stroopStim is stopping this frame...
            if stroopStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroopStim.tStartRefresh + sequenceDataset.trialDuration[experimentalBlock.thisN]-frameTolerance:
                    # keep track of stop time/frame for later
                    stroopStim.tStop = t  # not accounting for scr refresh
                    stroopStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stroopStim.stopped')
                    # update status
                    stroopStim.status = FINISHED
                    stroopStim.setAutoDraw(False)
            
            # *stroopResp* updates
            waitOnFlip = False
            
            # if stroopResp is starting this frame...
            if stroopResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stroopResp.frameNStart = frameN  # exact frame index
                stroopResp.tStart = t  # local t and not account for scr refresh
                stroopResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroopResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stroopResp.started')
                # update status
                stroopResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stroopResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stroopResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if stroopResp is stopping this frame...
            if stroopResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroopResp.tStartRefresh + sequenceDataset.trialDuration[experimentalBlock.thisN]-frameTolerance:
                    # keep track of stop time/frame for later
                    stroopResp.tStop = t  # not accounting for scr refresh
                    stroopResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stroopResp.stopped')
                    # update status
                    stroopResp.status = FINISHED
                    stroopResp.status = FINISHED
            if stroopResp.status == STARTED and not waitOnFlip:
                theseKeys = stroopResp.getKeys(keyList=['s','c','m','l','None'], ignoreKeys=["escape"], waitRelease=False)
                _stroopResp_allKeys.extend(theseKeys)
                if len(_stroopResp_allKeys):
                    stroopResp.keys = _stroopResp_allKeys[0].name  # just the first key pressed
                    stroopResp.rt = _stroopResp_allKeys[0].rt
                    stroopResp.duration = _stroopResp_allKeys[0].duration
                    # was this correct?
                    if (stroopResp.keys == str(sequenceDataset.expectedResponse[experimentalBlock.thisN])) or (stroopResp.keys == sequenceDataset.expectedResponse[experimentalBlock.thisN]):
                        stroopResp.corr = 1
                    else:
                        stroopResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *progressBar* updates
            
            # if progressBar is starting this frame...
            if progressBar.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                progressBar.frameNStart = frameN  # exact frame index
                progressBar.tStart = t  # local t and not account for scr refresh
                progressBar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progressBar, 'tStartRefresh')  # time at next scr refresh
                # update status
                progressBar.status = STARTED
                progressBar.setAutoDraw(True)
            
            # if progressBar is active this frame...
            if progressBar.status == STARTED:
                # update params
                pass
            
            # if progressBar is stopping this frame...
            if progressBar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > progressBar.tStartRefresh + sequenceDataset.trialDuration[experimentalBlock.thisN]-frameTolerance:
                    # keep track of stop time/frame for later
                    progressBar.tStop = t  # not accounting for scr refresh
                    progressBar.frameNStop = frameN  # exact frame index
                    # update status
                    progressBar.status = FINISHED
                    progressBar.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experimentalTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experimentalTrial" ---
        for thisComponent in experimentalTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('experimentalTrial.stopped', globalClock.getTime())
        # Run 'End Routine' code from addData
        # observed response
        if stroopResp.keys:
            sequenceDataset.observedResponse[experimentalBlock.thisN] = stroopResp.keys
        thisExp.addData('myExp.observedResponse',   sequenceDataset.observedResponse[experimentalBlock.thisN])
        
        # trialDuration
        thisExp.addData('myExp.trialDuration',      sequenceDataset.trialDuration[experimentalBlock.thisN])
        
        
        
        # Accuracy
        if sequenceDataset.observedResponse[experimentalBlock.thisN]==np.nan:
            sequenceDataset.Accuracy[experimentalBlock.thisN]             = int(0)
        else:
            sequenceDataset.Accuracy[experimentalBlock.thisN]             = int(sequenceDataset.observedResponse[experimentalBlock.thisN] == sequenceDataset.expectedResponse[experimentalBlock.thisN]) 
        thisExp.addData('myExp.Accuracy',         sequenceDataset.Accuracy[experimentalBlock.thisN])
            
        # RT all trials
        if stroopResp.keys:
            sequenceDataset.RT_allTrials[experimentalBlock.thisN]         = stroopResp.rt
            thisExp.addData('myExp.RT_allTrials',     sequenceDataset.RT_allTrials[experimentalBlock.thisN])
            
        # RT correct trials
        if sequenceDataset.Accuracy[experimentalBlock.thisN] == 1:
            sequenceDataset.RT_correctTrials[experimentalBlock.thisN] = stroopResp.rt
            thisExp.addData('myExp.RT_correctTrials',     sequenceDataset.RT_correctTrials[experimentalBlock.thisN])
        
        # adaptation
        sequenceDataset.step[experimentalBlock.thisN]    = 0.0  # no step change 
        thisExp.addData('myExp.step',         sequenceDataset.step[experimentalBlock.thisN])
        
        
            
            
        # check responses
        if stroopResp.keys in ['', [], None]:  # No response was made
            stroopResp.keys = None
            # was no response the correct answer?!
            if str(sequenceDataset.expectedResponse[experimentalBlock.thisN]).lower() == 'none':
               stroopResp.corr = 1;  # correct non-response
            else:
               stroopResp.corr = 0;  # failed to respond (incorrectly)
        # store data for experimentalBlock (TrialHandler)
        experimentalBlock.addData('stroopResp.keys',stroopResp.keys)
        experimentalBlock.addData('stroopResp.corr', stroopResp.corr)
        if stroopResp.keys != None:  # we had a response
            experimentalBlock.addData('stroopResp.rt', stroopResp.rt)
            experimentalBlock.addData('stroopResp.duration', stroopResp.duration)
        # the Routine "experimentalTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank.started', globalClock.getTime())
        # Run 'Begin Routine' code from fbCode
        # decide duration of blank element
        if stroopResp.keys:  # if a response was given, wait for the remainder before next trial
            blankDuration = sequenceDataset.trialDuration[experimentalBlock.thisN] - stroopResp.rt
        else:                 # if no response was given, it means that the time was already over for that trial
            blankDuration = 0
            
            
        # sound of feedback
        if stroopResp.corr:
            sound_volume = 0
        else:
            sound_volume = 1
        progressBar_2.setProgress(sequenceDataset.trial[experimentalBlock.thisN]/trialAll_num)
        fbSound.setSound('600', secs=0.050, hamming=False)
        fbSound.setVolume(sound_volume, log=False)
        fbSound.seek(0)
        # keep track of which components have finished
        blankComponents = [blankPeriod, progressBar_2, fbSound]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *progressBar_2* updates
            
            # if progressBar_2 is starting this frame...
            if progressBar_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                progressBar_2.frameNStart = frameN  # exact frame index
                progressBar_2.tStart = t  # local t and not account for scr refresh
                progressBar_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progressBar_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                progressBar_2.status = STARTED
                progressBar_2.setAutoDraw(True)
            
            # if progressBar_2 is active this frame...
            if progressBar_2.status == STARTED:
                # update params
                pass
            
            # if progressBar_2 is stopping this frame...
            if progressBar_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > progressBar_2.tStartRefresh + blankDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    progressBar_2.tStop = t  # not accounting for scr refresh
                    progressBar_2.frameNStop = frameN  # exact frame index
                    # update status
                    progressBar_2.status = FINISHED
                    progressBar_2.setAutoDraw(False)
            
            # if fbSound is starting this frame...
            if fbSound.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fbSound.frameNStart = frameN  # exact frame index
                fbSound.tStart = t  # local t and not account for scr refresh
                fbSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('fbSound.started', t)
                # update status
                fbSound.status = STARTED
                fbSound.play()  # start the sound (it finishes automatically)
            
            # if fbSound is stopping this frame...
            if fbSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fbSound.tStartRefresh + 0.050-frameTolerance:
                    # keep track of stop time/frame for later
                    fbSound.tStop = t  # not accounting for scr refresh
                    fbSound.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('fbSound.stopped', t)
                    # update status
                    fbSound.status = FINISHED
                    fbSound.stop()
            # update fbSound status according to whether it's playing
            if fbSound.isPlaying:
                fbSound.status = STARTED
            elif fbSound.isFinished:
                fbSound.status = FINISHED
            # *blankPeriod* period
            
            # if blankPeriod is starting this frame...
            if blankPeriod.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                blankPeriod.frameNStart = frameN  # exact frame index
                blankPeriod.tStart = t  # local t and not account for scr refresh
                blankPeriod.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankPeriod, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('blankPeriod.started', t)
                # update status
                blankPeriod.status = STARTED
                blankPeriod.start(blankDuration)
            elif blankPeriod.status == STARTED:  # one frame should pass before updating params and completing
                blankPeriod.complete()  # finish the static period
                blankPeriod.tStop = blankPeriod.tStart + blankDuration  # record stop time
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank.stopped', globalClock.getTime())
        # the Routine "blank" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed len(sequenceDataset) repeats of 'experimentalBlock'
    
    
    # --- Prepare to start Routine "End" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('End.started', globalClock.getTime())
    moveOn_4.keys = []
    moveOn_4.rt = []
    _moveOn_4_allKeys = []
    # keep track of which components have finished
    EndComponents = [endImage, endText, moveOn_4]
    for thisComponent in EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endImage* updates
        
        # if endImage is starting this frame...
        if endImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endImage.frameNStart = frameN  # exact frame index
            endImage.tStart = t  # local t and not account for scr refresh
            endImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endImage.started')
            # update status
            endImage.status = STARTED
            endImage.setAutoDraw(True)
        
        # if endImage is active this frame...
        if endImage.status == STARTED:
            # update params
            pass
        
        # *endText* updates
        
        # if endText is starting this frame...
        if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endText.frameNStart = frameN  # exact frame index
            endText.tStart = t  # local t and not account for scr refresh
            endText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endText.started')
            # update status
            endText.status = STARTED
            endText.setAutoDraw(True)
        
        # if endText is active this frame...
        if endText.status == STARTED:
            # update params
            pass
        
        # *moveOn_4* updates
        waitOnFlip = False
        
        # if moveOn_4 is starting this frame...
        if moveOn_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moveOn_4.frameNStart = frameN  # exact frame index
            moveOn_4.tStart = t  # local t and not account for scr refresh
            moveOn_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moveOn_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'moveOn_4.started')
            # update status
            moveOn_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(moveOn_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(moveOn_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if moveOn_4.status == STARTED and not waitOnFlip:
            theseKeys = moveOn_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _moveOn_4_allKeys.extend(theseKeys)
            if len(_moveOn_4_allKeys):
                moveOn_4.keys = _moveOn_4_allKeys[-1].name  # just the last key pressed
                moveOn_4.rt = _moveOn_4_allKeys[-1].rt
                moveOn_4.duration = _moveOn_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('End.stopped', globalClock.getTime())
    # check responses
    if moveOn_4.keys in ['', [], None]:  # No response was made
        moveOn_4.keys = None
    thisExp.addData('moveOn_4.keys',moveOn_4.keys)
    if moveOn_4.keys != None:  # we had a response
        thisExp.addData('moveOn_4.rt', moveOn_4.rt)
        thisExp.addData('moveOn_4.duration', moveOn_4.duration)
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            eyetracker.setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
