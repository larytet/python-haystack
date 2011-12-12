#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Loic Jaquemet loic.jaquemet+python@gmail.com
#

'''
This module holds some basic utils function.
'''

__author__ = "Loic Jaquemet loic.jaquemet+python@gmail.com"

import itertools
import logging
import numpy
import os
import array
import struct
import sys


from haystack.config import Config

log = logging.getLogger('utils')

def int_array_cache(filename):
  if os.access(filename,os.F_OK):
    # load
    f = file(filename,'r')
    nb = os.path.getsize(f.name)/4 # simple TODO 
    my_array = array.array('L')
    my_array.fromfile(f,nb)
    return my_array
  return None

def int_array_save(filename, lst):
  my_array = array.array('L')
  my_array.extend(lst)
  my_array.tofile(file(filename,'w'))
  return my_array


def closestFloorValueNumpy(val, lst):
  ''' return the closest previous value to where val should be in lst (or val)
   please use numpy.array for lst
  ''' 
  indicetab = numpy.searchsorted(lst, [val])
  ind = indicetab[0]
  i = max(0,ind-1)
  return lst[i], i

def closestFloorValueOld(val, lst):
  ''' return the closest previous value to val in lst '''
  if val in lst:
    return val, lst.index(val)
  prev = lst[0]
  for i in xrange(1, len(lst)-1):
    if lst[i] > val:
      return prev, i-1
    prev = lst[i]
  return lst[-1], len(lst)-1

closestFloorValue = closestFloorValueNumpy
  

def dequeue(addrs, start, end):
  ''' 
  dequeue address and return vaddr in interval ( Config.WORDSIZE ) from a list of vaddr
  dequeue addrs from 0 to start.
    dequeue all value between start and end in retval2
  return remaining after end, retval2
  '''
  ret = []
  while len(addrs)> 0  and addrs[0] < start:
    addrs.pop(0)
  while len(addrs)> 0  and addrs[0] >= start and addrs[0] <= end - Config.WORDSIZE:
    ret.append(addrs.pop(0))
  return addrs, ret

def getHeapPointers(dumpfilename, mappings):
  ''' Search Heap pointers values in stack and heap.
      records values and pointers address in heap.
  '''
  import signature
  
  F_VALUES = Config.getCacheFilename(Config.CACHE_HS_POINTERS_VALUES, dumpfilename)
  F_HEAP = Config.getCacheFilename(Config.CACHE_HEAP_ADDRS, dumpfilename)
  F_STACK = Config.getCacheFilename(Config.CACHE_STACK_VALUES, dumpfilename)
  log.debug('reading from %s'%(F_VALUES))
  values = int_array_cache(F_VALUES)
  heap_addrs = int_array_cache(F_HEAP)
  stack_addrs = int_array_cache(F_STACK)
  if values is None or heap_addrs is None:
    log.info('Making new cache')
    log.info('getting pointers values from stack ')
    stack_enumerator = signature.PointerEnumerator(mappings.getStack())
    stack_enumerator.setTargetMapping(mappings.getHeap()) #only interested in heap pointers
    stack_enum = stack_enumerator.search()
    stack_offsets, stack_values = zip(*stack_enum)
    log.info('  got %d pointers '%(len(stack_enum)) )
    log.info('Merging pointers from heap')
    heap_enum = signature.PointerEnumerator(mappings.getHeap()).search()
    heap_addrs, heap_values = zip(*heap_enum) # TODO change to offsets
    log.info('  got %d pointers '%(len(heap_enum)) )
    # merge
    values = sorted(set(heap_values+stack_values))
    int_array_save(F_VALUES , values)
    int_array_save(F_HEAP, heap_addrs)
    int_array_save(F_STACK, stack_values)
    log.info('\t[-] we have %d unique pointers values out of %d orig.'%(len(values), len(heap_values)+len(stack_values)) )
  else:
    log.info('[+] Loading from cache')
    log.info('\t[-] we have %d unique pointers values, and %d pointers in heap .'%(len(values), len(heap_addrs)) )
  aligned = numpy.asarray(filter(lambda x: (x%4) == 0, values))
  not_aligned = numpy.asarray(sorted( set(values)^set(aligned)))
  log.info('\t[-] only %d are aligned values.'%(len(aligned) ) )
  return values,heap_addrs, aligned, not_aligned


