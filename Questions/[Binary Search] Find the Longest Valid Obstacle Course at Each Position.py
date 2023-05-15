# Question: https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# Hard

import bisect
from typing import List

class Solution:
    # O(n*log(n)) time and O(n) space
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        output = [1 for _ in range(len(obstacles))]

        aux = []

        for jdx, height in enumerate(obstacles):
            idx = bisect.bisect_right(aux, height)

            if idx == len(aux):
                aux.append(height)
            else:
                aux[idx] = height
                
            output[jdx] = idx + 1

        return output


# May 07, 2023

'''

# Kunal Wadhwa

'''

@DataProvider(name = "standardTransferNegativeCasesData")
  public static Object[][] standardTransferNegativeCasesData() {
    String beneId = successBeneMap.get(PAYOUT_NODAL_ACCOUNT).get(IMPS.getRequestTransferMode());
    return new Object[][] {
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(null)
            .build(),
        AMOUNT_IS_MISSING,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferMode(randomName())
            .build(),
        TRANSFER_MODE_NOT_AVAILABLE,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(null)
            .build(),
        TRANSFERID_MISSING,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomName())
            .build(),
        POST_DATA_EMPTY,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomRegex("[a-z]{71}"))
            .build(),
        REMARKS_MAX_LENGTH_EXCEEDED,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomRegex("[a-z]{41}"))
            .build(),
        TRANSFERID_MAX_LENGTH_EXCEEDED,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("1." + randomRegex("[1-9]{3}"))
            .build(),
        INVALID_AMOUNT,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomRegex("[1-9]{20}"))
            .build(),
        AMOUNT_IS_INVALID,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("0")
            .build(),
        AMOUNT_IS_INVALID,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .build(),
        TRANSFERID_ALREADY_EXISTS,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        TRANSFERID_INVALID_FORMAT,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        REMARKS_IS_INVALID,
        TRANSFER_ASYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(null)
            .build(),
        AMOUNT_IS_INVALID,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferMode(randomName())
            .build(),
        TRANSFER_MODE_NOT_AVAILABLE,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(null)
            .build(),
        TRANSFERID_MISSING,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomName())
            .build(),
        POST_DATA_EMPTY,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomRegex("[a-z]{71}"))
            .build(),
        REMARKS_MAX_LENGTH_EXCEEDED,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomRegex("[a-z]{41}"))
            .build(),
        TRANSFERID_MAX_LENGTH_EXCEEDED,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("1." + randomRegex("[1-9]{3}"))
            .build(),
        INVALID_AMOUNT,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomRegex("[1-9]{20}"))
            .build(),
        AMOUNT_IS_INVALID,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("0")
            .build(),
        AMOUNT_IS_INVALID,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .build(),
        TRANSFERID_ALREADY_EXISTS,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        TRANSFERID_INVALID_FORMAT,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        REMARKS_IS_INVALID,
        TRANSFER_ASYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(null)
            .build(),
        TRANSFER_AMOUNT_BELOW_MINIMUM_LIMIT,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(null)
            .build(),
        TRANSFERID_MISSING,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomName())
            .build(),
        POST_DATA_EMPTY,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomRegex("[a-z]{71}"))
            .build(),
        REMARKS_MAX_LENGTH_EXCEEDED,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomRegex("[a-z]{41}"))
            .build(),
        TRANSFERID_MAX_LENGTH_EXCEEDED,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("1." + randomRegex("[1-9]{3}"))
            .build(),
        INVALID_AMOUNT,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferMode(randomName())
            .build(),
        MODE_NOT_VALID_FOR_BENEFICIARY,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomRegex("[1-9]{20}"))
            .build(),
        TRANSFER_AMOUNT_EXCEEDS_MAXIMUM_LIMIT,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("0")
            .build(),
        TRANSFER_AMOUNT_BELOW_MINIMUM_LIMIT,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .paymentInstrumentId(PAYMENT_INSTRUMENT_ID)
            .build(),
        TransferSvcStatus.INSUFFICIENT_BALANCE,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .beneficiaryId(randomName())
            .build(),
        BENEFICIARY_NOT_EXIST,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .build(),
        TRANSFERID_ALREADY_EXISTS,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        TRANSFERID_INVALID_FORMAT,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        REMARKS_IS_INVALID,
        TRANSFER_SYNC
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(null)
            .build(),
        TRANSFER_AMOUNT_BELOW_MINIMUM_LIMIT,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(null)
            .build(),
        TRANSFERID_MISSING,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomName())
            .build(),
        POST_DATA_EMPTY,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomRegex("[a-z]{71}"))
            .build(),
        REMARKS_MAX_LENGTH_EXCEEDED,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomRegex("[a-z]{41}"))
            .build(),
        TRANSFERID_MAX_LENGTH_EXCEEDED,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("1." + randomRegex("[1-9]{3}"))
            .build(),
        INVALID_AMOUNT,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferMode(randomName())
            .build(),
        MODE_NOT_VALID_FOR_BENEFICIARY,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount(randomRegex("[1-9]{20}"))
            .build(),
        TRANSFER_AMOUNT_EXCEEDS_MAXIMUM_LIMIT,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .amount("0")
            .build(),
        TRANSFER_AMOUNT_BELOW_MINIMUM_LIMIT,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .paymentInstrumentId(PAYMENT_INSTRUMENT_ID)
            .build(),
        TransferSvcStatus.INSUFFICIENT_BALANCE,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .beneficiaryId(randomName())
            .build(),
        BENEFICIARY_NOT_EXIST,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .build(),
        TRANSFERID_ALREADY_EXISTS,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .transferId(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        TRANSFERID_INVALID_FORMAT,
        TRANSFER_SYNC_V1_POINT2
      },
      {
        getGenericTransferRequestBuilder(PAYOUT_NODAL_ACCOUNT, IMPS, TransferStatus.SUCCESS.name())
            .remarks(randomBothify("?#?#?#?") + "!@#$%")
            .build(),
        REMARKS_IS_INVALID,
        TRANSFER_SYNC_V1_POINT2
      },
    };
  }