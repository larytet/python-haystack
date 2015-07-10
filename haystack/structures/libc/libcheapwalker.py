# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Loïc Jaquemet loic.jaquemet+python@gmail.com
#

__author__ = "Loic Jaquemet loic.jaquemet+python@gmail.com"

import os
import logging
import sys

from haystack.structures import heapwalker

log = logging.getLogger('libcheapwalker')


class LibcHeapWalker(heapwalker.HeapWalker):

    """Helper class that returns heap allocations and free chunks in a standard libc process heap """

    def _init_heap(self):
        log.debug('+ Heap @%x size: %d # %s' %
                  (self._mapping.start, len(self._mapping), self._mapping))
        self._allocs = None
        self._free_chunks = None
        assert hasattr(self._heap_module, 'iter_user_allocations')
        assert hasattr(self._heap_module, 'get_user_allocations')
        assert hasattr(self._heap_module, 'is_malloc_heap')
        assert hasattr(self._heap_module, 'mallocStruct')

    def get_user_allocations(self):
        """ returns all User allocations (addr,size) and only the user writeable part.
        addr and size EXCLUDES the HEAP_ENTRY header.
        """
        if self._allocs is None:
            self._set_chunk_lists()
        return self._allocs

    def get_free_chunks(self):
        """ returns all free chunks that are not allocated (addr,size) .
                addr and size EXCLUDES the HEAP_ENTRY header.
        """
        if self._free_chunks is None:
            self._set_chunk_lists()
        return self._free_chunks

    def _set_chunk_lists(self):
        self._allocs, self._free_chunks = self._heap_module.get_user_allocations(
            self._memory_handler, self._mapping)


class LibcHeapFinder(heapwalker.HeapFinder):

    # def _is_heap(self, _memory_handler, mapping):
    #    """test if a mapping is a heap - at least one allocation."""
    #    if not super(LibcHeapFinder,self)._is_heap(_memory_handler, mapping):
    #        return False
    #    # try to get at least one alloc.
    #    from haystack.structures.libc.ctypes_malloc import iter_user_allocations
    #    for x in iter_user_allocations(_memory_handler, mapping):
    #        return True
    #    return False

    def _init(self):
        """
        Return the heap configuration information
        :return: (heap_module_name, heap_class_name, heap_constraint_filename)
        """
        module_name = 'haystack.structures.libc.ctypes_malloc'
        heap_name = 'malloc_chunk'
        constraint_filename = os.path.join(os.path.dirname(sys.modules[__name__].__file__),'libcheap.constraints')
        log.debug('constraint_filename :%s', constraint_filename)
        return module_name, heap_name, constraint_filename

    def _init_heap_validation_depth(self):
        return 20

    def get_heap_mappings(self):
        """return the list of heaps that load as heaps

        Full overload of parent, to fix some bugs and prioritize.
        """
        heap_mappings = []
        for mapping in self._memory_handler:
            # BUG: python-ptrace read /proc/$$/mem.
            # file.seek does not like long integers like the start address
            # of the vdso or vsyscall mappigns
            if mapping.pathname in ['[vdso]', '[vsyscall]']:
                log.debug('Ignore system mapping %s', mapping)
            elif self._is_heap(mapping):
                heap_mappings.append(mapping)
        heap_mappings.sort(key=lambda m: m.start)
        # FIXME, isn't there a find() ?
        i = [
            i for (
                i,
                m) in enumerate(heap_mappings) if m.pathname == '[heap]']
        if len(i) == 1:
            h = heap_mappings.pop(i[0])
            heap_mappings.insert(0, h)
        return heap_mappings

    def get_heap_walker(self, heap):
        return LibcHeapWalker(self._memory_handler, self._heap_module, heap)
