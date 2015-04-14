class PyPractice:
    def secondMax(self):
        int_array = [123, 34, 54, 65, 45, 76]

        m_max = int_array[0]
        sec_max = int_array[1]

        if sec_max > m_max:
            temp = m_max
            m_max = sec_max
            sec_max = temp

        for num in int_array[2:]:
            if num > m_max:
                sec_max = m_max
                m_max = num
            elif num < m_max and num > sec_max:
                sec_max = num

        return sec_max


print PyPractice().secondMax()