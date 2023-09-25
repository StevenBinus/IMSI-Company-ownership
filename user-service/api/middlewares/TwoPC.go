package middlewares

// import (
// 	"context"
// 	"net/http"

// 	"github.com/gin-gonic/gin"
// 	"github.com/jmoiron/sqlx"
// )

// // Coordinator data structure
// type Coordinator struct {
// 	DB *sqlx.DB
// }

// // Participant data structure
// type Participant struct {
// 	DB *sqlx.DB
// }

// // Prepare prepares the transaction in the participant
// func (p *Participant) Prepare(ctx context.Context, tx *sqlx.Tx, prepareData interface{}) error {
// 	// Perform your transaction operations based on the prepareData
// 	// For example, insert a new record into the orders table

// 	return nil
// }

// // Commit commits the transaction in the participant
// func (p *Participant) Commit(ctx context.Context, tx *sqlx.Tx) error {
// 	err := tx.Commit()
// 	if err != nil {
// 		return err
// 	}
// 	return nil
// }

// // Rollback rolls back the transaction in the participant
// func (p *Participant) Rollback(ctx context.Context, tx *sqlx.Tx) error {
// 	err := tx.Rollback()
// 	if err != nil {
// 		return err
// 	}
// 	return nil
// }

// // ExecuteDistributedTransaction runs the distributed transaction using 2PC
// func (c *Coordinator) ExecuteDistributedTransaction(ctx context.Context, prepareData interface{}, participants []*Participant) error {
// 	// Phase 1: Prepare
// 	var preparedTransactions []*sqlx.Tx
// 	for _, p := range participants {
// 		tx, err := p.DB.Beginx()
// 		if err != nil {
// 			return err
// 		}

// 		err = p.Prepare(ctx, tx, prepareData)
// 		if err != nil {
// 			return err
// 		}

// 		preparedTransactions = append(preparedTransactions, tx)
// 	}

// 	// Phase 2: Commit
// 	for i, p := range participants {
// 		err := p.Commit(ctx, preparedTransactions[i])
// 		if err != nil {
// 			// Rollback transactions if commit fails
// 			for _, tx := range preparedTransactions {
// 				_ = p.Rollback(ctx, tx)
// 			}
// 			return err
// 		}
// 	}

// 	return nil
// }

// // register2PCEndpoints registers the distributed transaction endpoints
// func register2PCEndpoints(router *gin.Engine, coordinator *Coordinator, participants []*Participant) {
// 	router.POST("/distributed-transaction", func(c *gin.Context) {
// 		// Prepare data from the request
// 		var prepareData interface{}
// 		err := c.BindJSON(&prepareData)
// 		if err != nil {
// 			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
// 			return
// 		}

// 		// Execute the distributed transaction
// 		err = coordinator.ExecuteDistributedTransaction(c, prepareData, participants)
// 		if err != nil {
// 			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
// 			return
// 		}

// 		c.JSON(http.StatusOK, gin.H{"status": "success"})
// 	})
// }

// // Call the Register User Detail to process the register
// url := "http://10.1.32.26:8000/user-detail-test"
// payload := []byte(`{
// 	"fullname": "string",
// 	"address": "string",
// 	"company": "string",
// 	"NIK": "50000",
// 	"email_addr": "string",
// 	"login_id": 111
//   }`) // Body payload
// req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
// if err != nil {
// 	txHandle.Rollback()
// 	// Handle the error
// 	exceptions.AppException(c, "Register Failed 1")
// 	return
// }
// req.Header.Set("Content-Type", "application/json") // Include transaction ID in the request headers

// // Send the request to the PaymentService
// client := &http.Client{}
// resp, err := client.Do(req)
// if err != nil {
// 	txHandle.Rollback()
// 	// Handle the error
// 	exceptions.AppException(c, "Register Failed 2")
// 	return
// }
// defer resp.Body.Close()

// // Check the response from the RegisterDetailService
// if resp.StatusCode != http.StatusOK {
// 	// Register failed
// 	// Rollback the transaction
// 	txHandle.Rollback()
// 	exceptions.AppException(c, "Register Failed 4")
// 	// Handle the error
// }