def getAllocations(dumpfilename, mappings, heap):
  ''' Search malloc_chunks in heap .
      records addrs and sizes.
  '''
  # TODO if linux
  import libc.ctypes_malloc
  
  f_addrs = Config.getCacheFilename(Config.CACHE_MALLOC_CHUNKS_ADDRS, dumpfilename+'.%s'%(heap.start))
  f_sizes = Config.getCacheFilename(Config.CACHE_MALLOC_CHUNKS_SIZES, dumpfilename+'.%s'%(heap.start))
  log.debug('reading from %s'%(f_addrs))
  addrs = int_array_cache(f_addrs)
  sizes = int_array_cache(f_sizes)
  if addrs is None or sizes is None:
    log.info('[+] Making new cache - getting malloc_chunks from heap ')
    allocations = libc.ctypes_malloc.getUserAllocations(mappings, heap)
    addrs, sizes = zip(*allocations)
    int_array_save(f_addrs, addrs)
    int_array_save(f_sizes, sizes)
    log.info('\t[-] we have %d malloc_chunks'%(len(addrs)) )
  else:
    log.info('[+] Loading from cache')
  log.info('\t[-] we have %d malloc_chunks'%(len(addrs)) )
  return addrs, sizes

'''
  a shareBytes array of bytes. no allocation buffer should be made, only indexes.
'''
class SharedBytes():
  def __init__(self, src):
    self.src = src
    self.start = 0
    self.end = len(src)
    return
  
  def __makeMe(self, start, end):
    if end < 0:
      raise ValueError
    if start < 0:
      raise ValueError    
    sb = SharedBytes(self.src)
    sb.start = start
    sb.end = end
    return sb
  
  def unpack(self, typ, bytes):
    return struct.unpack(typ, str(bytes))

  def pack(self, typ, *val):
    return struct.pack(typ, *val)

  def __getslice__(self, start, end):
    if start < 0: # reverse
      start = self.end+start
    elif start == sys.maxint:
      start = self.start
    if end < 0: # reverse
      end = self.end+end
    elif end == sys.maxint:
      end = self.end
    return self.__makeMe(start, end)

  def __len__(self):
    return self.end-self.start

  def __getitem__(self, i):
    if isinstance(i, slice):
      return self.__getslice__(i)
    if i < 0: # reverse
      i = self.end+i
    return  self.src[self.start+i]

  def __getattribute__(self, *args):
    log.debug( '__getattribute__ %d %s'%(id(self), args))
    if len(args) == 1 and args[0] == 'src':
      return getattr(self, 'src')
    return self.src[self.start:self.end]#.__getattribute__(*args)

  def __getattr__(self, *args):
    log.debug('__getattr__ %d %s'%(id(self), args))
    return getattr(self.src[self.start:self.end], *args)
  
  def __setstate__(self, d):
    self.__dict__ = d.copy()

  def __getstate__(self):
    return self.__dict__.copy()
    
  def __str__(self):
    return self.src[self.start:self.end]

  def __repr__(self):
    return repr(self.src[self.start:self.end])

  def __iter__(self):
    return iter(self.src[self.start:self.end])


def nextStructure(context, struct):
  ind = context.structures_addresses.index(struct.vaddr)
  val = context.structures_addresses[ind+1]
  if val not in context.structures:
    return None
  if struct.vaddr+len(struct) != val:
    print '*** WARNING nextStruct is not concurrent to struct'
  return context.structures[val]


def printNext(ctx, s):
  s2 = nextStructure(ctx, s)
  s2.decodeFields()
  print s2.toString()
  return s2

def flatten(listOfLists):
  return itertools.chain.from_iterable(listOfLists)


