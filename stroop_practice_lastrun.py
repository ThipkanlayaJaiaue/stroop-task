#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.1),
    on August 21, 2025, at 13:44
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
expName = 'practiceStroop'  # from the Builder filename that created this script
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
        originPath='D:\\github\\study2\\stroop-task\\stroop_practice_lastrun.py',
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
    
    # --- Initialize components for Routine "startpractice" ---
    startText = visual.TextStim(win=win, name='startText',
        text='Press bar to start the practice',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
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
    
    # --- Initialize components for Routine "practiceTrial" ---
    stroopStim = visual.TextStim(win=win, name='stroopStim',
        text='',
        font='Open Sans',
        units='deg', pos=(0, 0), height=5.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    stroopResp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practiceTrial_feedback" ---
    fbText = visual.TextStim(win=win, name='fbText',
        text='',
        font='Open Sans',
        units='deg', pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    fbSound = sound.Sound('600', secs=0.050, stereo=True, hamming=False,
        name='fbSound')
    fbSound.setVolume(1.0)
    
    # --- Initialize components for Routine "practiceBlock_feedback" ---
    fbText_2 = visual.TextStim(win=win, name='fbText_2',
        text='',
        font='Open Sans',
        units='deg', pos=(0, 0.5), height=1.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    fbText_3 = visual.TextStim(win=win, name='fbText_3',
        text='If your accuracy was less than 70% you will repeat the practice block.\n\nPress bar to continue',
        font='Open Sans',
        pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    moveOn_4 = keyboard.Keyboard()
    
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
    moveOn_5 = keyboard.Keyboard()
    
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
    
    # set up handler to look after randomisation of conditions etc
    practiceRepetition = data.TrialHandler(nReps=5.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceRepetition')
    thisExp.addLoop(practiceRepetition)  # add the loop to the experiment
    thisPracticeRepetition = practiceRepetition.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeRepetition.rgb)
    if thisPracticeRepetition != None:
        for paramName in thisPracticeRepetition:
            globals()[paramName] = thisPracticeRepetition[paramName]
    
    for thisPracticeRepetition in practiceRepetition:
        currentLoop = practiceRepetition
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
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeRepetition.rgb)
        if thisPracticeRepetition != None:
            for paramName in thisPracticeRepetition:
                globals()[paramName] = thisPracticeRepetition[paramName]
        
        # --- Prepare to start Routine "startpractice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('startpractice.started', globalClock.getTime())
        moveOn_3.keys = []
        moveOn_3.rt = []
        _moveOn_3_allKeys = []
        # keep track of which components have finished
        startpracticeComponents = [startText, moveOn_3]
        for thisComponent in startpracticeComponents:
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
        
        # --- Run Routine "startpractice" ---
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
            for thisComponent in startpracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "startpractice" ---
        for thisComponent in startpracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('startpractice.stopped', globalClock.getTime())
        # check responses
        if moveOn_3.keys in ['', [], None]:  # No response was made
            moveOn_3.keys = None
        practiceRepetition.addData('moveOn_3.keys',moveOn_3.keys)
        if moveOn_3.keys != None:  # we had a response
            practiceRepetition.addData('moveOn_3.rt', moveOn_3.rt)
            practiceRepetition.addData('moveOn_3.duration', moveOn_3.duration)
        # the Routine "startpractice" was not non-slip safe, so reset the non-slip timer
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
        
        trialAll_num = 20 # number of trials (must be even)
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
        practiceBlock = data.TrialHandler(nReps=len(sequenceDataset), method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practiceBlock')
        thisExp.addLoop(practiceBlock)  # add the loop to the experiment
        thisPracticeBlock = practiceBlock.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeBlock.rgb)
        if thisPracticeBlock != None:
            for paramName in thisPracticeBlock:
                globals()[paramName] = thisPracticeBlock[paramName]
        
        for thisPracticeBlock in practiceBlock:
            currentLoop = practiceBlock
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
            # abbreviate parameter names if possible (e.g. rgb = thisPracticeBlock.rgb)
            if thisPracticeBlock != None:
                for paramName in thisPracticeBlock:
                    globals()[paramName] = thisPracticeBlock[paramName]
            
            # --- Prepare to start Routine "practiceTrial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('practiceTrial.started', globalClock.getTime())
            # Run 'Begin Routine' code from addData
            # add data about the sequence
            thisExp.addData('myPract.trial', sequenceDataset.trial[practiceBlock.thisN])
            thisExp.addData('myPract.word', sequenceDataset.word[practiceBlock.thisN])
            thisExp.addData('myPract.color', sequenceDataset.color[practiceBlock.thisN])
            thisExp.addData('myPract.congruent', sequenceDataset.congruent[practiceBlock.thisN])
            thisExp.addData('myPract.expectedResponse', sequenceDataset.expectedResponse[practiceBlock.thisN])
            stroopStim.setColor(str(sequenceDataset.color[practiceBlock.thisN]), colorSpace='rgb')
            stroopStim.setText(str(sequenceDataset.word[practiceBlock.thisN]))
            stroopResp.keys = []
            stroopResp.rt = []
            _stroopResp_allKeys = []
            # keep track of which components have finished
            practiceTrialComponents = [stroopStim, stroopResp]
            for thisComponent in practiceTrialComponents:
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
            
            # --- Run Routine "practiceTrial" ---
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
                    # update status
                    stroopStim.status = STARTED
                    stroopStim.setAutoDraw(True)
                
                # if stroopStim is active this frame...
                if stroopStim.status == STARTED:
                    # update params
                    pass
                
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
                if stroopResp.status == STARTED and not waitOnFlip:
                    theseKeys = stroopResp.getKeys(keyList=['s', 'c', 'm', 'l'], ignoreKeys=["escape"], waitRelease=False)
                    _stroopResp_allKeys.extend(theseKeys)
                    if len(_stroopResp_allKeys):
                        stroopResp.keys = _stroopResp_allKeys[0].name  # just the first key pressed
                        stroopResp.rt = _stroopResp_allKeys[0].rt
                        stroopResp.duration = _stroopResp_allKeys[0].duration
                        # was this correct?
                        if (stroopResp.keys == str(sequenceDataset.expectedResponse[practiceBlock.thisN])) or (stroopResp.keys == sequenceDataset.expectedResponse[practiceBlock.thisN]):
                            stroopResp.corr = 1
                        else:
                            stroopResp.corr = 0
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
                for thisComponent in practiceTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practiceTrial" ---
            for thisComponent in practiceTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('practiceTrial.stopped', globalClock.getTime())
            # Run 'End Routine' code from addData
            # observed response
            if stroopResp.keys:
                sequenceDataset.observedResponse[practiceBlock.thisN] = stroopResp.keys
            thisExp.addData('myPract.observedResponse',   sequenceDataset.observedResponse[practiceBlock.thisN])
            
            # Accuracy
            sequenceDataset.Accuracy[practiceBlock.thisN]             = int(sequenceDataset.observedResponse[practiceBlock.thisN] == sequenceDataset.expectedResponse[practiceBlock.thisN]) 
            thisExp.addData('myPract.Accuracy',         sequenceDataset.Accuracy[practiceBlock.thisN])
                
            # RT all trials
            sequenceDataset.RT_allTrials[practiceBlock.thisN]         = stroopResp.rt
            thisExp.addData('myPract.RT_allTrials',     sequenceDataset.RT_allTrials[practiceBlock.thisN])
                
            # RT correct trials
            if sequenceDataset.Accuracy[practiceBlock.thisN] == 1:
                sequenceDataset.RT_correctTrials[practiceBlock.thisN] = stroopResp.rt
                thisExp.addData('myPract.RT_correctTrials',     sequenceDataset.RT_correctTrials[practiceBlock.thisN])
            
            # check responses
            if stroopResp.keys in ['', [], None]:  # No response was made
                stroopResp.keys = None
                # was no response the correct answer?!
                if str(sequenceDataset.expectedResponse[practiceBlock.thisN]).lower() == 'none':
                   stroopResp.corr = 1;  # correct non-response
                else:
                   stroopResp.corr = 0;  # failed to respond (incorrectly)
            # store data for practiceBlock (TrialHandler)
            practiceBlock.addData('stroopResp.keys',stroopResp.keys)
            practiceBlock.addData('stroopResp.corr', stroopResp.corr)
            if stroopResp.keys != None:  # we had a response
                practiceBlock.addData('stroopResp.rt', stroopResp.rt)
                practiceBlock.addData('stroopResp.duration', stroopResp.duration)
            # the Routine "practiceTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "practiceTrial_feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('practiceTrial_feedback.started', globalClock.getTime())
            # Run 'Begin Routine' code from fbCode
            # text, color, and sound of feedback
            if stroopResp.corr:
                fb_text = 'Correct!'
                fb_col = 'green'
                sound_volume = 0
            else:
                fb_text = 'Incorrect'
                fb_col = 'red'
                sound_volume = 1
            
            # duration of feedback
            fb_duration = 0.5
            
            fbText.setColor(fb_col, colorSpace='rgb')
            fbText.setText(fb_text)
            fbSound.setSound('600', secs=0.050, hamming=False)
            fbSound.setVolume(sound_volume, log=False)
            fbSound.seek(0)
            # keep track of which components have finished
            practiceTrial_feedbackComponents = [fbText, fbSound]
            for thisComponent in practiceTrial_feedbackComponents:
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
            
            # --- Run Routine "practiceTrial_feedback" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fbText* updates
                
                # if fbText is starting this frame...
                if fbText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fbText.frameNStart = frameN  # exact frame index
                    fbText.tStart = t  # local t and not account for scr refresh
                    fbText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fbText, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    fbText.status = STARTED
                    fbText.setAutoDraw(True)
                
                # if fbText is active this frame...
                if fbText.status == STARTED:
                    # update params
                    pass
                
                # if fbText is stopping this frame...
                if fbText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fbText.tStartRefresh + fb_duration-frameTolerance:
                        # keep track of stop time/frame for later
                        fbText.tStop = t  # not accounting for scr refresh
                        fbText.frameNStop = frameN  # exact frame index
                        # update status
                        fbText.status = FINISHED
                        fbText.setAutoDraw(False)
                
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
                for thisComponent in practiceTrial_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practiceTrial_feedback" ---
            for thisComponent in practiceTrial_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('practiceTrial_feedback.stopped', globalClock.getTime())
            # the Routine "practiceTrial_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed len(sequenceDataset) repeats of 'practiceBlock'
        
        
        # --- Prepare to start Routine "practiceBlock_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practiceBlock_feedback.started', globalClock.getTime())
        # Run 'Begin Routine' code from fbCode_2
        # number of trials
        Practice_allTrials_num = len(sequenceDataset.Accuracy) 
        
        # number of trials with correct answer, among the trialRange specified below to discard the first 2 trials
        Practice_correctTrials_num = np.sum(sequenceDataset.Accuracy)
        
        # percentage of trials with correct answer
        Practice_correctTrials_pct= 100*Practice_correctTrials_num/ Practice_allTrials_num
        
        # Mdn RT for all responses
        Practice_allTrials_MdnRT = np.median(sequenceDataset.RT_allTrials)
        
        # Mdn RT for only correct responses
        if Practice_correctTrials_num> 0:
            Practice_correctTrials_MdnRT = np.nanmedian(sequenceDataset.RT_correctTrials)
        
        # 3rd quartile (i.e., 75th percentile) RT for only correct responses
        if Practice_correctTrials_num> 0:
            Practice_correctTrials_3qrtRT = np.nanpercentile(sequenceDataset.RT_correctTrials, 75)
        
        
        # message for feedback
        if Practice_correctTrials_num> 0:
            msg = "%i of %i correct responses \n%.2f%% correct \nMdn RT = %.2f s " %(Practice_correctTrials_num, Practice_allTrials_num, Practice_correctTrials_pct, Practice_correctTrials_MdnRT )
        else:
            msg = "%i of %i correct responses \n%.2f%% correct" %(Practice_correctTrials_num, Practice_allTrials_num, Practice_correctTrials_pct)
            
            
        # color of feedback
        if Practice_correctTrials_pct>=70:
            fb_col = 'green'     # if accuracy is at least the value above
        else:
            fb_col = 'red'
        fbText_2.setColor(fb_col, colorSpace='rgb')
        fbText_2.setText(msg
        )
        moveOn_4.keys = []
        moveOn_4.rt = []
        _moveOn_4_allKeys = []
        # keep track of which components have finished
        practiceBlock_feedbackComponents = [fbText_2, fbText_3, moveOn_4]
        for thisComponent in practiceBlock_feedbackComponents:
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
        
        # --- Run Routine "practiceBlock_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fbText_2* updates
            
            # if fbText_2 is starting this frame...
            if fbText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fbText_2.frameNStart = frameN  # exact frame index
                fbText_2.tStart = t  # local t and not account for scr refresh
                fbText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fbText_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fbText_2.status = STARTED
                fbText_2.setAutoDraw(True)
            
            # if fbText_2 is active this frame...
            if fbText_2.status == STARTED:
                # update params
                pass
            
            # *fbText_3* updates
            
            # if fbText_3 is starting this frame...
            if fbText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fbText_3.frameNStart = frameN  # exact frame index
                fbText_3.tStart = t  # local t and not account for scr refresh
                fbText_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fbText_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                fbText_3.status = STARTED
                fbText_3.setAutoDraw(True)
            
            # if fbText_3 is active this frame...
            if fbText_3.status == STARTED:
                # update params
                pass
            
            # *moveOn_4* updates
            
            # if moveOn_4 is starting this frame...
            if moveOn_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moveOn_4.frameNStart = frameN  # exact frame index
                moveOn_4.tStart = t  # local t and not account for scr refresh
                moveOn_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moveOn_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                moveOn_4.status = STARTED
                # keyboard checking is just starting
                moveOn_4.clock.reset()  # now t=0
            if moveOn_4.status == STARTED:
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
            for thisComponent in practiceBlock_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceBlock_feedback" ---
        for thisComponent in practiceBlock_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practiceBlock_feedback.stopped', globalClock.getTime())
        # Run 'End Routine' code from fbCode_2
        if Practice_correctTrials_pct >= 70:
            practiceRepetition.finished = True
        # the Routine "practiceBlock_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 5.0 repeats of 'practiceRepetition'
    
    
    # --- Prepare to start Routine "End" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('End.started', globalClock.getTime())
    moveOn_5.keys = []
    moveOn_5.rt = []
    _moveOn_5_allKeys = []
    # keep track of which components have finished
    EndComponents = [endImage, endText, moveOn_5]
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
        
        # *moveOn_5* updates
        waitOnFlip = False
        
        # if moveOn_5 is starting this frame...
        if moveOn_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moveOn_5.frameNStart = frameN  # exact frame index
            moveOn_5.tStart = t  # local t and not account for scr refresh
            moveOn_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moveOn_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'moveOn_5.started')
            # update status
            moveOn_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(moveOn_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(moveOn_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if moveOn_5.status == STARTED and not waitOnFlip:
            theseKeys = moveOn_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _moveOn_5_allKeys.extend(theseKeys)
            if len(_moveOn_5_allKeys):
                moveOn_5.keys = _moveOn_5_allKeys[-1].name  # just the last key pressed
                moveOn_5.rt = _moveOn_5_allKeys[-1].rt
                moveOn_5.duration = _moveOn_5_allKeys[-1].duration
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
    if moveOn_5.keys in ['', [], None]:  # No response was made
        moveOn_5.keys = None
    thisExp.addData('moveOn_5.keys',moveOn_5.keys)
    if moveOn_5.keys != None:  # we had a response
        thisExp.addData('moveOn_5.rt', moveOn_5.rt)
        thisExp.addData('moveOn_5.duration', moveOn_5.duration)
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
